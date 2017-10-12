#!/bin/bash

#make redirectedTempFolder
redirectedTempFolder=tmp
mkdir -p $redirectedTempFolder

#downloading the GSE70138_Broad_LINCS_sig_info_2017-03-06.txt.gz
url="https://www.ncbi.nlm.nih.gov/geo/download/?acc=GSE70138&format=file&file=GSE70138%5FBroad%5FLINCS%5Fsig%5Finfo%5F2017%2D03%2D06%2Etxt%2Egz"
fileName=$redirectedTempFolder/GSE70138_Broad_LINCS_sig_info_2017-03-06.txt.gz

curl -o "$fileName" -L "$url"


#downloading the LINCS - Phase I - Level 5 gctx file
url="https://www.ncbi.nlm.nih.gov/geo/download/?acc=GSE70138&format=file&file=GSE70138%5FBroad%5FLINCS%5FLevel5%5FCOMPZ%5Fn118050x12328%5F2017%2D03%2D06%2Egctx%2Egz"
fileName=$redirectedTempFolder/LINCS_PhaseII_Level5.gctx.gz

curl -o "$fileName" -L "$url"
gunzip "$fileName"

#downloading the GSE70138_Broad_LINCS_gene_info_2017-03-06.txt.gz
url="https://www.ncbi.nlm.nih.gov/geo/download/?acc=GSE70138&format=file&file=GSE70138%5FBroad%5FLINCS%5Fgene%5Finfo%5F2017%2D03%2D06%2Etxt%2Egz"
fileName=$redirectedTempFolder/GSE70138_Broad_LINCS_gene_info_2017-03-06.txt.gz

curl -o "$fileName" -L "$url"

#downloading GSE70138_Broad_LINCS_cell_info_2017-04-28.txt.gz
url="https://www.ncbi.nlm.nih.gov/geo/download/?acc=GSE70138&format=file&file=GSE70138%5FBroad%5FLINCS%5Fcell%5Finfo%5F2017%2D04%2D28%2Etxt%2Egz"
fileName=$redirectedTempFolder/GSE70138_Broad_LINCS_cell_info_2017-04-28.txt.gz

curl -o "$fileName" -L "$url"

#downloading GSE70138_Broad_LINCS_pert_info_2017-03-06.txt.gz
url="https://www.ncbi.nlm.nih.gov/geo/download/?acc=GSE70138&format=file&file=GSE70138%5FBroad%5FLINCS%5Fpert%5Finfo%5F2017%2D03%2D06%2Etxt%2Egz"
fileName=$redirectedTempFolder/GSE70138_Broad_LINCS_pert_info_2017-03-06.txt.gz

curl -o "$fileName" -L "$url"

#downloading GSE70138_Broad_LINCS_sig_metrics_2017-03-06.txt.gz
url="https://www.ncbi.nlm.nih.gov/geo/download/?acc=GSE70138&format=file&file=GSE70138%5FBroad%5FLINCS%5Fsig%5Fmetrics%5F2017%2D03%2D06%2Etxt%2Egz"
fileName=$redirectedTempFolder/GSE70138_Broad_LINCS_sig_metrics_2017-03-06.txt.gz

curl -o "$fileName" -L "$url"
