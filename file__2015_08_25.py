#!/usr/bin/python
# -*- coding: utf-8 -*-


"""
  File IO - No import is needed
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  
  - Mode
    'r' - Read (default)
    'w' - Write, clear out original content
    'x' - Create new file for write only; Error if file already exist
    'a' - Write, append to original content
    'b' - Binary mode
    't' - Text Mode (default)
    '+' - Open for update
    
    Examples:
    'w+b' - Binary write, clear original content
    'r+b' - 
    'r+'  - Both read and write.
    
    
  - File Attributes
    fo.name
    fo.closed
    fo.mode
    
  - File Method
    fo.close()
    fo.read()
    fo.seek(offset[, from]) - fo.seek(10, 0); fo.seek(0,2) - end of file
    fo.tell()
    fo.write - return number of char written
    
  
  Notes:
    1. Can have two fileobject to open the same file, can each work independently.
    
  
"""

import os
import time

# ------------------------------------------------------------------------------
# File Copy
#  - by using fo.read and fo.write
# ------------------------------------------------------------------------------
def fileCopy():
  fo_src = open("ptc.cfg", 'r')
  fo_dst = open("ptc_copy.cfg", 'w')
  readData = fo_src.read()
  fo_dst.write(readData)
  #print(readData)
  fo_src.close()
  fo_dst.close()

# ------------------------------------------------------------------------------
# File Open
#   fo = open(r'E:\Sam\Python\Examples_GerNin\ptc.cfg', 'r+')
# ------------------------------------------------------------------------------
def fileOpen():
  fo = open("ptc.cfg", 'r') # fo = file object (not file pointer like C)
  readData = fo.read()
  print(readData)
  fo.close()

# ------------------------------------------------------------------------------
# File attributes :
# -----------------------------------------------------------------------------
def fileAttributes():
  fp = open("Template.py", 'r')
  print ("Name of file : ", fp.name)
  print ("Closed or not : ", fp.closed)
  print ("Opening mode : ", fp.mode)
  #print ("Softspace flag : ", fp.softspace)
  
## ----------------------------------------------------------------------------
def fileSeek():
  # fo.seek(offset, whence)
  #   offset - position of read/write 
  #   whence - [optional, default=0]where to start the position
  #         0==begin of file
  #         1==current file pointer
  #         2==end of file
  
  fo.seek(15, 0)  # begin of file, offset to 15
  fo.seek(28, 1)  # from current file pointer, offset to 28 (Removed from Python 3.x)
  fo.seek(-3, 2)  # from end of file, move pointer back 3 pos (Removed in Python 3.x)
  fo.seek(0, 2)   # END OF FILE
  
  return;
  
  
  
# ------------------------------------------------------------------------------
# Main program
# ------------------------------------------------------------------------------
def main():
# This is the main function
  fileAttributes()
  fileOpen()
  fileCopy()
  time.sleep(1)

# ------------------------------------------------------------------------------
# Code entry
# ------------------------------------------------------------------------------      
if __name__ == "__main__":
	main()
  #msg = main()
  #print(msg)
  #mainloop()


"""
  Note: 
    - No ++ or --, use a+=1 or a-=1 
    - print ("Variable %d", %Val)
      print ("Variable %d %d", % (Val1, Val2))

  

"""
