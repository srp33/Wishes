import sys, gzip
import numpy as np

dataFilePath = sys.argv[1]
outFilePath = sys.argv[2]

#Create array and transpose 
data = []
if dataFilePath[-2:] == "gz":
    with gzip.open(dataFilePath, 'r') as f:
        for line in f:
            lineItems = line.decode().rstrip("\n").split("\t")
            data.append(lineItems)
    npArray = np.array(data)
    npArray = npArray.T
    firstLine = True
    with gzip.open(outFilePath, 'w') as outFile:
        for line in npArray:
            if firstLine:
                line[0] = 'Sample'
                firstLine = False
            outFile.write(("\t".join(line) + '\n').encode())
                                                                                        
else:
    with open(dataFilePath, 'r') as f:
        for line in f:
            lineItems = line.rstrip("\n").split("\t")
            data.append(lineItems)
    npArray = np.array(data)
    npArray = npArray.T

    firstLine = True
    with gzip.open(outFilePath, 'w') as outFile:
        for line in npArray:
            if firstLine:
                line[0] = 'Sample'
                firstLine = False
            outFile.write(("\t".join(line) + '\n').encode())

