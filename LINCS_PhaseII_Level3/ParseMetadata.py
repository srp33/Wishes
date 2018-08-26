import numpy as np
import sys, gzip

instInfoFile = sys.argv[1]
cellInfo = sys.argv[2]
pertInfo = sys.argv[3]
metadataOut = sys.argv[4]

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

instInfo =  gzip.open(instInfoFile, 'r')
metaOut = gzip.open(metadataOut, 'w')
try:
    headerList = instInfo.readline().decode().strip('\n').split('\t')
    sigId = ""
    metaOut.write("Sample\tVariable\tValue\n".encode())
    indeci = 0
    for row in instInfo :
        indeci = indeci + 1
        print(str(indeci) + " of 345976 molecular data")
        rowList = row.decode().strip('\n').split('\t')
        for i in range(len(rowList) - 1 ):
            if(str(rowList[i + 1]) != "-666") and (str(rowList[i + 1]) != "-666.0") :
                if(str(headerList[i + 1]) == "pert_time") :
                    metaOut.write((str(rowList[0]) + '\t' + str(headerList[i + 1]) + '\t' + str(rowList[i + 1]) + " " + str(rowList[i + 2]) + '\n').encode())
                    break
                metaOut.write((str(rowList[0]) + '\t' + str(headerList[i + 1]) + '\t' + str(rowList[i + 1]) + '\n').encode())

            if (headerList[i + 1] == "cell_id") :
                try :
                    cellIdList = cellInfoDict[rowList[i + 1]] ##This will add the cellInfo to the metadata.tsv.gz
                    for j in range(len(cellIdList)) :
                        if(str(cellIdList[j]) != "-666") :
                            metaOut.write((str(rowList[0]) + '\t' + str(cellHeaderList[j]) + '\t' + str(cellIdList[j]) + '\n').encode())
                except :
                    continue ## This catches SNUC4 that doesn't have any cellInfo, but is included in the sigInfo file
            elif (headerList[i + 1]  == "pert_id") :
                try :
                    pertInfoIdList = pertInfoDict[rowList[i + 1]] ##This will add the pertInfo metadata to the metadata.tsv.gz
                    for j in range(len(pertInfoIdList)) :
                        if(str(pertInfoIdList[j]) != "-666") :
                            metaOut.write((str(rowList[0]) + '\t' + str(pertInfoHeaderList[j]) + '\t' + str(pertInfoIdList[j]) + '\n').encode())
                except :
                    continue
finally:
    instInfo.close()
    metaOut.close()
