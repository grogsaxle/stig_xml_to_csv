# STIG XML to CSV

Needed a easy way to track hardening tasks that were generated from the [Ubuntu 20.04 STIG](https://ncp.nist.gov/checklist/992).  While the content is great, as an XML file, immediate consumption is a challenge.  Good for computers, bad for humans.  

Introducing stig_xml_to_csv.py.  It parses the STIG XML for Groups and Rules, and puts them into a CSV file. 

   Group Title,Rule Version,Rule Title,Rule Description,Rule Fix Text,Rule Check

## Usage

    python3 -m venv env
    source ./env/bin/activate
    pip3 install xmldict

    python3 stig_xml_to_csv.py U_CAN_Ubuntu_20-04_LTS_STIG_V1R2_Manual-xccdf.xml 



