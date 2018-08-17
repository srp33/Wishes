#! /bin/bash/

#Run parseData.py on all four datasets
bash parseCNV.sh
#bash parseGDC.sh
bash parseMiRNA.sh
bash parseRPPA.sh

#Generate cleaned Clinical data
bash parseMeta.sh


