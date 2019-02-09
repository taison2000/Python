#!C:\Python34\python.exe
#!/Python34/python
#!/usr/bin/python

# -*- coding: utf-8 -*-

"""
 Function - eval
 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  eval( something )


"""

import os
import time

##-----------------------------------------------------------------------------
def myFunction( a, b):
  print( "Value of a is : ", a)
  print( "Value of b is : ", b)
  
  c = a+3
  
  return c
  
##-----------------------------------------------------------------------------
def main():
  
  c = eval( "myFunction ( 333, 'ok fine' ) #this is comment only" )
  ## Can NOT use the following. Notice the return value is from 
  # eval( " c = myFunction( 333, 'ok fine')" )  <== Invalid syntax
  # c = eval( "myFunction ( 333, 'ok fine')" )  <== Good
  
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
"""

