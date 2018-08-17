import sys, gzip

mutectIn = sys.argv[1]
varscanIn = sys.argv[2]
museIn = sys.argv[3]
somaticsniperIn = sys.argv[4]
outFile = sys.argv[5]

def columnsOfInterest(inFile, mutationDict, duplicationList) :
    with gzip.open(inFile, 'r') as iF :
        first = True
        alleleIndex = 0
        lineCounter = 0

        for line in iF :
            lineCounter = lineCounter + 1
            line = line.decode()
            if(line[0] == '#') :
                continue
            else :
                if first == True :
                    first = False
                    headerList = line.strip('\n').split('\t')
                    barcodeIndex = [i for i in range(len(headerList)) if headerList[i] == "Tumor_Sample_Barcode"][0]
                else : 
                    lineList = line.strip('\n').split('\t')
                    createdId = lineList[0] + "_" + '-'.join(lineList[barcodeIndex].split('-')[:4])
                    try :
                        mutationDict[createdId].add(inFile)
                    except KeyError :
                        mutationDict[createdId] = set()
                        mutationDict[createdId].add(inFile)

mutationDict = {}
duplicationList = []
columnsOfInterest(mutectIn, mutationDict, duplicationList)
columnsOfInterest(varscanIn, mutationDict, duplicationList)
columnsOfInterest(museIn, mutationDict, duplicationList)
columnsOfInterest(somaticsniperIn, mutationDict, duplicationList)

with open(outFile, 'w') as oF :
    oF.write(("Hugo_Symbol\tPatient_Id\n"))
    for createdId, files  in mutationDict.items() :
        if len(files) > 4 : 
            raise ValueError("Duplication in file")
        if len(files) > 2 :
            createdIdList = createdId.split('_')
            oF.write(('\t'.join(createdIdList) + "\n"))
