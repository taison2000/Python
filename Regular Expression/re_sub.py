#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
  Python
  ~~~~~~~~~~~
"""

import os
import time
import re   # import the Regular Expression module

# ------------------------------------------------------------------------------
# re.sub
# ------------------------------------------------------------------------------
def sub_01():
# ------------------------------------------------------------------------------
    # re.sub (pattern, repl, string, max=0)
    #   Function returns modified string
    # ------------------------------------------------------------------------------
    line = "Human are smarter than dogs, human are smarter than dogs, human are smarter than dogs, human are smarter than dogs, human are smarter than dogs ";
    print("\n")
    print ("Original string: ")
    print (line, '\n')
    print("Search for 'human' and sub it with 'cats' ")

    # 
    newStr = re.sub( r'human', 'cats', line)

    if newStr:
        print ("The new modified string is:\n", newStr)
        #print ("newStr.group() : ", newStr.group())
        #print ("newStr.group(1) : ", newStr.group(1))
        #print ("newStr.group(2) : ", newStr.group(2))
    else:
        print("No match!!")

    return newStr

def sub_02():
    s = "this the with string"
    ss = re.sub('t', 'blah', s) # replace 't' with 'blah'
    return ss


# ------------------------------------------------------------------------------
# Remove  non-digits
#    including white space
# ------------------------------------------------------------------------------
def removeNonDigits(str):
    #newStr = re.sub( r'\D', '', str)
    newStr = re.sub( r'\D', '', str, 10)   # the 4th variable specify the number of sub
    return newStr

def removeDigits():
    numberOfSubstitute = 2
    string = "here is mix 45 digits 1 with 2 3 9 chars 1"
    new_string1 = re.sub( r'\d', '', string, numberOfSubstitute)   # the 4th variable specify the number of sub
    # 'here is mix  digits 1 with 2 3 9 chars 1  '   -> replace 2 digits (4 and 5)
    
    numberOfSubstitute = 5
    new_string2 = re.sub( r'\d', '', string, numberOfSubstitute)
    # 'here is mix  digits  with   9 chars 1  ' -> replace 5 digits (4, 5, 1, 2, 3)
    
    
# ------------------------------------------------------------------------------
# Main program
# ------------------------------------------------------------------------------
def main():
    # This is the main function

    print(removeNonDigits("here is mix 45 digits 1 with 2 3 9 chars 1  "))


# ------------------------------------------------------------------------------
# Code entry
# ------------------------------------------------------------------------------
if __name__ == "__main__":
    main()
    #msg = main()

"""
re.match (pattern, string, flags=0)
  Pattern : This is the regular expression to be matched
  String  : This is the string, which would be searched to match the pattern at the begining of string
  Flags   : Specify different flags using bitwise OR(|). These are modifiers, which are listed in the table below

    Modifier Description
    -----------------------------------------------------------------------------------------------
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
