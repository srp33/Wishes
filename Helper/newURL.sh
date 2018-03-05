#!/bin/bash

newURL=$1

echo "#! /bin/bash
cp ../Helper/BiomarkerBenchmark/download.sh .
cp ../Helper/BiomarkerBenchmark/parse.py .
cp ../Helper/BiomarkerBenchmark/parse.sh .
cp ../Helper/BiomarkerBenchmark/cleanup.sh .
sed -e "s,{urlExpression},$newURL?version=4,g"  ../Helper/BiomarkerBenchmark/download.sh > download.sh" > install.sh


