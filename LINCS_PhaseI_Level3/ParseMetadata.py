import numpy as np
import sys, gzip
import time

sigInfoFile = sys.argv[1]
cellInfo = sys.argv[2]
pertInfo = sys.argv[3]
pertMetrics = sys.argv[4]
metadataOut = sys.argv[5]

def readIntoDict(filePath, keyColumn, ignoreColumns):
    infoDict = {}
    with gzip.open(filePath) as f:
        headerList = f.readline().decode().rstrip('\n').split('\t')
        keyIndex = headerList.index(keyColumn)
        headerIndices = [i for i in range(len(headerList)) if headerList[i] not in ignoreColumns]

        for line in f:
            lineList = line.decode().rstrip('\n').split('\t')
            sample = lineList[keyIndex]

            infoDict[sample] = {}

            for i in headerIndices:
                variable = headerList[i]
                value = checkMissing(lineList[i])

                infoDict[sample][variable] = value

    return infoDict

def checkMissing(value):
    if value in ("-666.0", "-666"):
        value = "NA"

    return value

cellInfoDict = readIntoDict(cellInfo, "cell_id", [])
pertInfoDict = readIntoDict(pertInfo, "pert_id", ["pert_iname", "pert_type"])
pertMetricsDict = readIntoDict(pertInfo, "pert_id", ["pert_iname", "pert_type"])

with gzip.open(sigInfoFile, 'r') as sigInfo:
    with open(metadataOut, 'w', encoding="utf-8") as metaOut:
        headerList = sigInfo.readline().decode().rstrip('\n').split('\t')

        metaOut.write("Sample\tVariable\tValue\n")
        index = 0
        for row in sigInfo:
            rowList = row.decode().strip('\n').split('\t')

            index = index + 1
            if index % 1000 == 0:
                print(str(index) + " of metadata")
                sys.stdout.flush()

            sample = rowList[0]
            sampleDict = {}

            for i in range(1, len(rowList)):
                variable = headerList[i]
                value = checkMissing(rowList[i])

                if variable == "cell_id":
                    if value in cellInfoDict: # At least one cell line is not in the cell_info file
                        sampleDict.update(cellInfoDict[value])

                    sampleDict[variable] = value

                elif variable == "pert_id":
                    if value in pertInfoDict:
                        sampleDict.update(pertInfoDict[value])
                    if value in pertMetricsDict:
                        sampleDict.update(pertMetricsDict[value])

                    sampleDict[variable] = value

                else:
                    sampleDict[variable] = value

            for variable, value in sampleDict.items():
                metaOut.write("{}\t{}\t{}\n".format(sample, variable, value))
