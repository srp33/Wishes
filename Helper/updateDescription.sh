#!/bin/bash

#1 is new URL, 2 is dataset number

bash cleanup.sh
bash ../Helper/newURL.sh $1
bash install.sh
bash download.sh

#Get lines from Description File3
SOURCE=$(cat newDescription | grep "Citation" -A1 | tail -n 1)
TITLE=$(cat newDescription | grep "Title" -A1 | tail -n 1)

sed -e "s,{dataset},$2,g" -e "s,{source},$SOURCE,g"   ../Helper/BiomarkerBenchmark/description.md > description.md
TITLE="title: $TITLE ($2)"


