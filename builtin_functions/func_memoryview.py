#!C:\Python34\python.exe
#!/Python34/python
#!/usr/bin/python

# -*- coding: utf-8 -*-

"""
 Function - memoryview
 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  print( something )


"""

import os
import time

##-----------------------------------------------------------------------------
def format_para():
  i = 123; 
  j=456
  s = '{0}:{1}\n'.format('%-15s'%i, '%02X'%j)
  # {0} - First parameter of format
  # {1} - Second parameter of format
  
  return s

##-----------------------------------------------------------------------------
def main():
  ba = b'\xff\xff\xc3<\x01\x00\t\x033\xab\xcd'
  
  v = memoryview(ba)
  type(v) # <class 'memoryview'>
  
  print( v[0] ) # 255
  print( v[1] ) # 255
  print( v[2] ) # 195
  print( v[3] ) # 60
  print( v[4] ) # 1
  print( v[5] ) # 0
  print( v[6] ) # 9
  print( v[7] ) # 3
  
  v[1:4]  # <memory at 0x05523420>
  
  bytes( v[3:6] ) # b'<\x01\x00'
  bytes( v[4:7] ) # b'\x01\x00\t'
  
 return
 
if __name__ == "__main__":
	main()


##-----------------------------------------------------------------------------
"""
Resources:
 - 

"""
