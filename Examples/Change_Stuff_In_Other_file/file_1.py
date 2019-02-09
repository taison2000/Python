#!C:\Python34\python.exe
#!/Python34/python
#!/usr/bin/python
# -*- coding: utf-8 -*-

## ----------------------------------------------------------------------------
"""
  Change global Variable in other file
  ~~~~~~~~~~~~~~~~~~~~~~

"""

import os
import time

global gValue1
gValue1=10

def SetValue( value ):
  global gValue1
  gValue1 = value
  return;
  
def GetValue():
  global gValue1
  return gValue1;

def PrintValue():
  global gValue1
  print( gValue1 );

# -----------------------------------------------------------------------------
# Main program - This is the main function
# -----------------------------------------------------------------------------
def main():
  """
  range()
  
  """

# -----------------------------------------------------------------------------
# Code entry
# -----------------------------------------------------------------------------
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




'''
3 single quote string
'''
