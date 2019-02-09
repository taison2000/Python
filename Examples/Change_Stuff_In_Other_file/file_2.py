#!C:\Python34\python.exe
#!/Python34/python
#!/usr/bin/python
# -*- coding: utf-8 -*-

## ----------------------------------------------------------------------------
"""
  Python
  ~~~~~~~~~~~~~~~~~~~~~~

"""

import os
import time

import file_1

# -----------------------------------------------------------------------------
# Main program - This is the main function
# -----------------------------------------------------------------------------
def main():
  """
    Change a variable in other file.
  """
  print( "Print value from file_1.PrintValue()" )
  file_1.PrintValue()
  
  print(" Get value and print from here: ")
  v = file_1.GetValue()
  print( v )
  
  print( "Set value to 12345" )
  file_1.SetValue( 12345 )
  
  print( "Print value from file_1.PrintValue()" )
  file_1.PrintValue()
  
  print(" Get value and print from here: ")
  v = file_1.GetValue()
  print( v )

  return;


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



'''
3 single quote string
'''
