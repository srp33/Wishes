import sys, gzip

metadataIn = sys.argv[1]
metadataOut = sys.argv[2]
cellInfo = sys.argv[3]
pertInfo = sys.argv[4]

cellHeaderList = []
cellInfoDict = {}
f = gzip.open(cellInfo, 'r')
try :
    cellHeaderList = f.readline().strip('\n').split('\t')[1:]
    for line in f :
        lineList = line.strip('\n').split('\t') 
        cellInfoDict[lineList[0]] = lineList[1:]
finally:
    f.close()

pertInfoHeaderList = []
pertInfoDict = {}
f = gzip.open(pertInfo, 'r')
try :
    pertInfoHeaderList = f.readline().strip('\n').split('\t')[1:3]
    for line in f :
        lineList = line.strip('\n').split('\t')
        pertInfoDict[lineList[0]] = lineList[1:3]
finally:
    f.close()

metaIn =  gzip.open(metadataIn, 'r')
metaOut = gzip.open(metadataOut, 'w')
try:
    metaOut.write(metaIn.readline())
    sigId = ""
    for line in metaIn :
        metaOut.write(line)
        lineList = line.strip('\n').split('\t')
        if (lineList[1] == "cell_id") :
            try :
                cellIdList = cellInfoDict[lineList[2]] ##This will add the cellInfo to the metadata.tsv.gz
                for i in range(len(cellIdList)) :
                    if(str(cellIdList[i]) != "-666") :
                        metaOut.write(str(lineList[0]) + '\t' + str(cellHeaderList[i]) + '\t' + str(cellIdList[i]) + '\n')
            except :
                continue ## This catches SNUC4 that doesn't have any cellInfo, but is included in the sigInfo file
        elif (lineList[1] == "pert_id") :
            try :
                pertInfoIdList = pertInfoDict[lineList[2]] ##This will add the pertInfo metadata to the metadata.tsv.gz
                for i in range(len(pertInfoIdList)) :
                    if(str(pertInfoIdList[i]) != "-666") :
                        metaOut.write(str(lineList[0]) + '\t' + str(pertInfoHeaderList[i]) + '\t' + str(pertInfoIdList[i]) + '\n')
            except :
                continue
finally:
    metaIn.close()
    metaOut.close()
