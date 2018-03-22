import sys, gzip
import numpy as np
from numpy import genfromtxt, savetxt

CNVdata = sys.argv[1]
outFilePath = sys.argv[2]

#Create array and transpose 
data = []

with open(CNVdata, 'r') as f:
	for line in f:
		lineItems = line.rstrip("\n").split("\t")
		data.append(lineItems)
npArray = np.array(data)
npArray = npArray.T

firstLine = True
with open(outFilePath, 'w') as outFile:
	for line in npArray:
		if firstLine:
			line[0] = 'Sample'
			firstLine = False
		outFile.write("\t".join(line) + '\n')

