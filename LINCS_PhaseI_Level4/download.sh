#!/bin/bash

#make redirectedTempFolder
redirectedTempFolder=tmp
mkdir -p $redirectedTempFolder

#downloading the inst info meta data file
url="https://www.ncbi.nlm.nih.gov/geo/download/?acc=GSE92742&format=file&file=GSE92742%5FBroad%5FLINCS%5Finst%5Finfo%2Etxt%2Egz"
fileName=$redirectedTempFolder/GSE92742_Broad_LINCS_inst_info.txt.gz

curl -o "$fileName" -L "$url"


#downloading the LINCS - Phase I - Level 5 gctx file
url="https://www.ncbi.nlm.nih.gov/geo/download/?acc=GSE92742&format=file&file=GSE92742%5FBroad%5FLINCS%5FLevel4%5FZSPCINF%5Fmlr12k%5Fn1319138x12328%2Egctx%2Egz"
fileName=$redirectedTempFolder/LINCS_PhaseI_Level4.gctx.gz


curl -o "$fileName" -L "$url"
gunzip "$fileName"

#downloading the LINCS gene info
url="https://www.ncbi.nlm.nih.gov/geo/download/?acc=GSE92742&format=file&file=GSE92742%5FBroad%5FLINCS%5Fgene%5Finfo%2Etxt%2Egz"
fileName=$redirectedTempFolder/GSE92742_Broad_LINCS_gene_info.txt.gz


curl -o "$fileName" -L "$url"

#downloading GSE92742_Broad_LINCS_cell_info.txt.gz
url="https://www.ncbi.nlm.nih.gov/geo/download/?acc=GSE92742&format=file&file=GSE92742%5FBroad%5FLINCS%5Fcell%5Finfo%2Etxt%2Egz"
fileName=$redirectedTempFolder/GSE92742_Broad_LINCS_cell_info.txt.gz

curl -o "$fileName" -L "$url"

#downloading GSE92742_Broad_LINCS_pert_info.txt.gz
url="https://www.ncbi.nlm.nih.gov/geo/download/?acc=GSE92742&format=file&file=GSE92742%5FBroad%5FLINCS%5Fpert%5Finfo%2Etxt%2Egz"
fileName=$redirectedTempFolder/GSE92742_Broad_LINCS_pert_info.txt.gz

curl -o "$fileName" -L "$url"

#downloading GSE92742_Broad_LINCS_pert_metrics.txt.gz
url="https://www.ncbi.nlm.nih.gov/geo/download/?acc=GSE92742&format=file&file=GSE92742%5FBroad%5FLINCS%5Fpert%5Fmetrics%2Etxt%2Egz"
fileName=$redirectedTempFolder/GSE92742_Broad_LINCS_pert_metrics.txt.gz

curl -o "$fileName" -L "$url"

