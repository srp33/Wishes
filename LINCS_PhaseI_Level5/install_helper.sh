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

#installing parrallel operation
downloadAndInstall "https://ftp.gnu.org/gnu/parallel/parallel-20170922.tar.bz2" "tar"

#installing miniconda
softwareName=$softwareFolder/miniconda
downloadAndInstall "https://repo.continuum.io/miniconda/Miniconda3-4.3.27.1-Linux-x86_64.sh" "$softwareName"

#setting up channels for this project
export PATH=$softwareName/bin:$PATH

conda config --add channels defaults
conda config --add channels conda-forge
conda config --add channels bioconda

#setting up environment for this project
export PATH=$softwareName/bin:$PATH
conda create --name my_cmapPy_env -y  python=2.7.11 numpy=1.11.2 pandas=0.18 h5py=2.6.0 requests==2.13.0 cmappy

