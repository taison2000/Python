#!C:\Python34\python.exe
#!/Python34/python
#!/usr/bin/python
# -*- coding: utf-8 -*-


"""
 Module - pywinauto
 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  - installation : "pip install pywinauto"
  - Supported
    . Win32(backend='win32') : MFC, VB6, VCL
    . MS UI Automation(backend='uia') : WinForms, WPF, Store apps, Qt, browsers
  - Not Supported
    . Java AWT/Swing
    . GTK+
    . Tkinter
"""

## --- Methods ---
"""
#------------------------------------------------------------------------------
 - logging.BufferingFormatter.format()
 - logging.BufferingFormatter.formatFooter()
 - logging.BufferingFormatter.formatHeader()
 - logging.FileHandler()
 - logging.Filter()
 - logging.Filter.filter()
 - 
 - 
 - 
 - 
 - 
 - 
#------------------------------------------------------------------------------
"""

## --- Attribute ---
"""
Note : 
 usage : logging.Attribute
 - .BASIC_FORMAT
 - .CRITICAL
 - .DEBUG
 - .ERROR
 - .FATAL
 - .INFO
 - .
 - .
 - .
"""

## ----------------------------------------------------------------------------
import os
import time
import pywinauto

## ----------------------------------------------------------------------------
def method_Name():
    """
    Put a module method here
    """
    pass
    return;
    
def demo_run_Notepad():
    from pywinauto.application import Application
    app = Application(backend="uia").start("notepad.exe")
    #app.UntitledNotepad.type_keys("%FX")   ## "File" -> "Exit" ??
    app.UntitledNotepad.type_keys("Hello World")

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



## ----------------------------------------------------------------------------
## Resource
## ----------------------------------------------------------------------------
"""
 - https://pywinauto.readthedocs.io/en/latest/
 - 
 - 
"""

## ----------------------------------------------------------------------------
"""
  Note: 
    - No ++ or --, use a+=1 or a-=1 
    - print ("Variable %d", %Val)
      print ("Variable %d %d", % (Val1, Val2))


"""

