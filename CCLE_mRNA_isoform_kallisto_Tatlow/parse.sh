#! /bin/bash

redirectedTempFolder=tmp
expressionData=$redirectedTempFolder/CCLE_tpm.tsv
outFile=data.tsv
outFilegz=data.tsv.gz

#execute
python parse.py $expressionData $outFile

#clean-up
rm -f .gitignore
echo $outFilegz >> .gitignore
echo $redirectedTempFolder >> .gitignore
rm -r $redirectedTempFolder

gzip data.tsv
