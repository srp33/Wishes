import h5py
import numpy as np
import sys, gzip

sigInfoFile = sys.argv[1]
cellInfo = sys.argv[2]
pertInfo = sys.argv[3]
sigMetrics = sys.argv[4]
metadataOut = sys.argv[5]

print("writing metadata file")

cellHeaderList = []
cellInfoDict = {}
f = gzip.open(cellInfo, 'r')
try :
    cellHeaderList = f.readline().decode().strip('\n').split('\t')[1:]
    for line in f :
        lineList = line.decode().strip('\n').split('\t')
        cellInfoDict[lineList[0]] = lineList[1:]
finally:
    f.close()

pertInfoHeaderList = []
pertInfoDict = {}
f = gzip.open(pertInfo, 'r')
try :
    pertInfoHeaderList = f.readline().decode().strip('\n').split('\t')[1:3]
    for line in f :
        lineList = line.decode().strip('\n').split('\t')
        pertInfoDict[lineList[0]] = lineList[1:3]
finally:
    f.close()

sigMetricsHeaderList = []
sigMetricsDict = {}
f = gzip.open(sigMetrics, 'r')
try:
    firstLineList = f.readline().decode().strip('\n').split('\t')
    sigMetricsHeaderList = firstLineList[2:4] + firstLineList[7:]
    for line in f:
        lineList = line.decode().strip('\n').split('\t')
        sigMetricsDict[lineList[1]] = lineList[2:4] + lineList[7:]
finally:
    f.close()

sigInfo =  gzip.open(sigInfoFile, 'r')
metaOut = gzip.open(metadataOut, 'w')
try:
    headerList = sigInfo.readline().decode().strip('\n').split('\t')
    sigId = "Sample"
    metaOut.write("Sample\tVariable\tValue\n".encode())
    for row in sigInfo :
        rowList = row.decode().strip('\n').split('\t')[:7]
        for i in range(len(rowList) - 1 ):
            if(str(rowList[i + 1]) != "-666") :
                metaOut.write((str(rowList[0]) + '\t' + str(headerList[i + 1]) + '\t' + str(rowList[i + 1]) + '\n').encode())

                if (rowList[0] != sigId) :
                    sigMetricsList = sigMetricsDict[rowList[0]] ##This will add the sigMetrics metadata to the metadata.tsv.gz
                    for j in range(len(sigMetricsList)) :
                        if(str(sigMetricsList[j]) != "-666") :
                            metaOut.write((str(rowList[0]) + '\t' + str(sigMetricsHeaderList[j]) + '\t' + str(sigMetricsList[j]) + '\n').encode())
                    sigId = rowList[0]

                if (headerList[i + 1] == "cell_id") :
                    try :
                        cellIdList = cellInfoDict[rowList[i + 1]] ##This will add the cellInfo to the metadata.tsv.gz
                        for j in range(len(cellIdList)) :
                            if(str(cellIdList[j]) != "-666") :
                                metaOut.write((str(rowList[0]) + '\t' + str(cellHeaderList[j]) + '\t' + str(cellIdList[j]) + '\n').encode())
                    except :
                        continue ## This catches SNUC4 that doesn't have any cellInfo, but is included in the sigInfo file
                elif (headerList[i + 1] == "pert_id") :
                    try :
                        pertInfoIdList = pertInfoDict[rowList[i + 1]] ##This will add the pertInfo metadata to the metadata.tsv.gz
                        for j in range(len(pertInfoIdList)) :
                            if(str(pertInfoIdList[j]) != "-666") :
                                metaOut.write((str(rowList[0]) + '\t' + str(pertInfoHeaderList[j]) + '\t' + str(pertInfoIdList[j]) + '\n').encode())
                    except :
                        continue
finally:
    sigInfo.close()
    metaOut.close()
