#!/bin/bash

set -euo pipefail

python3 ParseClinical.py tmp/data_clinical_patient.txt "" Patient_Characteristics.tsv
python3 ParseClinical.py tmp/data_clinical_sample.txt "Sample Identifier" Sample_Characteristics.tsv
python3 ParseCNA.py tmp/data_CNA.txt Copy_Number_Alterations.tsv
python3 ParseMutations.py tmp/data_mutations_extended.txt
##python3 ParseMutations.py tmp/data_mutations_extended.txt HGVSp HGVS_Protein_Description.tsv
python3 ParseExpression.py "tmp/data_expression.txt" "Gene_Expression.tsv"

python3 keep_common_samples.py *.tsv

## Remove this because it has no Yes values
rm -f Variant_5_prime_UTR.tsv.gz
