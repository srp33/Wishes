#!/bin/bash

mkdir tmp

# Because we will need to download two files, let's create a bash function that performs the steps necessary to download a file.
function downloadData {
  # This function accepts one parameter, the URL.
  # Let's assign this to a variable.
  url="$1"

  # Create a variable that parses the file name from the URL.
  fileName="$(basename $url)"

  # Check to see if the file has been downloaded already. If not, download it.
  if [ ! -f "$fileName" ]
  then
    curl -o "$fileName" -L "$url"
  fi
}

# The data files are stored here: https://dcc.icgc.org/releases/release_25/Projects/BRCA-US
# Let's invoke the function that we just declared, for each file we want to download.
downloadData "https://dcc.icgc.org/api/v1/download?fn=/release_25/Projects/BRCA-US/donor.BRCA-US.tsv.gz"
downloadData "https://dcc.icgc.org/api/v1/download?fn=/release_25/Projects/BRCA-US/exp_seq.BRCA-US.tsv.gz"

mv donor.BRCA-US.tsv.gz tmp/ 
mv exp_seq.BRCA-US.tsv.gz tmp/ 
