from sys import argv
import gzip

inFilePath = argv[1]
outFilePath = argv[2]

#with gzip.open(inFilePath, 'r') as inFile:
#    with gzip.open(outFilePath, 'w') as outFile:
#        counter = 0
#        linecounter = 0
#        lineList = set()
#        for line in inFile:
#            counter +=1
#            if counter == 1:
#                outFile.write(line)
#                continue
#            lineList = line.decode().rstrip('\n').split('\t')[3:]
#            if len(lineList) > 1:
#                outFile.write(line)
#            else:
#                linecounter += 1
#                continue
#        print(linecounter)
def allNA (myList):
    redFlag = True
    baseItem = myList[1]
    for item in myList:
        if item != baseItem:
            redFlag = False
        else:
            continue
    return redFlag


with gzip.open(inFilePath, 'r') as inFile:
    with gzip.open(outFilePath, 'w') as outFile:
        counter = 0
        myDict = {}
        sampleList = []
        for line in inFile:
            counter += 1
            if counter == 1:
                varList = line.decode().rstrip('\n').split('\t')[1:]
                for i in range(len(varList)):
                    myDict[varList[i]] = []
                continue
            lineList = line.decode().rstrip('\n').split('\t')
            valList = lineList[1:]
            sampleList.append(lineList[0])
            for i in range(len(varList)):
                myDict[varList[i]].append(valList[i])

        print("Old length: " + str(len(myDict.keys())))
        for item in varList:
            if allNA(myDict[item]):
                del myDict[item]
        print("New Length: " + str(len(myDict.keys())))
        varList = list(myDict.keys())
        outFile.write(("Sample\t" + '\t'.join(varList) + '\n').encode())
        
        counter = 0
        for j in range(len(sampleList)):
            counter += 1
            outFile.write((sampleList[j]).encode())
            for i in range(len(varList)):                    
                outFile.write(('\t' + myDict[varList[i]][j]).encode())
            outFile.write(('\n').encode())

