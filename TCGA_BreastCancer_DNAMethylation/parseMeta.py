import sys, gzip

PatientCancerType = sys.argv[1]
outFilePath = sys.argv[2]

#Read in Patient Cancer Types (Sample ID's and Values)
patientIDToCancerDict = {}
with open(PatientCancerType, 'r') as f:
	for line in f:
		lineList= line.strip('\n').split('\t')
		patientIDToCancerDict[lineList[0]] = lineList[1]

# Create output file
with open(outFilePath, 'w') as outFile:
	outText = "\t".join(["Sample","Variable","Value"]) + "\n"
	outFile.write(outText)

	for cancerType in patientIDToCancerDict:
		mutation = patientIDToCancerDict[cancerType]
		outFile.write(cancerType[:15] + "\tSomatic mutation\t" + mutation + "\n")
