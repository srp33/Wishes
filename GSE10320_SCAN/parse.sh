#! /bin/bash

redirectedTempFolder=tmp
expressionData=$redirectedTempFolder/GSE10320_SCAN_Expression
clinicalData=$redirectedTempFolder/GSE10320_SCAN_Clinical
outFile=data.tsv
outFilegz=data.tsv.gz

#execute
python parse.py $expressionData $clinicalData $outFile 

#clean-up
rm -f .gitignore
echo $outFilegz >> .gitignore
rm -r $redirectedTempFolder

gzip $outFile
