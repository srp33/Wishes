import h5py
import numpy as np
import sys, gzip

instInfoFile = sys.argv[1]
gctxFileName = sys.argv[2]
metadataOut = sys.argv[3]
dataOut = sys.argv[4]
geneFile = sys.argv[5]
cellInfo = sys.argv[6]
pertInfo = sys.argv[7]
pertMetrics = sys.argv[8]

f = h5py.File(gctxFileName, "r")


grpname = f.require_group('/0')

subgrpMeta = grpname.require_group('/0/META')
colgrp = subgrpMeta.require_group('/0/META/ROW')
rowgrp = subgrpMeta.require_group('/0/META/COL')

subgrpData = grpname.require_group('/0/DATA')
subsubgrpData = subgrpData.require_group('/0/DATA/0')
print(subsubgrpData.items())

geneDict = {}
with gzip.open(geneFile, 'r') as f :
    headerLine = f.readline()

    for line in f :
        list = line.strip('\n').split('\t')
        geneDict[list[0]] = list[1]


print("reading source files")

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
    pertInfoHeaderList = f.readline().strip('\n').split('\t')[3:]
    for line in f :
        lineList = line.strip('\n').split('\t')
        pertInfoDict[lineList[0]] = lineList[3:]
finally:
    f.close()

pertMetricsHeaderList = []
pertMetricsDict = {}
with gzip.open(pertMetrics, 'r') as f:
    pertMetricsHeaderList = f.readline().strip('\n').split('\t')[3:]
    for line in f :
        lineList = line.strip('\n').split('\t')
        pertMetricsDict[lineList[0]] = lineList[3:]


instInfo =  gzip.open(instInfoFile, 'r')
metaOut = gzip.open(metadataOut, 'w')
instInfoSampleIds = []
#for row in instInfo :
#        rowList = row.strip('\n').split('\t')
#        instInfoSampleIds.append(rowList[0])
#instInfo.close()
#intersectionValues = np.intersect1d(instInfoSampleIds,rowgrp["id"])
#print("it worked")
print("writing metadata file")
try:
    headerList = instInfo.readline().strip('\n').split('\t')
    sigId = ""
    metaOut.write("Sample\tVariable\tValue\n")
    for row in instInfo :
        rowList = row.strip('\n').split('\t')
	if(np.any(rowgrp["id"][:,] ==  rowList[0])) :
            print("matched")
#            didItWork = np.where(rowgrp["id"]==rowList[0])
            instInfoSampleIds.append(rowList[0])
            print(rowList[0])        
            for i in range(len(rowList) - 1 ):
                if(str(rowList[i + 1]) != "-666") and (str(rowList[i + 1]) != "-666.0") :
                    metaOut.write(str(rowList[0]) + '\t' + str(headerList[i + 1]) + '\t' + str(rowList[i + 1]) + '\n')
                
                if (headerList[i + 1] == "cell_id") :
                    try :
                        cellIdList = cellInfoDict[rowList[i + 1]] ##This will add the cellInfo to the metadata.tsv.gz
                        for j in range(len(cellIdList)) :
                            if(str(cellIdList[j]) != "-666") :
                                metaOut.write(str(rowList[0]) + '\t' + str(cellHeaderList[j]) + '\t' + str(cellIdList[j]) + '\n')
                    except :
                        continue ## This catches SNUC4 that doesn't have any cellInfo, but is included in the sigInfo file
                elif (headerList[i + 1]  == "pert_id") :
                    try :
                        pertInfoIdList = pertInfoDict[rowList[i + 1]] ##This will add the pertInfo metadata to the metadata.tsv.gz
                        for j in range(len(pertInfoIdList)) :
                            if(str(pertInfoIdList[j]) != "-666") :
                                metaOut.write(str(rowList[0]) + '\t' + str(pertInfoHeaderList[j]) + '\t' + str(pertInfoIdList[j]) + '\n')
                        pertMetricsIdList = pertMetricsDict[rowList[i + 1]] ##This will add the pertMetrics metadata to the metadata.tsv.gz 
                        for j in range(len(pertMetricsIdList)) :
                            if(str(pertMetricsIdList[j]) != "-666") :
                                metaOut.write(str(rowList[0]) + '\t' + str(pertMetricsHeaderList[j]) + '\t' + str(pertMetricsIdList[j]) + '\n')
                    except :
                        continue
        else :
#        except :
            print("metadata lines didn't match")
            continue
finally:
    instInfo.close()
    metaOut.close()

print("writing expression file")

instInfoSampleIds = np.asarray(instInfoSampleIds)

f = gzip.open(dataOut, 'w')
try :
    f.write("Sample")
    for value in colgrp["id"] :
        f.write('\t' + geneDict[str(value)])
    f.write('\n')

    index = 0
    for line in subsubgrpData["matrix"] :
        a = np.asarray(line).astype(str)
#            didItWork = np.where(intersectionValues==rowgrp["id"][index])
	if(np.any(instInfoSampleIds[:,0] == rowgrp["id"][index])) :
#        if(np.any(instInfoSampleIds[:,0] == rowgrp["id"][index])) :
#            didItWork = np.where(instInfoSampleIds==rowgrp["id"][index])
            f.write(rowgrp["id"][index] + '\t' + '\t'.join(a) + '\n')
            index = index + 1
            print(str(index) + " of ")
        else :
            index = index + 1
            print("didn't match " + rowgrp["id"][index])
            continue
finally :
    f.close()
