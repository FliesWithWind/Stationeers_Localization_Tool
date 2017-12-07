# Stationeers_Localization_Tool
Simple tool that combines new localization XML file with your old translations.

# Installation
1. In order to run this script you need to install Python 2.7. You can get it here https://www.python.org/downloads/release/python-2714/

2. Download contents of this repo and place it in some folder. For example C:\Stationeers_translation

3. Place your XML localization file and new english.xml file in the same folder.

# Usage

The easiest way to run it is to change "polish.xml" to your localization file name in file "transfer.bat" and run it.

You can also run the script from CMD/Terminal with command:
python transfer_localization.py -o polish.xml
or
python.exe transfer_localization.py -o polish.xml

To check avalible parameters run:
python transfer_localization.py -h
