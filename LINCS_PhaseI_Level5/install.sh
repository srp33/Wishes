#! /bin/bash

#make Software Directory
softwareFolder=Software
mkdir -p $softwareFolder
echo $softwareFolder >> .gitignore

#installing miniconda
fileName=$softwareFolder/miniconda.sh
url="https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh"
softwareName=$softwareFolder/miniconda
wget $url -O $fileName
bash $fileName -b -p $softwareName
export PATH=$softwareName/bin:$PATH
rm $fileName
echo $softwareName >> .gitignore

#setting up channels for this project
conda config --add channels defaults
conda config --add channels conda-forge
conda config --add channels bioconda

#setting up environment for this project
export PATH=$softwareName/bin:$PATH
conda create --name my_cmapPy_env -y  python=2.7.11 numpy=1.11.2 pandas=0.18 h5py=2.6.0 requests==2.13.0 cmappy

#installing parrallel operation
url="https://ftp.gnu.org/gnu/parallel/parallel-latest.tar.bz2"
fileName=$softwareFolder/parallel-latest.tar.bz2
fileNameInDirectory=parallel-latest.tar.bz2

echo $fileName >> .gitignore

wget $url -O $fileName
cd $softwareFolder
tar -xvf $fileNameInDirectory
rm $fileNameInDirectory

