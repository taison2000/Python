#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
 RE - Regular Expression
 ~~~~~~~~~~~~~~~~~~~

  import re
  
  re.compile   - 
  re.error     - 
  re.escape    - 
  re.findall   - 
  re.finditer  - 
  re.fullmatch - 
  re.match     - Only match from beginning of string
  re.purge     - 
  re.search    - Search anywhere in the string
  re.split     - 
  re.sub       - 
  re.subn      - 
  re.template  - 
  
  
  re.match('hel', 'hello world', re.I)  re.I = Case insensitive
    
"""

## ----------------------------------------------------------------------------
import os
import time
import re   # import the Regular Expression module

def summary():
    line = "Cats are smarter than dogs"
    matchObj = re.match(r'(.*) are (.*?).*', line, re.M | re.I)
    
    # symbol(^) : search from beginning
    matchObj = re.search('^Cats', line) # found
    matchObj = re.search('^are', line)  # NOT found
    matchObj = re.search('are', line)   # found
    
    # case insensitive
    matchObj = re.search('ARE', line, re.I) # found
    matchObj = re.search('ARE', line)   # NOT found
    
    return
    
# -----------------------------------------------------------------------------
# Main program
# -----------------------------------------------------------------------------
def main():
    # match
    match1 = re.match("hel", "hello world")
    match2 = re.match("wor", "hello world")
    
    # search
    search1 = re.search("hel", "hello world")
    search2 = re.search("wor", "hello world")
    
    # sub
    sub1 = re.sub("cat", "dog", "this cat is a happy cat. What about capital Cat?")
    sub2 = re.sub("", "hello world")
    
    return


# -----------------------------------------------------------------------------
# Code entry
# -----------------------------------------------------------------------------
if __name__ == "__main__":
    main()

## ----------------------------------------------------------------------------
"""
re.search (pattern, string, flags=0)
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

## ----------------------------------------------------------------------------
"""
  Note: 
    - No ++ or --, use a+=1 or a-=1 
    - print ("Variable %d", %Val)
      print ("Variable %d %d", % (Val1, Val2))



"""
