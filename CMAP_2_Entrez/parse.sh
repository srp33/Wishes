#! /bin/bash

redirectedTmpFolder=tmp
dataIn=$redirectedTmpFolder/Matrices/CMap_SCAN_EntrezGene_BatchAdjusted.tsv.gz
convertedData=$redirectedTmpFolder/test.tsv
metaDataIn=$redirectedTmpFolder/CMAP_Metadata.tsv
dataOut=data.tsv.gz
metaDataOut=metadata.tsv.gz
convertedMetaOut=Clinical.tsv.gz

Rscript parse_helpers/entrezIdConvert.R $dataIn $convertedData
python3 parse.py $convertedData $metaDataIn $dataOut $metaDataOut
python3 convertTallFormatToWide.py $metaDataOut $convertedMetaOut
cp $convertedData data.tsv
rm data.tsv.gz
gzip data.tsv
