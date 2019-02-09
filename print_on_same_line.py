# -*- coding: utf-8 -*-

## ----------------------------------------------------------------------------
"""
  Python Topic : print on same line
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""

import os
import time

##-----------------------------------------------------------------------------

def format_para():
  i = 123; 
  j = 456;
  s = '{0}:{1}\n'.format('%-15s'%i, '%02X'%j)
  # {0} - First parameter of format
  # {1} - Second parameter of format
  
  return s

def PrintOnSameLine():
  """
  Somehow the command prompt don't show the print until last print
  """
  print ('installing ... |', end='')
  print ('\b/', end='') # \b == backspace
  time.sleep(1)
  print ('\b-', end='')
  time.sleep(1)
  print ('\b\\', end='')
  time.sleep(1)
  print ('\b|', end='')
  time.sleep(1)
  print ('\b/', end='')
  time.sleep(1)
  print ('\b-', end='')
  time.sleep(1)
  print ('\b\\', end='')
  time.sleep(1)
  print ('\b|', end='')
  return;
  
def main():
  format (1234, '5X')
  format (1234, '5x')
    
  # with leading '0'
  format (1234, '05X')
  format (1234, '05x')
  
  return;
 
if __name__ == "__main__":
  PrintOnSameLine()
  main()


##-----------------------------------------------------------------------------
"""
Resources:
 - 

"""

