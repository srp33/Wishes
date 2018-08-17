import sys, gzip

metadata = sys.argv[1]
PatientCancerType = sys.argv[2]
tumorTPM = sys.argv[3]
transposedTumorTPM = sys.argv[4]
dataOutFile = sys.argv[5]
metadataOutFile = sys.argv[6]
condensedMutationData = sys.argv[7]


# functions copied from fslg_piccololab/code/utilities.py
def readMatrixFromFile(filePath, numLines=None):
    matrix = []
    for line in file(filePath, 'rU'):
        if numLines != None and len(matrix) >= numLines:
            break

        matrix.append(line.rstrip().split("\t"))

        if len(matrix) % 100 == 0:
            print(len(matrix))

    return matrix

def writeMatrixToFile(x, filePath, writeMode='w'):
    outFile = open(filePath, writeMode)
    writeMatrixToOpenFile(x, outFile)
    outFile.close()

def writeMatrixToOpenFile(x, outFile):
    for y in x:
        outFile.write("\t".join([str(z) for z in y]) + "\n")

def transposeMatrix(x):
    transposed = zip(*x)

    for i in range(len(transposed)):
        transposed[i] = list(transposed[i])

    return transposed

# code copied from fslg_piccololab/code/TransposeData.py
# This code transposes tumorTPM and stores the transposed version in transposedTumorTPM
data = readMatrixFromFile(tumorTPM)

if len(data) > 1 and len(data[0]) == len(data[1]) - 1:
    data[0].insert(0, " ")

writeMatrixToFile(transposeMatrix(data), transposedTumorTPM)

# This code takes the new transposedTumorTPM and addes the PatientCancerType to the second column and writes it to the outFile data.tsv.gz
patientIDToCancerDict = {}
with open(PatientCancerType, 'r') as f:
    for line in f:
        print(line)
        lineList= line.strip('\n').split('\t')
        patientIDToCancerDict[lineList[0]] = lineList[1]

###I need to read this file and process it
data = readMatrixFromFile(metadata)

if len(data) > 1 and len(data[0]) == len(data[1]) - 1:
    data[0].insert(0, " ")

metadataDict = {}
first = True
for list in transposeMatrix(data) :
    if first :
        metadataDict["header"] = list[3:]
        first = False
    else :
        metadataDict[list[0]] = list[3:]

PatientIdToMutations = {}
with open(condensedMutationData, 'r') as f:
    f.readline()
    for line in f :
        print(line)
        lineList = line.strip('\n').split('\t')
        print(lineList) 
        try :
            PatientIdToMutations[lineList[1]].append(lineList[0])
        except KeyError :
            PatientIdToMutations[lineList[1]] = []
            PatientIdToMutations[lineList[1]].append(lineList[0])

with open(transposedTumorTPM, 'r') as iF:
    with open(dataOutFile, 'w') as ofData:
        with open(metadataOutFile, 'w') as ofMeta:
            firstLine = iF.readline().strip('\n').split('\t')
            ofMeta.write("Sample\tVariable\tValue\n")
            ofData.write("Sample\t" + '\t'.join(firstLine[1:]) + '\n')
            j = 0
            print("starting to write out")
            first = True
            for line in iF:
                j = j + 1
                if j % 1000 :
                    print("line " + str(j))

                lineList = line.strip('\n').split('\t')
                metaDataList = metadataDict[lineList[0]]
                #Pass over everything that is not BRCA
                if patientIDToCancerDict[lineList[0]] != "BRCA" : #We only want expression and metadata values associated with BRCA
                    continue

                patientId = '-'.join(lineList[0].split('-')[:4])
                #See if the specific BRCA patient is in the condensed file
                try : #check to see if the BRCA patient is in the condensed file
                    mutationList = PatientIdToMutations[patientId] 
                except KeyError :
                    print("patient Id not in condensed file: " + patientId)
                    continue

                ## Only BRCA patients in the condensed file should execute the following lines
                allNA = True 
                notAvailableMetaVariables = [] 
                for i in range(len(metaDataList)) :
                    if i == 66 :
                        continue
                    if(metaDataList[i] != "NA" and metaDataList[i] != "[Not Applicable]") : #excluding NA and [Not Applicable], but keeping [Not Available] unless they are the only values
                        if(metaDataList[i] != "[Not Available]") :
                            ofMeta.write(lineList[0][:15] + '\t' + metadataDict["header"][i] + '\t' + metaDataList[i] + '\n')
                            allNA = False
                        else :
                            #If all the values are [Not Available] we do not want to include them because we won't have any metavariables for the patient
                            notAvailableMetaVariables.append(i) 
                             
                if allNA == False :
                    for i in notAvailableMetaVariables : #Include the metavariables if not all of them are NA, [Not Applicable], and [Not Available]
                        ofMeta.write(lineList[0][:15] + '\t' + metadataDict["header"][i] + '\t' + metaDataList[i] + '\n')
                    for mutation in mutationList :
                        ofMeta.write(lineList[0][:15] + "\tSomatic mutation\t" + mutation + "\n")
                    ofData.write(lineList[0][:15] + "\t" + '\t'.join(lineList[1:]) + '\n')


