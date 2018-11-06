import sys, gzip
import numpy as np
from io import StringIO

inFilePath = sys.argv[1]
outFilePath = sys.argv[2]

def standardizeMissingValues(values):
    standardized = []
    for value in values:
        if value in ["[Not Applicable]", "[Not Available]"]:
            standardized.append("NA")
        else:
            standardized.append(value)

    return standardized

def shouldKeepColumn(values):
    numNonMissing = [value for value in values if value != "NA"]
    return len(numNonMissing) > 0

with gzip.open(inFilePath, 'r') as inFile:
    with gzip.open(outFilePath, 'a') as outFile:
        headerList = inFile.readline().decode().rstrip("\n").split("\t")
        sampleIDs = headerList[3:]

        for line in inFile:
            lineList = line.decode().rstrip("\n").split("\t")
            variableName = lineList[0]
            values = standardizeMissingValues(lineList[3:])

            if not shouldKeepColumn(values):
                continue

            for i in range(len(sampleIDs)):
                sampleID = sampleIDs[i][:15]
                value = values[i]

                outFile.write("{}\t{}\t{}\n".format(sampleID, variableName, value).encode())

###### This is old code that we may or may not need for working around encoding issues.
#                metaDataList = metadataDict[lineList[0].encode('US-ASCII')]
#
#                try :
#                    writeMetaData(ofMeta, metaDataList, 'US-ASCII')
#                except UnicodeDecodeError : ## Using US-ASCII is much quicker, but it cannot convert all types, so I have encorporated this second fassion.
#                    writeMetaData(ofMeta, metaDataList, 'UTF-8')
