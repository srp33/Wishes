#! /bin/bash

redirectedTemp=tmp
mkdir -p $redirectedTemp


url="https://tcga.xenahubs.net/download/TCGA.BRCA.sampleMap/RPPA.gz"
fileName=$redirectedTemp/TCGA.BRCA.sampleMap.gz
wget -O $fileName $url
gunzip $fileName

#downloading CancerType Samples
url="https://www.ncbi.nlm.nih.gov/geo/download/?acc=GSE62944&format=file&file=GSE62944%5F06%5F01%5F15%5FTCGA%5F24%5FCancerType%5FSamples%2Etxt%2Egz"
fileName=$redirectedTemp/GSE62944_06_01_15_TCGA_24_CancerType_Samples.txt.gz

wget -O $fileName $url
gunzip $fileName

