import sys, gzip
import numpy as np
from io import StringIO

inFilePath = sys.argv[1]
outFilePath = sys.argv[2]

missingTerms = set(["[Not Applicable]", "[Not Available]", "[Not Evaluated]", "[Completed]", "[Unknown]", "[Discrepancy]", "[Not Reported]"])

def standardizeMissingValues(values):
    standardized = []
    for value in values:
        isMissing = False
        for missingTerm in missingTerms:
            if missingTerm in value:
                standardized.append("NA")
                isMissing = True
                break

        if not isMissing:
            standardized.append(value)

    return standardized

def shouldKeepColumn(values):
    numNonMissing = [value for value in values if value != "NA"]
    return len(numNonMissing) > 0

with gzip.open(inFilePath, 'r') as inFile:
    with open(outFilePath, 'a') as outFile:
        headerList = inFile.readline().decode().rstrip("\n").split("\t")
        sampleIDs = headerList[3:]

        for line in inFile:
            lineList = line.decode().rstrip("\n").split("\t")
            variableName = lineList[0]
            values = standardizeMissingValues(lineList[3:])

            if not shouldKeepColumn(values):
                continue

            # This variable has some values that are inconsistent, so ignoring this variable for now
            if variableName in ["chemo_concurrent_fractions_total", "cyto_abnormality_type_other", "her2_and_cent17_scale_other", "hpv_types_other", "i_131_radiation_subsequent_tx", "new_tumor_event_melanoma_count", "radiation_therapy_xrt_dose"]:
                continue

            for i in range(len(sampleIDs)):
                #sampleID = sampleIDs[i][:15]
                sampleID = sampleIDs[i]
                value = values[i]

                #This variable is giving us problems because it has a string value mixed in with numbers,
                #so we'll list it as missing for now.
                if variableName == "cent17_copy_number" and value == "polisomy":
                    value = "NA"

                outFile.write("{}\t{}\t{}\n".format(sampleID, variableName, value))
