#!/bin/bash


function downloadData {
#:FUnction accepts the URL as a parameter
	url="$1"
	
	fileName="$(basename $url)"

#Check to see if the file has been downloaded already. If not, download it.
	if [ ! -f "$fileName" ]
	then 
		curl -o "$fileName" -L "$url"
	fi
}


#This will download the file using the function above

downloadData "ftp://anonymous:guest@caftpd.nci.nih.gov/pub/OCG-DCC/CTD2/UCSF-2/Gene_Expression_Profiling_Mouse/UCSF_Weiss_CTDD_data_submission.zip"

unzip UCSF_Weiss_CTDD_data_submission.zip -d tmp
 
