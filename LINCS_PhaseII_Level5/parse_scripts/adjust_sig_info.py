import sys, gzip

inFilePath = sys.argv[1]
outFilePath = sys.argv[2]

with gzip.open(inFilePath) as f:
    inHeaderItems = f.readline().rstrip("\n").split("\t")
    with gzip.open(outFilePath, 'w') as g:
        g.write('\t'.join(inHeaderItems) + '\n')
        for line in f:
            value = line.rstrip("\n").split("\t") 
            try:
                float(value[5])
                float(value[7])
                g.write(line)
            except ValueError:
                new = value[5].split("|")
                value[5] = new[0]
                if '-666' in value[7]:
                    value[7] = '-666'
                g.write('\t'.join(value) + '\n')
