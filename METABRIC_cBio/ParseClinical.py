import sys, gzip

clinical_sample_filePath = sys.argv[1]
clinical_patient_filePath=sys.argv[2]
cna_filePath=sys.argv[3]
mutations_extended_filePath=sys.argv[4]
outFilePath = sys.argv[5]

#Function used to interpret data_CNA.txt values
def geneAlterationTranslator(int):
	if int== '-2':
		return "Homozygous deletion"
	if int=='-1':
		return "Heterozygous deletion"
	if int =='1':
		return "Low-level amplification"
	if int=='2':
		return "High-level amplification"
	return 0;

#Ignore first 4 lines (comments)
clinicalPatientFile = open(clinical_patient_filePath, "r")
clinicalPatientFile.readline()
clinicalPatientFile.readline()
clinicalPatientFile.readline()
clinicalPatientFile.readline()

print("Processing data_clinical_patient")
#Start with data_clinical_patient, extract ALL metadata for each patient
metaheaders = clinicalPatientFile.readline().rstrip("\n").split("\t")
clinicalDict = {} #this will store metadata for data_clinical_patient.txt and data_clinical_sample.txt at least

#each patient-key corresponds to a dictionary of metadata-value pairs
for line in clinicalPatientFile:
	line=line.rstrip("\n").split("\t")
	clinicalDict[line[0]]={}
	for header in range(1, len(metaheaders)):
		clinicalDict[line[0]][metaheaders[header]]=line[header]
clinicalPatientFile.close()
#print(clinicalDict["MB-0002"]["VITAL_STATUS"])

#Same process, but for data_clinical_sample, add them to the dictionary
print("Processing data_clinical_sample")
clinicalSampleFile=open(clinical_sample_filePath, "r")
clinicalSampleFile.readline()
clinicalSampleFile.readline()
clinicalSampleFile.readline()
clinicalSampleFile.readline()
metaheaders2 = clinicalSampleFile.readline().rstrip("\n").split("\t")
for line in clinicalSampleFile:
	line=line.rstrip("\n").split("\t")
	sample=line[0]
	if sample not in clinicalDict:
		clinicalDict[sample]={}	
	for header in range(2, len(metaheaders2)):
		clinicalDict[sample][metaheaders2[header]]=line[header]
clinicalSampleFile.close()
#print(clinicalDict["MB-0002"]["SAMPLE_TYPE"])
#print(clinicalDict["MB-0002"]["VITAL_STATUS"])

#Process data_CNA.txt
print("Processing data_CNA")
cnaFile = open(cna_filePath,"r")
cnaHeaders = cnaFile.readline().rstrip("\n").split("\t")
del cnaHeaders[1]
cnaDict = {}
for sample in range(1, len(cnaHeaders)):
	cnaDict[cnaHeaders[sample]]  = {}

for line in cnaFile:
	line=line.rstrip("\n").split("\t")
	del line[1]
	metaGene= "CNA__"+line[0]
	for word in range(1, len(line)):
#		if line[word]!='0' and line[word]!=0:
		if geneAlterationTranslator(line[word]) != 0:
			cnaDict[cnaHeaders[word]][metaGene]= geneAlterationTranslator(line[word])
#print(cnaDict["MB-0008"])
#print(len(cnaDict["MB-0000"]))
#print(cnaDict["MB-0045"]["CNA__A1BG"])	
print("Processing data_mutations_extended")
mutationsFile = open(mutations_extended_filePath, "r")
mutationsFile.readline();
headers = mutationsFile.readline().rstrip("\n").split("\t")
headers[39]="Protein_Variant"

variantDict = {}

#Protein Dict: Key=sample id, value is dictionary with key=gene, value is list of protein variants
proteinDict={}
sample = ""
variant = ""
for line in mutationsFile:
	line = line.rstrip("\n").split("\t")
	gene = line[0]
	#this code gets all Variant_Classification info
	if not line[16] in variantDict:
		variantDict[line[16]]={}
	if not gene in variantDict[line[16]]:
		variantDict[line[16]][gene]=set()
	variantDict[line[16]][gene].add(line[9])
	
	#this code gets all Protein_Variant info
	if not line[16] in proteinDict:
		proteinDict[line[16]]={}
	if not gene in proteinDict[line[16]]:
		proteinDict[line[16]][gene] = []
	proteinDict[line[16]][gene].append(line[39])
	#End Protein_Variant code

	if line[16] != sample and line[9] !=variant: #avoid duplicate variant_classification
		sample = line[16]	
		variant = line[9]

#print(len(proteinDict["MTS-T0058"]["TP53"]))
#print(proteinDict["MTS-T0058"]["TP53"])
#print(proteinDict["MTS-T0058"])
#print(variantDict["MTS-T0058"])
mutationsFile.close()
print("Sorting sample ids")
uniqueSampleIDs = set()
for key in clinicalDict:
	uniqueSampleIDs.add(key) 
for key in proteinDict:
	uniqueSampleIDs.add(key) 
for key in variantDict:
	uniqueSampleIDs.add(key) 
uniqueSampleIDs = sorted(list(uniqueSampleIDs))	
#output all our dictionaries to a file
print("Printing all data to file")

#outFile = open(outFilePath, "w")
with gzip.open(outFilePath, 'wb') as outFile:
	outText = "Sample\tVariable\tValue\n"
	outFile.write(outText.encode())
	for sample in uniqueSampleIDs:
		#add clinicalDict data first
		if sample in clinicalDict:
			for meta in clinicalDict[sample]:
				outText = sample+"\t"+meta+"\t"+clinicalDict[sample][meta]+"\n"
				outFile.write(outText.encode())
	
		#add CNA data
		if sample in cnaDict:
			for meta in cnaDict[sample]:
			
				#print(cnaDict[sample][meta])
				#if cnaDict[sample][meta] == 0:
				#	print("is 0 int")
				outText = sample + "\t"+meta+"\t"+ cnaDict[sample][meta]+"\n"
				outFile.write(outText.encode())
	
		#add variant classification info
		if sample in variantDict:
			for meta in variantDict[sample]:
				for value in variantDict[sample][meta]:
					outText = sample+"\t"+"SomaticMutation__"+meta+"__Variant_Classification"+"\t"+value+"\n"
					outFile.write(outText.encode())	
	
		#add protein variant info
		if sample in proteinDict:
			for meta in proteinDict[sample]: 
				for value in proteinDict[sample][meta]:
					outText = sample+"\t"+"SomaticMutation__"+meta+"__Protein_Variant"+"\t" +value+"\n"
					outFile.write(outText.encode())
#outFile.close()

