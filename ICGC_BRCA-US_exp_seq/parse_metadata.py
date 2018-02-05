import sys, gzip

inFilePath = sys.argv[1]
outFilePath = sys.argv[2]

# This dataset is pretty straightforward. It is already in the correct format. Just need to leave out certain columns and rename the first column.

columnsOfInterest = set(["submitted_donor_id", "donor_sex", "donor_vital_status", "disease_status_last_followup", "donor_age_at_diagnosis", "donor_age_at_last_followup", "donor_survival_time", "donor_interval_of_last_followup"])

with gzip.open(inFilePath, 'rb') as inFile:
    with gzip.open(outFilePath, 'wb') as outFile:
        inHeaderItems = inFile.readline().decode().rstrip("\n").split("\t")

        outFile.write("Sample\tVariable\tValue\n".encode())

        for line in inFile:
            lineItems = line.decode().rstrip("\n").split("\t")
            sample = lineItems[inHeaderItems.index("icgc_donor_id")]

            for column in columnsOfInterest:
                columnIndex = inHeaderItems.index(column)

                if column == "submitted_donor_id":
                    # This name is more user friendly
                    column = "TCGA_ID"
                else:
                    # Remove unnecessary prefix from any column names that have it
                    column = column.replace("donor_", "")

                value = lineItems[columnIndex]
		if value != "":
                	outItems = [sample, column, value]
                	outLine = "\t".join(outItems) + "\n"
               		outFile.write(outLine.encode())
