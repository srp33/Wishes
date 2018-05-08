#! /bin/bash

redirectedTemp=tmp
mkdir -p $redirectedTemp


url="https://tcga.xenahubs.net/download/TCGA.BRCA.sampleMap/Gistic2_CopyNumber_Gistic2_all_thresholded.by_genes.gz"
fileName=$redirectedTemp/Gistic2_CopyNumber_Gistic2_all_thresholded.by_genes.gz
wget -O $fileName $url
gunzip $fileName

#downloading CancerType Samples
url="https://www.ncbi.nlm.nih.gov/geo/download/?acc=GSE62944&format=file&file=GSE62944%5F06%5F01%5F15%5FTCGA%5F24%5F548%5FClinical%5FVariables%5F9264%5FSamples%2Etxt%2Egz"
fileName=$redirectedTemp/GSE62944_06_01_15_TCGA_24_CancerType_Samples.txt.gz

wget -O $fileName $url
gunzip $fileName

