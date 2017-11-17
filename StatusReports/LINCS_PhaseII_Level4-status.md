<h1><center>LINCS_PhaseII_Level4</center></h1>
<h2><center> Status: In Progress </center></h2>


### Testing Directory . . .

#### Results: PASS
---
### Testing Description File . . .

&#9989;	Title is less than 100 characters

#### Results: PASS
---
### Running Install . . .

Executing install.sh: Success

#### Results: PASS
---

### Testing file paths:

&#9989;	test_data.tsv exists.

&#9989;	test_metadata.tsv exists.

&#9989;	download.sh exists.

&#9989;	install.sh exists.

&#9989;	parse.sh exists.

&#9989;	cleanup.sh exists.

&#9989;	description.md exists.

*Running user code . . .*

Executing download.sh: Success

Executing parse.sh: Success

&#9989;	data.tsv.gz was created and zipped correctly.

&#9989;	metadata.tsv.gz was created and zipped correctly.

#### Results: PASS
---
### Testing Key Files:

&#9989;	test_data.tsv contains enough unique samples to test

&#9989;	test_data.tsv contains enough test cases (12; min: 8)

&#9989;	test_metadata.tsv contains enough unique samples to test

&#9989;	test_metadata.tsv contains enough test cases (15; min: 8)

#### Results: PASS
---

### First 5 columns and 5 rows of data.tsv.gz:

|	Sample	|	DDR1	|	PAX8	|	GUCA1A	|	EPHB3	|
|	---	|	---	|	---	|	---	|	---	|
|	LJP005_A375_24H_X1_B19:A03	|	-0.318599998951	|	-0.869700014591	|	0.715499997139	|	-0.679000020027	|
|	LPROT001_A375_6H_X1_B20:B03	|	-1.03359997272	|	-0.562600016594	|	0.214800000191	|	0.263099998236	|
|	LPROT001_A375_6H_X1_B20:B05	|	0.294299989939	|	0.241500005126	|	-0.57380002737	|	1.8723000288	|
|	LPROT002_A375_6H_X1_B22:B03	|	0.542800009251	|	-0.958100020885	|	-0.118100002408	|	0.0888999998569	|

**Columns: 12329 Rows: 345632**

---
### "data.tsv.gz" Test Cases (from rows in test file). . .

&#9989;	First column of file is titled "Sample"

&#10060;	Row 7 of "test_data.tsv" does not contain 3 columns

&#9989;	Row 1: Success

&#9989;	Row 2: Success

&#9989;	Row 3: Success

&#9989;	Row 4: Success

&#9989;	Row 5: Success

&#9989;	Row 6: Success

&#10060;	Row: 7 - Sample "REP.A028_YAPC_24H_X1_B25:G09" is not found in data.tsv.gz

&#9989;	Row 8: Success

&#9989;	Row 9: Success

&#9989;	Row 10: Success

&#9989;	Row 11: Success

&#9989;	Row 12: Success

#### Results: **<font color="red">FAIL</font>**
---
### First 3 columns and 5 rows of metadata.tsv.gz:

|	Sample	|	Variable	|	Value	|
|	---	|	---	|	---	|
|	LJP005_A375_24H_X1_B19:A03	|	cell_id	|	A375	|
|	LJP005_A375_24H_X1_B19:A03	|	cell_type	|	cell line	|
|	LJP005_A375_24H_X1_B19:A03	|	base_cell_id	|	A375	|
|	LJP005_A375_24H_X1_B19:A03	|	sample_type	|	tumor	|

**Columns: 3 Rows: 7778851**

---
### "metadata.tsv.gz" Test Cases (from rows in test file). . .

&#9989;	First column of file is titled "Sample"

&#10060;	The value for variable "pert_time_unit" for all samples is the same ("h").

&#9989;	Row 1: Success

&#9989;	Row 2: Success

&#9989;	Row 3: Success

&#9989;	Row 4: Success

&#9989;	Row 5: Success

&#9989;	Row 6: Success

&#9989;	Row 7: Success

&#9989;	Row 8: Success

&#10060;	Row 9: Fail
- "REP.A028_YAPC_24H_X3_B25:P24	cell_id	YAPC" is not found.

&#10060;	Row 10: Fail
- "REP.A028_YAPC_24H_X3_B25:P24	cell_type	cell line" is not found.

&#10060;	Row 11: Fail
- "REP.A028_YAPC_24H_X3_B25:P24	donor_sex	M" is not found.

&#10060;	Row 12: Fail
- "REP.A028_YAPC_24H_X3_B25:P24	det_plate	REP.A028_YAPC_24H_X3_B25" is not found.

&#10060;	Row 13: Fail
- "REP.A028_YAPC_24H_X3_B25:P24	pert_id	BRD-A97502381" is not found.

&#10060;	Row 14: Fail
- "REP.A028_YAPC_24H_X3_B25:P24	inchi_key	FMCRMSOQAVOHRD-SBGISONWSA-M" is not found.

&#10060;	Row 15: Fail
- "REP.A028_YAPC_24H_X3_B25:P24	pert_iname	cyanocobalamin" is not found.

#### Results: **<font color="red">FAIL</font>**
---
### Making sure no commas exist in either file . . .

&#10060;	Comma(s) exist in "metadata.tsv.gz"

#### Results: **<font color="red">FAIL</font>**
---
### Comparing samples in both files . . .

&#9989;	Samples are the same in both "data.tsv.gz" & "metadata.tsv.gz"

#### Results: PASS

---
### Testing Directory after cleanup . . .

#### Results: PASS
---