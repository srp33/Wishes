#!/bin/bash

# Make sure the whole script will fail if any part of it fails
set -euo pipefail

python3 parse_metadata.py tmp/donor.BRCA-US.tsv.gz "metadata.tsv.gz"
python3 parse_data.py tmp/exp_seq.BRCA-US.tsv.gz "data.tsv.gz"
python3 keep_common_samples.py "metadata.tsv.gz" "data.tsv.gz"
python3 convertTallFormatToWide.py "metadata.tsv.gz" "Clinical.tsv.gz"

