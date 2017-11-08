#! /bin/bash

cp ../Helper/BiomarkerBenchmark/download.sh .
cp ../Helper/BiomarkerBenchmark/parse.py .
cp ../Helper/BiomarkerBenchmark/parse.sh .
cp ../Helper/BiomarkerBenchmark/cleanup.sh .
cp badfile badlocation

sed -e "s,{urlExpression},https://osf.io/4m3sv/download,g" -e "s,{urlClinical},https://osf.io/pxkfy/download,g" ../Helper/BiomarkerBenchmark/download.sh > download.sh 

