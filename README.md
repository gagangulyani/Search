# Search
Search for files more conveniently

## What it does

It looks for search phrase entered by the user in file names and displays the filename if it's in it.

## Usage

> python **search.py** [SearchPhrase] --arguments

### If executable version is in path
> **search** [SearchPhrase] --arguments

#### Example 
> **search** happyness **-c**

#### Note : It can be executed without any arguments aswell!

#### Arguments 
> **-s | --simple :**
Searches file in Current Working Directory

> **-c | --crawl** (DEFAULT)
Searches file by Crawling through all Directories

> **-d | --deep :** 
Searches file in all files and folders **(UnAvailable at the Moment)**

## In Windows 
### install pyinstaller using pip and run the following command
> pyinstaller --onefile -n search search.py
#### copy (from  dist directory) and paste this executable at a location and add it in PATH
