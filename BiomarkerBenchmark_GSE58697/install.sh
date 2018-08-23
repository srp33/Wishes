#! /bin/bash

cp ../Helper/BiomarkerBenchmark/download.sh .
cp ../Helper/BiomarkerBenchmark/parse.py .
cp ../Helper/BiomarkerBenchmark/parse.sh .
cp ../Helper/BiomarkerBenchmark/cleanup.sh .
cp ../Helper/convertTallFormatToWide.py .

sed -e s,{urlExpression},https://osf.io/yd8mp/download?version=4,g  ../Helper/BiomarkerBenchmark/download.sh > download.sh
