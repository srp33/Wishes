#! /bin/bash

redirectedTempFolder=tmp
Expression=$redirectedTempFolder/GSE2109_Colon_SCAN_Expression
Clinical=$redirectedTempFolder/GSE2109_Colon_SCAN_Clinical
dataOutFile=data.tsv
metadataOutFile=metadata.tsv
dataOutFilegz=data.tsv.gz
metadataOutFilegz=metadata.tsv.gz

rm -f $metadataOutFilegz
rm -f $dataOutFilegz

python parse.py $Clinical $Expression $dataOutFile $metadataOutFile 

gzip $metadataOutFile
gzip $dataOutFile
