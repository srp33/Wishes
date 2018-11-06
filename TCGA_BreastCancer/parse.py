import sys, gzip, re

mutectIn = sys.argv[1]
varscanIn = sys.argv[2]
museIn = sys.argv[3]
somaticsniperIn = sys.argv[4]
mutectOut = sys.argv[5]
varscanOut = sys.argv[6]
museOut = sys.argv[7]
somaticsniperOut = sys.argv[8]

def adjustFile(inFile, outFile) :
    with gzip.open(inFile, 'r') as iF :
        with gzip.open(outFile, 'w') as oF:
            first = True

            for line in iF :
                line = line.decode()
                if(line[0] == '#') :
                     continue
                else :
                    if first == True :
                        first = False
                        headerList = line.strip('\n').split('\t')
                        filterIndex = [i for i in range(len(headerList)) if headerList[i] == "FILTER"][0]
                        impactIndex = [i for i in range(len(headerList)) if headerList[i] == "IMPACT"][0]
                        clinSigIndex = [i for i in range(len(headerList)) if headerList[i] == "CLIN_SIG"][0]
                        exACAFIndex = [i for i in range(len(headerList)) if headerList[i] == "ExAC_AF"][0]
                        SIFTIndex = [i for i in range(len(headerList)) if headerList[i] == "SIFT"][0]
                        PolyPhenIndex = [i for i in range(len(headerList)) if headerList[i] == "PolyPhen"][0]
                        oF.write(line.encode())
                    else : 
                        lineList = line.strip('\n').split('\t')
                        if(lineList[filterIndex] == "PASS") :
                            if(lineList[impactIndex] == "HIGH") or (lineList[impactIndex] == "MODERATE") :
                                if lineList[exACAFIndex] == "" :
                                    exACAFSig = True
                                else :
                                    exACAFSig = float(lineList[exACAFIndex]) <= .01

                                if(lineList[clinSigIndex] == "pathogenic") :
                                    oF.write(line.encode())
                                elif exACAFSig == True :
                                    if("deleterious" in lineList[SIFTIndex]) or ("probably_damaging" in lineList[PolyPhenIndex]) :
                                        oF.write(line.encode())
                                    elif("tolerated" in lineList[SIFTIndex]) and ("possibly_damaging" in lineList[PolyPhenIndex]) :
                                        if "tolerated_low_confidence" not in lineList[SIFTIndex] :
                                            toleratedLevel = re.findall("\d+\.*\d*", lineList[SIFTIndex])
                                            if float(toleratedLevel[0]) <= .2 :
                                                oF.write(line.encode())
                                    

adjustFile(mutectIn, mutectOut)
adjustFile(varscanIn, varscanOut)
adjustFile(museIn, museOut)
adjustFile(somaticsniperIn, somaticsniperOut)
