import sys, gzip
import numpy as np

PatientCancerType = sys.argv[1]
NormalTPM = sys.argv[2]
dataOutFile = sys.argv[3]
metadataOutFile = sys.argv[4]
print(metadataOutFile)
namesToAbbreviations = sys.argv[5]

## Read the namesToAbbreviation
abbvToNamesDict = {}
with open(namesToAbbreviations, 'r') as f:
    f.readline()
    for line in f :
        lineList = line.strip('\n').split('\t')
        abbvToNamesDict[lineList[2]] = lineList[1]

# This code takes the new transposedNormalTPM and addes the PatientCancerType to the second column and writes it to the outFile data.tsv.gz
patientIDToCancerDict = {}
with gzip.open(PatientCancerType, 'r') as f:
    for line in f:
        lineList= line.decode().strip('\n').split('\t')
        patientIDToCancerDict[lineList[0]] = lineList[1]

with gzip.open(NormalTPM, 'r') as iF:
    data = np.genfromtxt(iF,delimiter='\t',dtype=str)
    with gzip.open(dataOutFile, 'w') as ofData:
        with gzip.open(metadataOutFile, 'w') as ofMeta:
            firstLine = data.T[0,:]
            ofMeta.write(("Sample\tVariable\tValue\n").encode())
            ofData.write(("Sample\t" + '\t'.join(firstLine[1:]) + '\n').encode())
            for lineList in data.T[1:,:]:
                ofMeta.write((lineList[0] + "\tCancer_Type\t" + abbvToNamesDict[patientIDToCancerDict[lineList[0]]] + "\n").encode())
                ofData.write(('\t'.join(lineList) + '\n').encode())
