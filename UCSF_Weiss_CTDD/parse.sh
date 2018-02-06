#!/bin/bash

set -euo pipefail

python3 parse_data.py "tmp/expression_main.txt" "tmp/probe_attributes.txt" "data.tsv.gz"
python3 parse_metadata.py "tmp/sample_attributes.txt" "metadata.tsv.gz"
python3 keep_common_samples.py "metadata.tsv.gz" "data.tsv.gz"
