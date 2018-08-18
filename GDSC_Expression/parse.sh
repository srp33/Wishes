#! /bin/bash

redirectedTempFolder=tmp
cellLine=$redirectedTempFolder/Cell_Lines_Details.xlsx
doseResponse=$redirectedTempFolder/v17_fitted_dose_response.xlsx
screenedComponents=$redirectedTempFolder/Screened_Compounds.xlsx
RACS=$redirectedTempFolder/RACS_in_cell_lines.xlsx
variants=$redirectedTempFolder/WES_variants.xlsx
expression=$redirectedTempFolder/sanger1018_brainarray_ensemblgene_rma.txt.gz
expressiontmp=$redirectedTempFolder/expressiontmp.tsv.gz
dataOutFilegz=Gene_Expression.tsv.gz
metadataOutFilegz=metadata.tsv.gz

python parse.py $cellLine $doseResponse $screenedComponents $RACS $variants $expression $metadataOutFilegz $expressiontmp $dataOutFilegz 

python convertTallFormatToWide.py $metadataOutFilegz Annotations.tsv.gz
rm -f $metadataOutFilegz
