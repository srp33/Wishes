#!/bin/bash

set -euo pipefail

python3 ParseClinical.py "tmp/data_clinical_sample.txt" "tmp/data_clinical_patient.txt" "tmp/data_CNA.txt" "tmp/data_mutations_extended.txt" "tmp/Clinical.tsv.gz"

#python3 ParseExpression.py "tmp/data_expression.txt" "Gene_Expression.tsv.gz"

#python3 keep_common_samples.py "tmp/Clinical.tsv.gz" "Gene_Expression.tsv.gz"
#python3 convertTallFormatToWide.py "tmp/Clinical.tsv.gz" "Clinical.tsv.gz"
