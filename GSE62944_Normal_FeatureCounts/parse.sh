#! /bin/bash

redirectedTempFolder=tmp
PatientCancerType=$redirectedTempFolder/GSE62944_06_01_15_TCGA_24_Normal_CancerType_Samples.txt
NormalFeatureCounts=$redirectedTempFolder/GSM1697009_06_01_15_TCGA_24.normal_Rsubread_FeatureCounts.txt
transposedNormalFeatureCounts=$redirectedTempFolder/transposedNormalTPM.txt
dataOutFile=data.tsv
metadataOutFile=metadata.tsv
dataOutFilegz=data.tsv.gz
metadataOutFilegz=metadata.tsv.gz

rm -f $metadataOutFilegz
rm -f $dataOutFilegz

python parse.py $PatientCancerType $NormalFeatureCounts $transposedNormalFeatureCounts $dataOutFile $metadataOutFile

gzip $metadataOutFile
gzip $dataOutFile
