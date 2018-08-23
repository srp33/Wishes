#make redirectedTempFolder
redirectedTempFolder=tmp
mkdir -p $redirectedTempFolder

#downloading the tar file 
url="https://osf.io/xtuq2/download"
fileName=$redirectedTempFolder/cmap.tar

wget -O $fileName $url

cd $redirectedTempFolder
tar -xvf cmap.tar

rm cmap.tar
