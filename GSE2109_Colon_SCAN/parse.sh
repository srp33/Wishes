#! /bin/bash

Expression=/tmp/GSE2109_Colon_SCAN_Expression
Clinical=/tmp/GSE2109_Colon_SCAN_Clinical
outFile=data.tsv.gz

#bash download.sh

python parse.py $Clinical $Expression $outFile
