#! /bin/bash

redirectedTempFolder=~/compute/tmp_GSE10320_SCAN
expressionData=$redirectedTempFolder/GSE10320_SCAN_Expression
clinicalData=$redirectedTempFolder/GSE10320_SCAN_Clinical
outFile=data.tsv.gz

python parse.py $expressionData $clinicalData $outFile 

rm -f .gitignore
echo $outFile >> .gitignore

rm -r $redirectedTempFolder
