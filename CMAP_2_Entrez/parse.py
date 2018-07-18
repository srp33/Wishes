from sys import argv
import gzip

dataIn = argv[1]
metaDataIn = argv[2]
dataOut = argv[3]
metaDataOut = argv[4]

def parseFiles(dataIn, metaDataIn, dataOut, metaDataOut):
    with open(dataIn, 'r') as dI:
        with open(metaDataIn, 'r') as mdI:
            with gzip.open(dataOut, 'w') as dO:
                with gzip.open(metaDataOut, 'w') as mdO:
                    #myDict = {}
                    sampleList = []
                    #varList = []
                    counter = 0
                    #print("Working through data file")
                    for line in dI:
                        counter += 1
                        #line = line.decode()
                        line = line.strip('\n').split('\t')
                        if counter == 1:
                            #varList = line
                            continue
                        else:
                            sampleList.append(line[0])
                            #myDict[line[0]] = line[1:]
                        #if counter == 1:
                        #    dO.write(('Sample\t' + line).encode())
                        #else:
                        #    dO.write((line).encode())
                        #    line = line.strip('\n').split('\t')
                        #    sampleList.append(line[0])
                        #if counter % 500 == 0:
                        #    print(counter)
            
                    counter = 0
                    print("Working through meta data")
                    mdO.write(("Sample\tVariable\tValue\n").encode())
                    for line in mdI:
                        counter += 1
                        line = line.strip('\n').split('\t')
                        if counter == 1:
                            firstLineList = line
                            continue
                        if line[7] in sampleList:
                            lineIter = 0
                            for item in firstLineList:
                                if item == "ScanID":
                                    continue
                                mdO.write((line[7] + '\t' + item + '\t' + line[lineIter] + '\n').encode())
                                lineIter += 1
                        if counter % 500 == 0:
                            print(counter)



parseFiles(dataIn, metaDataIn, dataOut, metaDataOut)
