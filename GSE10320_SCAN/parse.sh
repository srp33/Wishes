#! /bin/bash

expressionData=/tmp/GSE10320_SCAN_Expression
clinicalData=/tmp/GSE10320_SCAN_Clinical
outFile=data.tsv.gz

python parse.py $expressionData $clinicalData $outFile 

rm -f .gitignore
echo $outFile >> .gitignore
