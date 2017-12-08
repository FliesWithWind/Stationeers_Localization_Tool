# Stationeers_Localization_Tool
Simple tool that extracts new strings from "english.xml" file and after translation, it combines new localization XML file with your old translations.

# Installation
1. In order to run this script you need to install Python 2.7. You can get it here https://www.python.org/downloads/release/python-2714/

Be sure to add python to path during installation on Windows.

2. Download contents of this repo and place it in some folder. For example C:\Stationeers_translation

3. Place your XML localization file and new english.xml file in the same folder.

# Usage

## Extracting new strings
The easiest way to extract new strings for translation, is to change "polish.xml" to your localization file name in file "extract.bat" and run it.

You can also run the script from CMD/Terminal with command:
```
python transfer_localization.py -o polish.xml
```
or
```
python.exe transfer_localization.py -o polish.xml
```

This will create a new file called "newstrings.xml" containing all new strings you need to translate.

## Extracting new strings
The easiest way to combine evrything, is to change "polish.xml" to your localization file name in file "combine.bat" and run it.

You can also run the script from CMD/Terminal with command:
```
python transfer_localization.py -o polish.xml -c
```
or
```
python.exe transfer_localization.py -o polish.xml -c
```

To check avalible parameters run:
```
python transfer_localization.py -h
```
