#! /bin/bash

redirectedTempFolder=tmp
PatientCancerType=$redirectedTempFolder/GSE62944_06_01_15_TCGA_24_Normal_CancerType_Samples.txt.gz
NormalFeatureCounts=$redirectedTempFolder/GSM1697009_06_01_15_TCGA_24.normal_Rsubread_FeatureCounts.txt.gz
nameToAbbreviation="nameToAbbreviation.txt"
dataOutFilegz=data.tsv.gz
metadataOutFilegz=metadata.tsv.gz
clinicalDataOut=Clinical.tsv.gz

python parse.py $PatientCancerType $NormalFeatureCounts $dataOutFilegz $metadataOutFilegz $nameToAbbreviation
python convertTallFormatToWide.py $metadataOutFilegz $clinicalDataOut
rm -f metadata.tsv.gz
