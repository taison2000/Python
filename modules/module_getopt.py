#!C:\Python34\python.exe
#!/Python34/python
#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
 Module - getopt
 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  - installation : "pip install pyautogui"

"""

## ----------------------------------------------------------------------------

import os
import time
import sys, getopt  # use argparse instead, it is newer

# getopt, optparse, argparse

## ----------------------------------------------------------------------------
def method_methName():
    """
    Put a module method here
    """
    pass
    return;


# -----------------------------------------------------------------------------
# Main program - This is the main function
# -----------------------------------------------------------------------------
def main( argv ):
    inputfile = ''
    outputfile = ''
    try:
        opts, args = getopt.getopt(argv, "hi:o:",["ifile=","ofile="])
    except getopt.GetoptError:
        print( 'test.py -i <inputfile> -o <outputfile>' )
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print( 'test.py -i <inputfile> -o <outputfile>' )
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg
    print( 'Input file is "', inputfile )
    print( 'Output file is "', outputfile )

    #method_Name()
    return;

# -----------------------------------------------------------------------------
# Code entry
# -----------------------------------------------------------------------------      
if __name__ == "__main__":
    main(sys.argv[1:])

"""
  Note: 
    - c:\python34\python.exe module_getopt.py -h
    - c:\python34\python.exe module_getopt.py -i "Input File.txt" -o "Output file.txt"
    

"""


## ----------------------------------------------------------------------------
## Resource
## ----------------------------------------------------------------------------
"""

  
  
"""

