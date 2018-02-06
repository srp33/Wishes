#! /bin/bash

function downloadAndInstall {
  url="$1"
  fileName="$softwareFolder/$(basename $url)"

  if [ ! -f "$fileName" ];
  then
    curl -o "$fileName" -L "$url"
    if [ "$2" == "tar" ];
    then
      tar -xvf "$fileName" --directory "$softwareFolder"
    else
      bash "$fileName" -b -p "$2"
    fi
    rm "$fileName"
  fi
}

#make Software Directory
softwareFolder=Software
mkdir -p $softwareFolder

#installing miniconda
softwareName=$softwareFolder/miniconda
downloadAndInstall "https://repo.continuum.io/miniconda/Miniconda3-4.3.27.1-Linux-x86_64.sh" "$softwareName"

#setting up environment for this project
export PATH=$softwareName/bin:$PATH
conda create --name my_GDSC_Expression_env -y python=2.7.11 pandas=0.18 xlrd=1.1.0 
