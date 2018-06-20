#! /bin/bash


metadataOut=metadata.tsv.gz
metadataTranslated=Clinical.tsv.gz

python3 translate.py $metadataOut $metadataTranslated
