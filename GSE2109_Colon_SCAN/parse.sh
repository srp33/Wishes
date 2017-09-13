#! /bin/bash

redirectedTempFolder=~/compute/tmp_GSE2109_Colon_SCAN
Expression=$redirectedTempFolder/GSE2109_Colon_SCAN_Expression
Clinical=$redirectedTempFolder/GSE2109_Colon_SCAN_Clinical
outFile=data.tsv.gz

python parse.py $Clinical $Expression $outFile

rm -f .gitignore
echo $outFile >> .gitignore

rm -r $redirectedTempFolder
