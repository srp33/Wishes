import h5py
import numpy as np
import sys, gzip

gctxFileName = sys.argv[1]
geneFile = sys.argv[2]
dataOut = sys.argv[3]

geneDict = {}
with gzip.open(geneFile, 'r') as f :
    headerLine = f.readline().decode()

    for line in f :
        list = line.decode().strip('\n').split('\t')
        geneDict[list[0]] = list[1]

f = h5py.File(gctxFileName, "r")

grpname = f.require_group('/0')

subgrpMeta = grpname.require_group('/0/META')
colgrp = subgrpMeta.require_group('/0/META/ROW')
rowgrp = subgrpMeta.require_group('/0/META/COL')

subgrpData = grpname.require_group('/0/DATA')
subsubgrpData = subgrpData.require_group('/0/DATA/0')

print("Writing expression file")

f = gzip.open(dataOut, 'w')
try :
    f.write("Sample".encode())
    for value in colgrp["id"] :
        f.write(('\t' + geneDict[value.decode()]).encode())
    f.write('\n'.encode())

    index = 0
    for line in subsubgrpData["matrix"] :
        sample = rowgrp["id"][index].decode()
        values = [str(x) for x in line.tolist()]

        f.write((sample + '\t' + '\t'.join(values) + '\n').encode())

        index = index + 1
#        if index == 10:
#            break
        if index % 1000 == 0:
            print(str(index) + " of 345976 expression data")
            sys.stdout.flush()
finally :
    f.close()
