import csv
import os
import sys
import xmltodict

def parse_rule(rule, line=[]):
    new_line = line.copy()
    new_line.append(rule["version"])
    new_line.append(rule["title"])
    new_line.append(rule["description"])
    new_line.append(rule["fixtext"]["#text"])
    new_line.append(rule["check"]["check-content"])
    csvfile_writer.writerow(new_line)

def parse_group(group, line=[]):
    new_line = line.copy()
    new_line.append(group["title"])
    if "Rule" in group.keys():
        if "@id" in group["Rule"]:
            parse_rule(group["Rule"], new_line)
        else:
            for r in group["Rule"]:
                parse_rule(r, new_line)

if len(sys.argv) == 2:
    input_xmlfile=sys.argv[1]
    output_csvfile=os.path.splitext(input_xmlfile)[0]+'.csv'

    with open(input_xmlfile) as xmlfile:
        xml = xmltodict.parse(xmlfile.read())

    csvfile = open(output_csvfile,'w',encoding='utf-8')
    csvfile_writer = csv.writer(csvfile)

    csvfile_writer.writerow(["Group Title","Rule Version","Rule Title", "Rule Description", "Rule Fix Text", "Rule Check"])

    for group in xml["Benchmark"]["Group"]:
        parse_group(group)
else:
    print("Usage: ")
    print("   " + sys.argv[0] + " stig_xml_file.xml")

