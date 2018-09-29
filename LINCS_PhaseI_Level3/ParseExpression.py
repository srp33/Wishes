import h5py
import numpy as np
import sys, gzip

gctxFileName = sys.argv[1]
geneFile = sys.argv[2]
dataOut = sys.argv[3]

#np.savetxt(dataOut, h5py.File(gctxFileName)['/0/DATA/0/matrix'], '%g', '\t')

f = h5py.File(gctxFileName, "r")

grpname = f.require_group('/0')
subgrpMeta = grpname.require_group('/0/META')
colgrp = subgrpMeta.require_group('/0/META/ROW')
rowgrp = subgrpMeta.require_group('/0/META/COL')
subgrpData = grpname.require_group('/0/DATA')
subsubgrpData = subgrpData.require_group('/0/DATA/0')

geneDict = {}
with gzip.open(geneFile, 'r') as f :
    headerLine = f.readline().decode()

    for line in f :
        list = line.decode().strip('\n').split('\t')
        geneDict[list[0]] = list[1]

print("Writing expression file")
f = open(dataOut, 'w')

try :
    f.write("Sample")
    for value in colgrp["id"] :
        f.write('\t' + geneDict[str(int(value))])
    f.write('\n')

    index = 0
    for line in subsubgrpData["matrix"]:
        a = np.asarray(line).astype(str)
        sample = rowgrp["id"][index].decode()

        f.write(sample + '\t' + '\t'.join(a) + '\n')
        index = index + 1

        if index % 1000 == 0 :
            print(str(index) + " expression rows")
            break

finally :
    f.close()
