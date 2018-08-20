#! /bin/bash

python3 ParseMetadata.py tmp/CMAP_Metadata.tsv Metadata.tsv.gz

Rscript entrezIdConvert.R tmp/Matrices/CMap_SCAN_EntrezGene_BatchAdjusted.tsv.gz Gene_Expression.tsv.gz
