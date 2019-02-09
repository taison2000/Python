#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
  Python
  ~~~~~~~~~~~

"""

import os
import time
import _thread

def hello(num):
  print('Hello from thread %s\n' % num)
  return

def FunctionWithoutArgument():
  for i in range(60):
    print (i)
    time.sleep(0.1)
  return;
  
# -----------------------------------------------------------------------------
# Main program - This is the main function
# -----------------------------------------------------------------------------
def main():
  _thread.start_new_thread(hello, (0,))
  _thread.start_new_thread(hello, (1,))
  _thread.start_new_thread(hello, (2,))
  _thread.start_new_thread( FunctionWithoutArgument, () ) # Function with no argument
  
  
# -----------------------------------------------------------------------------
# Code entry
# -----------------------------------------------------------------------------      
if __name__ == "__main__":
	main()


"""
  Note: 
    - No ++ or --, use a+=1 or a-=1 
    - print ("Variable %d", %Val)
      print ("Variable %d %d", % (Val1, Val2))

  

"""


## ----------------------------------------------------------------------------
## ----- Multi Thread -----
## ----------------------------------------------------------------------------
"""
https://code.google.com/p/pyloadtools/wiki/CodeTutorialMultiThreading

  


"""