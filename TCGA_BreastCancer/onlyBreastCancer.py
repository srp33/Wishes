import gzip
from sys import argv

inFile = argv[1]
outFile = argv[2]

print("Removing everything except Breast Cancer Samples")
with gzip.open(inFile, 'r') as iF:
    with gzip.open(outFile, 'w') as oF:
        counter = 0
        for line in iF:
            counter += 1
            if counter == 1:
                oF.write(line)
            lineList = line.decode().rstrip('\n').split('\t')
            if "BRCA" not in lineList[1]:
                continue
            else:
                oF.write(line)
