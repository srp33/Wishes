import sys, gzip
import numpy as np
from io import StringIO

metadata = sys.argv[1]
PatientCancerType = sys.argv[2]
tumorFeatureCounts = sys.argv[3]
dataOutFile = sys.argv[4]
metadataOutFile = sys.argv[5]
namesToAbbreviations = sys.argv[6]

def writeMetaData(ofMeta, metaDataList, code) :
    allNA = True
    notAvailableMetaVariables = []

    for i in range(len(metaDataList)) :
        metaValue = metaDataList[i].decode(code)

        if metaValue not in ["[Not Applicable]", "[Not Available]", "NA"]:
            ofMeta.write((lineList[0]  + '\t' + metadataDict["header"][i].decode(code) + '\t' + metaValue + '\n').encode())
            allNA = False
        else:
            #If all the values are [Not Available] we do not want to include them because we won't have any metavariables for the patient
            notAvailableMetaVariables.append(i)

    if allNA  == False :
        for i in notAvailableMetaVariables : #Include the metavariables if not all of them are NA, [Not Applicable], and [Not Available]
            ofMeta.write((lineList[0]  + '\t' + metadataDict["header"][i].decode(code)  + '\t' + "NA" + '\n').encode())


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

#store metainfo
metadataDict = {}
with gzip.open(metadata, 'r') as f :
    data = np.genfromtxt(metadata,delimiter='\t',dtype='S50')
    metadataDict["header"] = data.T[0,3:]
    for line in data.T[1:,:] :
        metadataDict[line[0]] = line[3:]

#read Tumor expression info and print out files
with gzip.open(tumorFeatureCounts, 'r') as iF:
    with gzip.open(dataOutFile, 'w') as ofData:
        with gzip.open(metadataOutFile, 'w') as ofMeta:
            data = np.genfromtxt(iF,delimiter='\t',dtype=str)
            firstLine = data.T[0,:].astype(str)
            ofMeta.write(("Sample\tVariable\tValue\n").encode())
            ofData.write(("Sample\t" + '\t'.join(firstLine[1:]) + '\n').encode())
            j = 0
            for lineList in data.T[1:,:]:
                j += 1
                if j % 50 == 0 :
                    print(str(j) + " of 9267")
                ofMeta.write((lineList[0] + "\tCancer_Type\t" + abbvToNamesDict[patientIDToCancerDict[lineList[0]]] + "\n").encode())
                metaDataList = metadataDict[lineList[0].encode('US-ASCII')]

                try :
                    writeMetaData(ofMeta, metaDataList, 'US-ASCII')
                except UnicodeDecodeError : ## Using US-ASCII is much quicker, but it cannot convert all types, so I have encorporated this second fassion.
                    writeMetaData(ofMeta, metaDataList, 'UTF-8')

                ofData.write(('\t'.join(lineList) + '\n').encode())
