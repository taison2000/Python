#!/usr/bin/python
# -*- coding: utf-8 -*-
#
#
"""
  Multithread framework

"""

import os
import time
#import _thread
from threading import Thread

THREADS = 3

class MyThread( Thread ):
  def __init__(self, i):
    Thread.__init__(self)
    self.i = i
    
  def run(self):
    while True:
      print('hello from thread # %i' % self.i)
      time.sleep(.25+self.i)
      
class ThreadManager:
  def __init__(self):
    pass
  
  def start( self, threads ):
    thread_refs = []
    for i in range( threads ):
      t = MyThread(i)
      t.daemon = True
      print( 'starting thread %i' % i)
      t.start()
    for t in thread_refs:
      t.join()

  
# ------------------------------------------------------------------------------
# Main program - This is the main function
# ------------------------------------------------------------------------------
def main():
  manager = ThreadManager()
  manager.start( THREADS )
  
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