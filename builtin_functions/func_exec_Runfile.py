#!C:\Python34\python.exe
#!/Python34/python
#!/usr/bin/python

# -*- coding: utf-8 -*-

"""
 Function - exec
 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  exec( something )


"""

import os
import time

##-----------------------------------------------------------------------------
def execRunFile( ):
  """
  Run a file with Python code.
  """
  fo = open("func_exec_Runfile_01.txt", 'r')
  data = fo.read()
  fo.close()
  print("data type ", type(data))
  
  exec( data )
  
  return 
  
##-----------------------------------------------------------------------------
def main():
  #exec( "c = myFunction( 333, 'ok fine') #this is comment only" )
  execRunFile()
  
if __name__ == "__main__":
	main()


##-----------------------------------------------------------------------------
"""
Resources:
 - http://stackoverflow.com/questions/2220699/whats-the-difference-between-eval-exec-and-compile-in-python

"""


##-----------------------------------------------------------------------------
## NOTE: 'eval' vs 'exec'
"""
 eval( " c = myFunction( 333, 'ok fine')" ) <== Invalid Syntax
 exec( " c = myFunction( 333, 'ok fine')" ) <== Good
 
 eval('Total=12+36')   <== Invalid Syntax => 
 Total = eval('12+36') <== Good
 exec('Total=12+36')   <== Good
 Total=exec('12+36')   <== Good Total==None
"""

## eval returns result
#   Total = eval('12+36')
## exec does not return anything.
#   exec('Total=12+36')

