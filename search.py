description = """
                    [ Search ]  

    This Program searches for a file in Directories.
Displays filename containing the word/Search_Phrase if exists.

    Usage:
        python search.py SEARCH_PHRASE --METHODS
"""

from os import walk, getcwd, listdir, system
from fnmatch import fnmatch
from time import sleep
from sys import argv, exit

def disp_avail_args():
    print("=" * 55)
    print("""
            AVAILABLE ARGUMENTS
            ====================

        -s / --simple : SIMPLE SEARCH
        -----------------------------
    [Searches file in Current Working Directory]

        -d / --deep   : DEEP SEARCH
        ----------------------------
    [Searches file in all files and folders]
    
        -c / --crawl  : DIRECTORY CRAWLER
        ---------------------------------
  [Searches file by crawling through all directories]
    (root = current working directory) ["Default"]
""")

    print("=" * 55)

def matched(word,file):
    # If word / search phrase contains wilcard characters..
    # use fnmatch function else traditional substring in string

    if "?" in word or "*" in word:
        return fnmatch(file,word.lower())
    return word in file

def crawl_search(word):
    # Crawls through directories
    # Displays filename along with path if found 
    # returns number of files found

    count = 0 # for counting number of files found
    for root,dirs,files in walk(getcwd()):
        for file in files:
            if matched(word.lower(),file.lower()):
                count += 1
                print("\n[FOUND] " + file)
                print("[PATH]",root)
    return count                

def simple_search(word):
    # Searches in Current Working Directory 
    # Without going into subdirectories
    # Displays filename if found 
    # returns number of files found

    count = 0 # for counting number of files found

    for file in listdir(getcwd()):
        if matched(word.lower(),file.lower()):
            count += 1
            print(file)
    return count            

def deep_search(word):
    # Searches in Files while crawling
    # Yet to be implemented!

    print("\nDeep Search Coming Soon!\nTry a different method for now..\n")
    exit()

def found(word = "", method = 1):    
    # Heart of the script

    # Links search phrase with methods..

    method_names = {
    1: "Directory Crawler",
    2: "Simple Search",
    3: "Deep Search"
    }

    print("="*30)
    print ("\nUsing Method {} [{}]".format(method,method_names[method]))
    print("="*30)

    methods = {
    1: crawl_search,
    2: simple_search,
    3: deep_search
    }

    count = methods[method](word)

    print("\n\t--> {} files found!\n".format(count))
    print("\n**Search Finished!**\n".upper())
    return count

method = 1 #default (Crawler)
word = "" # Search Phrase

for arg in argv:
    # Custom Argument Parser

    if arg[0] == "-":
    
        if arg in ["-c", "--crawl"]:
            # default
            method = 1

        elif arg in ["-s", "--simple"]:
            method = 2

        elif arg in ["-d", "--deep"]:
            method = 3

        else:
            print('\n\nInvalid Argument!')
            disp_avail_args()
            exit()

    elif arg in ["/?", "-h", "--help"]:
            system("cls||clear") # Clears the screen
            print(description)
            disp_avail_args()
            exit()

    elif arg not in ["search_.py","search"] :
        word = arg

system("cls||clear") # Clears the screen

try:
    while True:
        print('-' * 30)

        while not word:
            word = input("\n\nEnter File to be Searched or Press Ctrl + C to Exit\n\nSearch Phrase: ")
            
            if not word :
                print("\n[ERROR] Searched Phrase can't be empty!")
                sleep(2)
            else:
                break

        print("\n**Search Started!**".upper())
        
        c = found(word,method)

        if c < 0:
            for t in range(3,0,-1):
                print("Enter again in {} seconds...".format(t) , end = "\r")
                sleep(1)
                system("cls||clear")
        
        word = ""
        


except KeyboardInterrupt:
    print("\nSearch Terminated!")
