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
def myFunction( a, b):
	print("a is :", a)
	print("b is :", b)
	return a
  x = [1, 2, 3]
  y = [4, 5, 6]
  
  zipped = zip(x, y)  # zipped == <zip object at 0x02E45580>
  
  type (zipped)   #-> <class 'zip'>
  
  list( zipped )  #-> [(1, 4), (2, 5), (3, 6)]
  
  x2, y2 = zip(*zip(x, y))
  # x2==(1, 2, 3) -> tuple
  # y2==(4, 5, 6) -> tuple
  
  x==list(x2) #-> True
  y==list(y2) #-> True
  
  return s
  
##-----------------------------------------------------------------------------
def main():
  exec( "c = myFunction( 333, 'ok fine') #this is comment only" )
  
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

