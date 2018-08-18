#!/bin/bash

function downloadFile {
  url="$1"
  fileName="$redirectedTempFolder/$2"

  if [ ! -f "$fileName" ];
  then
    curl -o "$fileName" -L "$url"
  fi
}

redirectedTempFolder=tmp
mkdir -p $redirectedTempFolder

#downloading files
downloadFile "https://www.ncbi.nlm.nih.gov/geo/download/?acc=GSE70138&format=file&file=GSE70138%5FBroad%5FLINCS%5Fsig%5Finfo%5F2017%2D03%2D06%2Etxt%2Egz" "GSE70138_Broad_LINCS_sig_info_2017-03-06.txt.gz"
downloadFile "https://www.ncbi.nlm.nih.gov/geo/download/?acc=GSE70138&format=file&file=GSE70138%5FBroad%5FLINCS%5FLevel5%5FCOMPZ%5Fn118050x12328%5F2017%2D03%2D06%2Egctx%2Egz" "LINCS_PhaseII_Level5.gctx.gz"
downloadFile "https://www.ncbi.nlm.nih.gov/geo/download/?acc=GSE70138&format=file&file=GSE70138%5FBroad%5FLINCS%5Fgene%5Finfo%5F2017%2D03%2D06%2Etxt%2Egz" "GSE70138_Broad_LINCS_gene_info_2017-03-06.txt.gz"
downloadFile "https://www.ncbi.nlm.nih.gov/geo/download/?acc=GSE70138&format=file&file=GSE70138%5FBroad%5FLINCS%5Fcell%5Finfo%5F2017%2D04%2D28%2Etxt%2Egz" "GSE70138_Broad_LINCS_cell_info_2017-04-28.txt.gz"
downloadFile "https://www.ncbi.nlm.nih.gov/geo/download/?acc=GSE70138&format=file&file=GSE70138%5FBroad%5FLINCS%5Fpert%5Finfo%5F2017%2D03%2D06%2Etxt%2Egz" "GSE70138_Broad_LINCS_pert_info_2017-03-06.txt.gz"
downloadFile "https://www.ncbi.nlm.nih.gov/geo/download/?acc=GSE70138&format=file&file=GSE70138%5FBroad%5FLINCS%5Fsig%5Fmetrics%5F2017%2D03%2D06%2Etxt%2Egz" "GSE70138_Broad_LINCS_sig_metrics_2017-03-06.txt.gz"

cd $redirectedTempFolder
gunzip "LINCS_PhaseII_Level5.gctx.gz"
