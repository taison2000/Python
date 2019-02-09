#!C:\Python34\python.exe
#!/Python34/python
#!/usr/bin/python
# -*- coding: utf-8 -*-


"""
 Module - shutil
 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  - Utility functions for copying and archiving files and directory trees.
  - Includes in Python package
  - 

"""

## --- Methods ---
"""
#------------------------------------------------------------------------------
 - shutil.chown()
 - shutil.copy()
 - shutil.copy2()
 - shutil.copyfile()
 - shutil.copyfileobj()
 - shutil.copymode()
 - shutil.copystat()
 - shutil.copytree()
 - shutil.disk_usage()
 - shutil.get_archive_formats()
 - shutil.get_terminal_size()
 - shutil.get_unpack_formats()
 - shutil.ignore_patterns()
 - shutil.make_archive()
 - shutil.move()
 - shutil.register_archive_format()
 - shutil.register_unpack_format()
 - shutil.rmtree()
 - shutil.unpack_archive()
 - shutil.unregister_archive_format()
 - shutil.unregister_unpack_format()
 - shutil.which()
"""

## --- Attribute ---
"""
Note : 
 usage : shutil.Attribute
 - .Error
 - .ExecError
 - .SameFileError
 - .SpecialFileError
"""

## ----------------------------------------------------------------------------

import os
import time
import shutil

## ----------------------------------------------------------------------------
def method_copyfile():
    """
    Put a module method here
    """
    shutil.copyfile( src, dst )

    # copy a file named "test_control.py" to "dst_text.txt"
    shutil.copyfile("test_control.py", "dst_text.txt")

    return;


# -----------------------------------------------------------------------------
# Main program - This is the main function
# -----------------------------------------------------------------------------
def main():
    method_Name()
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


## ----------------------------------------------------------------------------
## Resource
## ----------------------------------------------------------------------------
"""

  
  
"""

