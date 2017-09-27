import sys, gzip

expressionData = sys.argv[1]
clinicalData = sys.argv[2]
dataOutFile = sys.argv[3]
metedataOutFile = sys.argv[4]

#write outFile, clinical on left expression on Right
with open(expressionData, 'r')  as f:
    with open(dataOutFile, 'w') as o:
        headerList = f.readline().strip('\n').split('\t')
        o.write("Sample" + '\t' + '\t'.join(headerList[1:]) + '\n')
        for line in f:
            o.write(line)

with open(clinicalData, 'r') as f:
    with open(metedataOutFile, 'w') as o:
        headerList = f.readline().strip('\n').split('\t')
        o.write("Sample\tVariable\tValue\n")
        for line in f:
            lineList = line.strip('\n').split('\t')
            o.write(lineList[0] + '\t' + headerList[1] + '\t' + lineList[1] + '\n') 
