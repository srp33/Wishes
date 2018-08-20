#!/bin/bash

set -euo pipefail

python3 parse_metadata.py "./brca_metabric/data_clinical_sample.txt" "./brca_metabric/data_clinical_patient.txt" "./brca_metabric/data_CNA.txt" "./brca_metabric/data_mutations_extended.txt" "metadata.tsv.gz"
python3 parse_data.py "./brca_metabric/data_expression.txt" "data.tsv.gz"
python3 keep_common_samples.py "metadata.tsv.gz" "data.tsv.gz"
python3 convertTallFormatToWide.py "metadata.tsv.gz" "Clinical.tsv.gz"

