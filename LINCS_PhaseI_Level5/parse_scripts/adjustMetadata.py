import sys, gzip

metadataIn = sys.argv[1]
metadataOut = sys.argv[2]
cellInfo = sys.argv[3]
pertInfo = sys.argv[4]
pertMetrics = sys.argv[5]

cellHeaderList = []
cellInfoDict = {}
with gzip.open(cellInfo, 'r') as f:
    cellHeaderList = f.readline().strip('\n').split('\t')[1:]
    for line in f :
        lineList = line.strip('\n').split('\t') 
        cellInfoDict[lineList[0]] = lineList[1:]

pertInfoHeaderList = []
pertInfoDict = {}
with gzip.open(pertInfo, 'r') as f:
    pertInfoHeaderList = f.readline().strip('\n').split('\t')[3:]
    for line in f :
        lineList = line.strip('\n').split('\t')
        pertInfoDict[lineList[0]] = lineList[3:]

pertMetricsHeaderList = []
pertMetricsDict = {}
with gzip.open(pertMetrics, 'r') as f:
    pertMetricsHeaderList = f.readline().strip('\n').split('\t')[3:]
    for line in f :
        lineList = line.strip('\n').split('\t')
        pertMetricsDict[lineList[0]] = lineList[3:]

with gzip.open(metadataIn, 'r') as metaIn :
    with gzip.open(metadataOut, 'w') as metaOut :
        metaOut.write(metaIn.readline())
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
                pertInfoIdList = pertInfoDict[lineList[2]] ##This will add the pertInfo metadata to the metadata.tsv.gz
                for i in range(len(pertInfoIdList)) :
                    if(str(pertInfoIdList[i]) != "-666") :
                        metaOut.write(str(lineList[0]) + '\t' + str(pertInfoHeaderList[i]) + '\t' + str(pertInfoIdList[i]) + '\n')
                pertMetricsIdList = pertMetricsDict[lineList[2]] ##This will add the pertMetrics metadata to the metadata.tsv.gz 
                for i in range(len(pertMetricsIdList)) :
                    if(str(pertMetricsIdList[i]) != "-666") :
                        metaOut.write(str(lineList[0]) + '\t' + str(pertMetricsHeaderList[i]) + '\t' + str(pertMetricsIdList[i]) + '\n')
