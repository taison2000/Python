#!C:\Python34\python.exe
#!/Python34/python
#!/usr/bin/python

# -*- coding: utf-8 -*-

## ----------------------------------------------------------------------------
"""
  Python
  ~~~~~~~~~~~

"""

import os
import time

## ----------------------------------------------------------------------------
'''
# if acc_Globals_ProC is locate in the parent folder.
# here is how to import, add the path to PYTHONPATH first.
'''
import sys
sys.path.insert(0, '..')  # Insert path to the begining of PYTHONPATH
from acc_Globals_ProC import GetGlobals

sys.path.append('..')  # Append the parent path to the END of PYTHONPATH


# -----------------------------------------------------------------------------
# Main program - This is the main function
# -----------------------------------------------------------------------------
def main():
    pass

# -----------------------------------------------------------------------------
# Code entry
# -----------------------------------------------------------------------------
if __name__ == "__main__":
    main()




# -----------------------------------------------------------------------------
# Why (  if __name__ == "__main__":  )
# -----------------------------------------------------------------------------
"""
http://stackoverflow.com/questions/4383571/importing-files-from-different-folder-in-python



"""

'''
3 single quote string
'''

"""
  Note: 
    - No ++ or --, use a+=1 or a-=1 
    - print ("Variable %d", %Val)
      print ("Variable %d %d", % (Val1, Val2))

"""
