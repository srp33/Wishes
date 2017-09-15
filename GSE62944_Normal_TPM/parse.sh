#! /bin/bash

redirectedTempFolder=tmp
PatientCancerType=$redirectedTempFolder/GSE62944_06_01_15_TCGA_24_Normal_CancerType_Samples.txt
NormalTPM=$redirectedTempFolder/GSM1697009_06_01_15_TCGA_24.normal_Rsubread_TPM.txt
transposedNormalTPM=$redirectedTempFolder/transposedNormalTPM.txt
outFile=data.tsv.gz

#execute
python parse.py $PatientCancerType $NormalTPM $transposedNormalTPM $outFile

#clean-up
rm -f .gitignore
echo $outFile >> .gitignore
echo $redirectedTempFolder >> .gitignore
rm -r $redirectedTempFolder
