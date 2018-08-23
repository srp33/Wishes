#!/bin/bash

# Because we will need to download two files, let's create a bash function that performs the steps necessary to download a file.
function downloadData {
  # This function accepts one parameter, the URL.
  # Let's assign this to a variable.
  url="$1"

  # Create a variable that parses the file name from the URL.
  fileName="$(basename $url)"

  # Check to see if the file has been downloaded already. If not, download it.
  if [ ! -f "tmp/$fileName" ]
  then
    echo Downloading "$fileName"
    curl -o "tmp/$fileName" -L "$url"

    if [ ! -f "tmp/$fileName" ]
    then
      echo "Trying $fileName again"
      curl -o "tmp/$fileName" -L "$url"
    fi
  fi
}

mkdir -p tmp

for f in data_clinical_patient.txt data_clinical_sample.txt data_CNA.txt data_mutations_extended.txt data_expression.txt
do
  downloadData https://media.githubusercontent.com/media/cBioPortal/datahub/master/public/brca_metabric/$f
done
