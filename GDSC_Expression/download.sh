#! /bin/bash

function downloadData {
  url="$1"

  fileName="$redirectedTempFolder/$(basename $url)"

  if [ ! -f "$fileName" ]
  then
    curl -o "$fileName" -L "$url"
  fi
}

#make redirectedTempFolder
redirectedTempFolder=tmp
mkdir -p $redirectedTempFolder

downloadData "ftp://ftp.sanger.ac.uk/pub/project/cancerrxgene/releases/release-6.0/Cell_Lines_Details.xlsx"
downloadData "ftp://ftp.sanger.ac.uk/pub/project/cancerrxgene/releases/release-6.0/Screened_Compounds.xlsx"
downloadData "ftp://ftp.sanger.ac.uk/pub/project/cancerrxgene/releases/release-6.0/v17_fitted_dose_response.xlsx"
downloadData "ftp://ftp.sanger.ac.uk/pub/project/cancerrxgene/releases/release-6.0/RACS_in_cell_lines.xlsx"
downloadData "ftp://ftp.sanger.ac.uk/pub/project/cancerrxgene/releases/release-6.0/WES_variants.xlsx"
downloadData "ftp://ftp.sanger.ac.uk/pub/project/cancerrxgene/releases/release-6.0/sanger1018_brainarray_ensemblgene_rma.txt.gz"
