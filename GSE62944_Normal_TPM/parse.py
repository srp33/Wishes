import sys, gzip

PatientCancerType = sys.argv[1]
NormalTPM = sys.argv[2]
transposedNormalTPM = sys.argv[3]
dataOutFile = sys.argv[4]
metadataOutFile = sys.argv[5]

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
data = readMatrixFromFile(NormalTPM)

if len(data) > 1 and len(data[0]) == len(data[1]) - 1:
    data[0].insert(0, " ")

writeMatrixToFile(transposeMatrix(data), transposedNormalTPM)

# This code takes the new transposedNormalTPM and addes the PatientCancerType to the second column and writes it to the outFile data.tsv.gz
patientIDToCancerDict = {}
with open(PatientCancerType, 'r') as f:
    for line in f:
        lineList= line.strip('\n').split('\t')
        patientIDToCancerDict[lineList[0]] = lineList[1]

with open(transposedNormalTPM, 'r') as iF:
    with open(dataOutFile, 'w') as ofData:
        with open(metadataOutFile, 'w') as ofMeta:
            firstLine = iF.readline().strip('\n').split('\t')
            ofMeta.write("SampleID\tVariable\tValue\n")
            ofData.write("SampleID\t" + '\t'.join(firstLine[1:]) + '\n')
            for line in iF:
                lineList = line.strip('\n').split('\t')
                ofMeta.write(lineList[0] + "\tCancer_Type\t" + patientIDToCancerDict[lineList[0]] + "\n")
                ofData.write('\t'.join(lineList) + '\n')
