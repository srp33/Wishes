<h1><center>BiomarkerBenchmark_GSE15296</center></h1>
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

&#9989;	test_data.tsv contains enough test cases (8; min: 8)

&#9989;	test_metadata.tsv contains enough unique samples to test

&#9989;	test_metadata.tsv contains enough test cases (8; min: 8)

#### Results: PASS
---

### First 5 columns and 5 rows of data.tsv.gz:

|	Sample	|	ENSG00000000003	|	ENSG00000000005	|	ENSG00000000419	|	ENSG00000000457	|
|	---	|	---	|	---	|	---	|	---	|
|	GSM382248	|	-0.123477328823529	|	-0.18570138375	|	1.97677030444444	|	1.049999476875	|
|	GSM382249	|	-0.189238480588235	|	-0.19206116	|	2.17388854444444	|	1.0877007365625	|
|	GSM382250	|	-0.175121237058824	|	-0.11864399	|	0.913606556666667	|	0.6683048721875	|
|	GSM382251	|	-0.121842637647059	|	-0.1708570525	|	1.89917884222222	|	1.226143414375	|

**Columns: 20025 Rows: 75**

---
### "data.tsv.gz" Test Cases (from rows in test file). . .

&#9989;	First column of file is titled "Sample"

&#9989;	Row 1: Success

&#9989;	Row 2: Success

&#9989;	Row 3: Success

&#9989;	Row 4: Success

&#9989;	Row 5: Success

&#9989;	Row 6: Success

&#9989;	Row 7: Success

&#9989;	Row 8: Success

#### Results: PASS
---
### First 3 columns and 5 rows of metadata.tsv.gz:

|	Sample	|	Variable	|	Value	|
|	---	|	---	|	---	|
|	GSM382248	|	phenotype	|	Acute Kidney Rejection	|
|	GSM382248	|	subtype	|	IA	|
|	GSM382249	|	phenotype	|	Acute Kidney Rejection	|
|	GSM382249	|	subtype	|	IB	|

**Columns: 3 Rows: 149**

---
### "metadata.tsv.gz" Test Cases (from rows in test file). . .

&#9989;	First column of file is titled "Sample"

&#10060;	Row 1: Fail
- "GSM38055	Alcohol_Consumption	Yes" is not found.

&#10060;	Row 2: Fail
- "GSM38055	Years_of_Tobacco_Use	46-50" is not found.

&#10060;	Row 3: Fail
- "GSM38061	Alcohol_Consumption	No" is not found.

&#10060;	Row 4: Fail
- "GSM38061	Years_of_Tobacco_Use	11-15" is not found.

&#10060;	Row 5: Fail
- "GSM353939	Alcohol_Consumption	No" is not found.

&#10060;	Row 6: Fail
- "GSM353939	Years_of_Tobacco_Use	16-20" is not found.

&#10060;	Row 7: Fail
- "GSM353901	Alcohol_Consumption	No" is not found.

&#10060;	Row 8: Fail
- "GSM353901	Years_of_Tobacco_Use	41-45" is not found.

#### Results: **<font color="red">FAIL</font>**
---
### Making sure no commas exist in either file . . .

&#9989;	No Commas in metadata.tsv.gz

&#9989;	No Commas in data.tsv.gz

#### Results: PASS
---
### Comparing samples in both files . . .

&#9989;	Samples are the same in both "data.tsv.gz" & "metadata.tsv.gz"

#### Results: PASS

---
### Testing Directory after cleanup . . .

#### Results: PASS
---