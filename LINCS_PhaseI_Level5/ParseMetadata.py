import h5py
import numpy as np
import sys, gzip

sigInfoFile = sys.argv[1]
cellInfo = sys.argv[2]
pertInfo = sys.argv[3]
pertMetrics = sys.argv[4]
sigMetrics = sys.argv[5]
metadataOut = sys.argv[6]

print("Reading metadata info")

cellHeaderList = []
cellInfoDict = {}
with gzip.open(cellInfo, 'r') as f :
    cellHeaderList = f.readline().decode().strip('\n').split('\t')[1:]
    for line in f :
        lineList = line.decode().strip('\n').split('\t')
        cellInfoDict[lineList[0]] = lineList[1:]

pertInfoHeaderList = []
pertInfoDict = {}
with gzip.open(pertInfo, 'r') as f :
    pertInfoHeaderList = f.readline().decode().strip('\n').split('\t')[3:]
    for line in f :
        lineList = line.decode().strip('\n').split('\t')
        pertInfoDict[lineList[0]] = lineList[3:]

pertMetricsHeaderList = []
pertMetricsDict = {}
with gzip.open(pertMetrics, 'r') as f:
    pertMetricsHeaderList = f.readline().decode().strip('\n').split('\t')[3:]
    for line in f :
        lineList = line.decode().strip('\n').split('\t')
        pertMetricsDict[lineList[0]] = lineList[3:]

sigMetricsHeaderList = []
sigMetricsDict = {}
with gzip.open(sigMetrics, 'r') as f :
    firstLineList = f.readline().decode().strip('\n').split('\t')
    sigMetricsHeaderList = firstLineList[4:]
    for line in f :
        lineList = line.decode().strip('\n').split('\t')
        sigMetricsDict[lineList[0]] = lineList[4:]

print("writing metadata file")
with gzip.open(metadataOut, 'w') as metaOut :
    with gzip.open(sigInfoFile, 'r') as sigInfo :
        headerList = sigInfo.readline().decode().strip('\n').split('\t')
        sigId = ""
        metaOut.write("Sample\tVariable\tValue\n".encode())
        indecis = 0
        for row in sigInfo :
            indecis = indecis + 1
            if indecis % 1000 == 0 :
                print(str(indecis) + " of 473647 molecular")
            rowList = row.decode().strip('\n').split('\t')[:11] ## don't select distil_id
            for i in range(len(rowList) - 1): ##This should not grab the first and last column
                if(str(rowList[i + 1]) != "-666") :
                    if headerList[i + 1] == "pert_time" or headerList[i + 1] == "pert_time_unit" :
                        continue
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
                            pertInfoIdList = pertInfoDict[rowList[1]] ##This will add the pertInfo metadata to the metadata.tsv.gz
                            for j in range(len(pertInfoIdList)) :
                                if(str(pertInfoIdList[j]) != "-666") :
                                    metaOut.write((str(rowList[0]) + '\t' + str(pertInfoHeaderList[j]) + '\t' + str(pertInfoIdList[j]) + '\n').encode())
                            pertMetricsIdList = pertMetricsDict[rowList[1]] ##This will add the pertMetrics metadata to the metadata.tsv.gz
                            for i in range(len(pertMetricsIdList)) :
                                if(str(pertMetricsIdList[i]) != "-666") :
                                    metaOut.write((str(rowList[0]) + '\t' + str(pertMetricsHeaderList[i]) + '\t' + str(pertMetricsIdList[i]) + '\n').encode())
                        except :
                            continue
