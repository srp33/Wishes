import sys, gzip

metadata = sys.argv[1]
PatientCancerType = sys.argv[2]
tumorFeatureCounts = sys.argv[3]
transposedTumorFeatureCounts = sys.argv[4]
dataOutFile = sys.argv[5]
metadataOutFile = sys.argv[6]

# functions copied from fslg_piccololab/code/utilities.py
def readMatrixFromFile(filePath, numLines=None):
    matrix = []
    for line in file(filePath, 'rU'):
        if numLines != None and len(matrix) >= numLines:
            break

        matrix.append(line.rstrip().split("\t"))

        if len(matrix) % 100000 == 0:
            print len(matrix)

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
# This code transposes NormalTPM and stores the transposed version in transposedNormalTPM
data = readMatrixFromFile(tumorFeatureCounts)

if len(data) > 1 and len(data[0]) == len(data[1]) - 1:
    data[0].insert(0, " ")

writeMatrixToFile(transposeMatrix(data), transposedTumorFeatureCounts)

# This code takes the new transposedNormalTPM and addes the PatientCancerType to the second column and writes it to the outFile data.tsv.gz
patientIDToCancerDict = {}
with open(PatientCancerType, 'r') as f:
    for line in f:
        lineList= line.strip('\n').split('\t')
        patientIDToCancerDict[lineList[0]] = lineList[1]

###I need to read this file and process it
data = readMatrixFromFile(metadata)

if len(data) > 1 and len(data[0]) == len(data[1]) - 1:
    data[0].insert(0, " ")

#writeMatrixToFile(transposeMatrix(data), transposedMetadata)

metadataDict = {}
first = True
for list in transposeMatrix(data) :
    if first :
        metadataDict["header"] = list[3:]
        first = False
    else :
        metadataDict[list[0]] = list[3:]

with open(transposedTumorFeatureCounts, 'r') as iF:
    with open(dataOutFile, 'w') as ofData:
        with open(metadataOutFile, 'w') as ofMeta:
            firstLine = iF.readline().strip('\n').split('\t')
            ofMeta.write("SampleID\tVariable\tValue\n")
            ofData.write("SampleID\t" + '\t'.join(firstLine[1:]) + '\n')
            for line in iF:
                lineList = line.strip('\n').split('\t')
                ofMeta.write(lineList[0] + "\tCancer_Type\t" + patientIDToCancerDict[lineList[0]] + "\n")
                metaDataList = metadataDict[lineList[0]]
                for i in range(len(metaDataList)) :
                    if(metaDataList[i] != "NA") :
                        ofMeta.write(lineList[0] + '\t' + metadataDict["header"][i] + '\t' + metaDataList[i] + '\n')
                ofData.write('\t'.join(lineList) + '\n')
