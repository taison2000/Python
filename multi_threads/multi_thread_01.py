#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
  Python
  ~~~~~~~~~~~

"""

import os
import time
#import _thread
from threading import Thread

class MyThread( Thread ):
  def run(self):
    print('hello from thread %s\n' % self.name)

  
# ------------------------------------------------------------------------------
# Main program - This is the main function
# ------------------------------------------------------------------------------
def main():
  for i in range(3):
    my_thread = MyThread()
    my_thread.name = i
    my_thread.start()
  return
  
# ------------------------------------------------------------------------------
# Code entry
# ------------------------------------------------------------------------------      
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