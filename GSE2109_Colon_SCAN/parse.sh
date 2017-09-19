#! /bin/bash

redirectedTempFolder=tmp
Expression=$redirectedTempFolder/GSE2109_Colon_SCAN_Expression
Clinical=$redirectedTempFolder/GSE2109_Colon_SCAN_Clinical
outFile=data.tsv
outFilegz=data.tsv.gz

#execute
python parse.py $Clinical $Expression $outFile

#clean-up
rm -f .gitignore
echo $outFilegz >> .gitignore
rm -r $redirectedTempFolder

gzip $outFile
