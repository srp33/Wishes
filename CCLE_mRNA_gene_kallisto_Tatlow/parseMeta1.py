import sys, gzip

inFilePath = sys.argv[1] #"expression_main.txt"    
outFilePath = sys.argv[2] #"data.txt" 

sampleIndexes = {} #Create a dictionary linking cell line names with given index
geneValues = {} #Will link cell lines to a dictionary linking symbol with it's value

uniqueCells = []

#Get a collection of each unique sample and gene in the dataset
with open(inFilePath, 'r') as inFile:
	inHeaderItems = inFile.readline().rstrip("\n").split("\t")

	symbolIndex = inHeaderItems.index("SYMBOL")
	
	numOfIndices = len(inHeaderItems)

	cellLineIndex = inHeaderItems.index("LOUNH91_LUNG")
	
	for x in range(cellLineIndex, (numOfIndices-1)):
		cellType = inHeaderItems[x]
		sampleIndexes[cellType] = x
		uniqueCells.append(cellType)

	for cell in sampleIndexes:
		geneValues[cell] = {}
	
	for line in inFile:
		lineData = line.rstrip("\n").split("\t")
		for key in sampleIndexes:
			geneValues[key][lineData[symbolIndex]] = lineData[sampleIndexes[key]]

uniqueCells = sorted(list(uniqueCells))

# Create output file
with open(outFilePath, 'a') as outFile:
	for cell in uniqueCells:
		for key in geneValues[cell]:
			outText = "\t".join([cell,key,geneValues[cell][key]]) + "\n"
			outFile.write(outText)
