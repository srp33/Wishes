#! /bin/bash

cp ../Helper/convertTallFormatToWide.py .
#setting up environment for this project
export PATH=$softwareName/bin:$PATH
conda create --name my_GDSC_Expression_env -y python=2.7.11 pandas=0.18 xlrd=1.1.0 
