#! /bin/bash

redirectedTempFolder=tmp
PatientCancerType=$redirectedTempFolder/GSE62944_06_01_15_TCGA_24_Normal_CancerType_Samples.txt.gz
NormalFeatureCounts=$redirectedTempFolder/GSM1697009_06_01_15_TCGA_24.normal_Rsubread_FeatureCounts.txt.gz
nameToAbbreviation="nameToAbbreviation.txt"
dataOutFile=Gene_Expression.tsv
metadataOutFile=metadata.tsv
clinicalDataOut=Clinical.tsv

python parse.py $PatientCancerType $NormalFeatureCounts $dataOutFile $metadataOutFile $nameToAbbreviation
python ../Helper/convertTallFormatToWide2.py $metadataOutFile $clinicalDataOut
rm -f $metadataOutFile
