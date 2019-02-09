#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
 RE - Regular Expression
 ~~~~~~~~~~~~~~~~~~~

  import re
  re.match('hel', 'hello world', re.I)  re.I = Case insensitive
    
"""

## ----------------------------------------------------------------------------

import os
import time
import re


# -----------------------------------------------------------------------------
# match - start from the begining
#   Result return a match object or 'None' if no match
# -----------------------------------------------------------------------------
def re_match():
  m = re.match("hel", 'hello world')   # matched
  print (m)
  if (m != None):
    print ("Found match :", m.group(0)) # match pattern ?

# Case sensitive 
  print("\nmatch 'hello world' with pattern 'HEl'")
  print("Case sensitive by default, no match")
  m = re.match("HEl", 'hello world')   # matched
  print (m)
  if (m != None):
    print ("Found match :", m.group(0)) # match pattern ?
    
# Case insensitive
  print("\nmatch 'hello world' with pattern 'HEl'")
  print("Set case insensitive flag(I), should have match!")
  m = re.match("HEl", 'hello world', re.I)   # matched
  print (m)
  if (m != None):
    print ("Found match :", m.group(0)) # match pattern ?
    
# Pattern not match the begining
  print("\nmatch 'hello world' with pattern 'el'")
  print("no match, because string not start with 'e'")
  m = re.match("el", 'hello world')   # no match, because string not start with 'e'
  print (m)
  if (m != None):
    print (m.group(0))

  print()


# -----------------------------------------------------------------------------
# search 
#   Scan through string looking for a match to the pattern, 
#    returning a match object, or None if no match was found.
# -----------------------------------------------------------------------------
def re_search():
  re_m = re.search("hel", 'hello world')   # matched
  print (re_m)
  if (re_m != None):
    print ("Found search :", re_m.group(0)) # match pattern ?

  re_m = re.search("el", 'hello world')   # still match
  print (re_m)
  if (re_m != None):
    print (re_m.group(0))

  print ("\nmultiple search result")
  re_m = re.search("el", 'hello world, hello kitty')   # still match
  print (re_m)
  if (re_m != None):
    print (re_m.group(0))

# -----------------------------------------------------------------------------
# Main program
# -----------------------------------------------------------------------------
def main():
# This is the main function
  print ("----- match function demo -----")
  re_match()
  print ("----- search function demo -----")
  re_search()

# -----------------------------------------------------------------------------
# Code entry
# -----------------------------------------------------------------------------
if __name__ == "__main__":
  main()
  #msg = main()
  #print(msg)
  #mainloop()


"""
  Note: 
    - No ++ or --, use a+=1 or a-=1 
    - print ("Variable %d", %Val)
      print ("Variable %d %d", % (Val1, Val2))

  

"""
