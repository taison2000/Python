#!C:\Python34\python.exe
#!/Python34/python
#!/usr/bin/python

# -*- coding: utf-8 -*-

## ----------------------------------------------------------------------------
"""
  import module from sub-directory
  ~~~~~~~~~~~~~~~~~~~~~~
  from subdirectoryName.moduleName import myUserFunction
  - may need to have __init__.py empty file in the subdirectory.

"""

import os
import time

## import module from subdirectory "classes"
from classes.myFunctions import myPrint, add_two_num

# -----------------------------------------------------------------------------
# Main program - This is the main function
# -----------------------------------------------------------------------------
def main():
  myPrint();
  print( add_two_num(34, 394) )
  
  return;

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


# -----------------------------------------------------------------------------
# What is __init__.py for in a Python source directory?
# -----------------------------------------------------------------------------
"""
 The __init__.py files are required to make Python treat the directories as 
 containing packages; this is done to prevent directories with a common name, 
 such as string, from unintentionally hiding valid modules that occur 
 later on the module search path. 
 In the simplest case, __init__.py can just be an empty file, 
 but it can also execute initialization code for the package or 
 set the __all__ variable, described later.
"""

## ----------------------------------------------------------------------------
# Resources:
"""
- http://stackoverflow.com/questions/448271/what-is-init-py-for

"""

'''
3 single quote string
'''
