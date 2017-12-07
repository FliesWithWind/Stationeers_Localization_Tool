import xml.etree.ElementTree as ET
import argparse


#parse command line input
PARSER = argparse.ArgumentParser(description=
								"""
								This script imports tranlsated strings from your old XML localization file.
								ex. "python transfer_localization.py -o polish.xml -n english.xml"
								""")
PARSER.add_argument('-o', '--oldfile', help=
					"""
					Old localization xml file.
					"""
					, required=True)
PARSER.add_argument('-n', '--newfile', help=
					"""
					New english localizatiion xml file.
					"""
					, default='english.xml', required=False)

ARGS = PARSER.parse_args()

new = ET.parse(ARGS.newfile)
old = ET.parse(ARGS.oldfile)
newroot = new.getroot()
oldroot = old.getroot()

#Copying language Name, Code and Font
oldname = oldroot.find('Name')
newname = newroot.find('Name')
newname.text = oldname.text
oldcode = oldroot.find('Code')
newcode = newroot.find('Code')
newcode.text = oldcode.text
oldfont = oldroot.find('Font')
newfont = newroot.find('Font')
newfont.text = old.text

#Importing 
for record_reagent in oldroot.iter('RecordReagent'):
	oldkey = record_reagent.find('Key').text
	oldvalue = record_reagent.find('Value').text
	for new_record_reagent in newroot.iter('RecordReagent'):
		newkey = new_record_reagent.find('Key').text
		newvalue = new_record_reagent.find('Value').text
		value = new_record_reagent.find('Value')
		
		if newkey == oldkey:
			value.text = oldvalue
			if record_reagent.find('Unit'):
				unit = new_record_reagent.find('Unit')
				oldunit = record_reagent.find('Unit').text
				unit.text = oldunit


for record in oldroot.iter('Record'):
	oldkey = record.find('Key').text
	oldvalue = record.find('Value').text
	for new_record in newroot.iter('Record'):
		newkey = new_record.find('Key').text
		newvalue = new_record.find('Value').text
		value = new_record.find('Value')
		if newkey == oldkey:
			value.text = oldvalue

newroot.set('xmlns:xsi', 'http://www.w3.org/2001/XMLSchema-instance')
newroot.set('xmlns:xsd', 'http://www.w3.org/2001/XMLSchema')

new.write('output.xml',encoding="utf-8", xml_declaration=True)