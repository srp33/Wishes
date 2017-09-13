#! /bin/bash

redirectedTempFolder=~/compute/tmp_GSE62944_Normal_TPM
PatientCancerType=$redirectedTempFolder/GSE62944_06_01_15_TCGA_24_Normal_CancerType_Samples.txt
NormalTPM=$redirectedTempFolder/GSM1697009_06_01_15_TCGA_24.normal_Rsubread_TPM.txt
transposedNormalTPM=$redirectedTempFolder/transposedNormalTPM.txt
outFile=data.tsv.gz

python parse.py $PatientCancerType $NormalTPM $transposedNormalTPM $outFile

rm -f .gitignore
echo $outFile >> .gitignore

rm -r $redirectedTempFolder
