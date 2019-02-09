#!C:\Python34\python.exe
#!/Python34/python
#!/usr/bin/python

# -*- coding: utf-8 -*-

"""
 Function - locals
 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  locals( ) - Returns a dictionary


"""

import os
import time

##-----------------------------------------------------------------------------
 def localVariables():
	a=1
	b='hello'
  
	print( locals() ) # 
  # => {'b': 'hello', 'a': 1}
	
  return

def localVariables_01():
	a=1
	b='hello'
	
	c = locals()
  # c=={'b': 'hello', 'a': 1}
	
	print( locals() ) 
  #=> {'c': {...}, 'b': 'hello', 'a': 1}
  ## notice the variable 'c' from locals()
  
	return
  
##-----------------------------------------------------------------------------
def main():
  a = 123
  print ('%05s', a) # <- Leading empty spaces
  print ('%05s', a) # <- Leading empty spaces
  
  # with leading '0'
  format( 1234, '05X' )
 
if __name__ == "__main__":
	main()


##-----------------------------------------------------------------------------
"""
Resources:
 - 

"""
