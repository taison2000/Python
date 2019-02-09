#!C:\Python34\python.exe
#!/Python34/python
#!/usr/bin/python
# -*- coding: utf-8 -*-


"""
 Module - pprint
 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  - Includes in Python package
"""

## --- Methods ---
"""
#------------------------------------------------------------------------------
 - pprint.PrettyPrinter()
 - pprint.isreadable()
 - pprint.isrecursive()
 - pprint.pformat()
 - pprint.pprint()
 - pprint.saferepr()
#------------------------------------------------------------------------------
"""

## --- Attribute ---
"""
Note : 
 usage : pprint.Attribute
 - .
 - .
 - .
"""
 
## ----------------------------------------------------------------------------
import os
import time
import pprint

## ----------------------------------------------------------------------------
def method_pprint():
  """
   - < Automate The Boring Stuff With Python > Page-111
  """
  message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
  count = {}
  for character in message:
    count.setdefault(character, 0)
    count[character] = count[character]+1
    
  pprint.pprint( count )
  return;




# -----------------------------------------------------------------------------
# Main program - This is the main function
# -----------------------------------------------------------------------------
def main():
  method_pprint()
  return;
  
# -----------------------------------------------------------------------------
# Code entry
# -----------------------------------------------------------------------------
if __name__ == "__main__":
	main()



## ----------------------------------------------------------------------------
## Resource
## ----------------------------------------------------------------------------
"""
 -
 -
  
"""

## ----------------------------------------------------------------------------
"""
  Note: 
    - No ++ or --, use a+=1 or a-=1 
    - print ("Variable %d", %Val)
      print ("Variable %d %d", % (Val1, Val2))



"""

