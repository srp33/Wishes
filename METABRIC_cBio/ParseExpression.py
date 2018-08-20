import sys, gzip

inFilePath = sys.argv[1]
outFilePath = sys.argv[2];

uniqueSampleIDs = set()
uniqueGeneIDs = set()
#the line below is for opening zipped files, for now we just use basic file.open()
# with gzip.open(inFilePath, 'rb') as inFile:
inFile = open(inFilePath,"r")
inHeaderItems = inFile.readline().rstrip("\n").split("\t")

print("Sorting sample IDs")
#make a set of all sample ids, which start at index 2
for i in range(2, len(inHeaderItems)):
	uniqueSampleIDs.add(inHeaderItems[i])
uniqueSampleIDs = sorted(list(uniqueSampleIDs))


print("Sorting Gene IDs")
#extract gene symbol
for line in inFile:
	uniqueGeneIDs.add(line.rstrip("\n").split("\t")[0])
uniqueGeneIDs = sorted(list(uniqueGeneIDs))
del uniqueGeneIDs[0]

#Initialize a dictionary that will store data values
#dataDict will be sampleID: dictionary{gene: value}
print("Initializing data dictionary")
dataDict = {}
for sampleID in uniqueSampleIDs:
	dataDict[sampleID] = {}

inFile.close()
inFile = open(inFilePath,"r")
inFile.readline()

#Populate the dictionary, iterating through every row for each column
print("Populating dictionary")
for line in inFile:
	lineItems=line.rstrip("\n").split("\t")
	geneID = lineItems[0]

	for col in range(2, len(inHeaderItems)):
		dataDict[inHeaderItems[col]][geneID]=lineItems[col]

#print(len(dataDict[uniqueSampleIDs[2]]))
#print("A1CF" in dataDict[uniqueSampleIDs[2]].keys())
#print(inHeaderItems[2])
#write everything to a file
#outFile=open(outFilePath, "w")
with gzip.open(outFilePath,'wb') as outFile:
	outText = "\t".join(["Sample"] + uniqueGeneIDs) + "\n"
	outFile.write(outText.encode())
#print(dataDict[uniqueSampleIDs[0]]["A1CF"]) #error: not finding keys in second dictionary
#print(len(dataDict["MB-4313"]))
#print(dataDict["MB-4313"]["1-Mar"])
#print(dataDict["MB-4313"]["1-Sep"])
#print(dataDict["MB-4313"]["10-Mar"])
	print("Writing to file")
	for sampleID in uniqueSampleIDs:
		dataItems = [dataDict[sampleID][geneID] for geneID in uniqueGeneIDs]
		outText = "\t".join([sampleID] + dataItems) + "\n"
		outFile.write(outText.encode())
inFile.close()
#outFile.close()
