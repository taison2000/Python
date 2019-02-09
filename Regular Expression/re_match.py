#!C:\Python34\python.exe
#!/Python34/python
#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
 Regular Expression
 ~~~~~~~~~~~~~~~~~~~
  match - will only search from the begining.
"""

## ----------------------------------------------------------------------------
import os
import time
import re	# import the Regular Expression module

## ----------------------------------------------------------------------------
def Match_A_Digit():
    # Look at begining for a digit
    result = re.match("[0-9]", "8 is eight")

    # Look at begining for a digit either 4, 6 or 8, not 468
    result = re.match("[468]", "8 is eight")  # match found, span=(0,1) match='8'
    result = re.match("468", "8 is eight") # <- this will look for 468

    return

# -----------------------------------------------------------------------------
# Main program
# -----------------------------------------------------------------------------
def main():
    # This is the main function
    line = "Cats are smarter than dogs"
    matchObj = re.match( r'(.*) are (.*?) .*', line, re.M|re.I)

    if matchObj:
        print ("matchObj.group() : ", matchObj.group())     # 'Cats are smarter than dogs'
        print ("matchObj.group(1) : ", matchObj.group(1))   # 'Cats'
        print ("matchObj.group(2) : ", matchObj.group(2))   # 'smarter'
    else:
        print("No match!!")

    ## added one more group from previous match
    matchObj = re.match( r'(.*) are (.*?) (.*)', line, re.M|re.I)
    # matchObj.group()    # 'Cats are smarter than dogs'
    # matchObj.group(1)   # 'Cats'
    # matchObj.group(2)   # 'smarter'
    # matchObj.group(3)   # 'than dogs'

# -----------------------------------------------------------------------------
# Code entry
# -----------------------------------------------------------------------------
if __name__ == "__main__":
    main()

"""
re.match (pattern, string, flags=0)
  Pattern : This is the regular expression to be matched
  String  : This is the string, which would be searched to match the pattern at the begining of string
  Flags   : Specify different flags using bitwise OR(|). These are modifiers, which are listed in the table below

    Modifier Description
    ---------------------------------------------------------------------------------------------------
      re.I    Performs case-insensitive matching.
      re.L    Interprets words according to the current locale. 
                This interpretation affects the alphabetic group (\w and \W), 
                as well as word boundary behavior (\b and \B).
      re.M    Makes $ match the end of a line (not just the end of the string) and makes ^ match the
                start of any line (not just the start of the string).
      re.S    Makes a period (dot) match any character, including a newline.
      re.U    Interprets letters according to the Unicode character set. 
                This flag affects the behavior of \w, \W, \b, \B.
      re.X    Permits "cuter" regular expression syntax. It ignores whitespace (except inside a set []
                or when escaped by a backslash) and treats unescaped # as a comment marker.  
"""

"""
  Note: 
    - No ++ or --, use a+=1 or a-=1 
    - print ("Variable %d", %Val)
      print ("Variable %d %d", % (Val1, Val2))

  

"""
