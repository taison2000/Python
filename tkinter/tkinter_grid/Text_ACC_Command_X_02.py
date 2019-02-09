#!/usr/bin/python
# Comment start with #


"""
#------------------------------------------------------------------------------
Text Widgets:
  Parameters
   - bg
   - bd
   - cursor
   - exportselection
   - font
   - fg
   - height
   - highlightbackground
   - highlightcolor
   - highligtthickness
   - insertbackground
   - insertborderwidth
   - insertofftime
   - insertontime
   - insertwidth
   - padx
   - pady
   - relief
   - selectbackgroud
   - selectborderwidth
   - spacing1 
   - spacing2 
   - spacing3 
   - state
   - tabs
   - width
   - wrap
   - xscrollcommand
   - yscrollcommand

  
  Methods
   - delete( startIndex [, endIndex] )
   - get( startIndex [, endIndex] )
   - index( index )
   - insert( index [, string] )
   - see( index )
   Bookmark
   - index( mark )
   - mark_gravity( mark [, gravity] )
   - mark_names()
   - mark_set( mark, index )
   - mark_unset( mark, index )
   Tab (Tag?)
   - tag_add( tagName, startIndex [, endIndex] )
   - tag_config ( ... )
   - tag_delete( tagName )
   - tag_remove( tagName [, startIndex [, endIndex]] )
#------------------------------------------------------------------------------
"""

'''
NOTE:
 - Text (multiple lines); Entry (One line)
 - no ttk.Text ??
'''

## ----------------------------------------------------------------------------
# Text:
#  - 
#  - 
#


import tkinter as tk
from tkinter import *
from tkinter import ttk
from accCmdUtil import execute_command_hex_string
from funByteArray import ByteArrayToString

# -----------------------------------------------------------------------------
'''-------------------------------------------------------------------------'''
def onclick():
  pass




## ----------------------------------------------------------------------------
class Application(tk.Frame):
  def __init__(self, master=None):
    tk.Frame.__init__(self, master)
    self.grid()
    self.createWidgets()

  def createWidgets(self):
    # HEX command 
    self.AccCmdText = tk.Text(self, height=2)
    self.AccCmdText.grid(row=0, rowspan=2, column=0, columnspan=4)
    self.AccCmdRun = tk.Button(self)
    self.AccCmdRun["text"] = "Run"
    self.AccCmdRun["command"] = self.run_acc_command
    self.AccCmdRun.grid(row=0, column=5, ipady=3)

    self.AccFuncText = tk.Text(self, height=10)
    self.AccFuncText.grid(row=3, rowspan=2, column=0, columnspan=4, pady=10)
    self.AccFuncRun = tk.Button(self)
    self.AccFuncRun["text"] = "Run"
    self.AccFuncRun["command"] = self.run_acc_function
    self.AccFuncRun.grid(row=3, column=5)
    
    #self.QUIT = tk.Button(self, text="QUIT", fg="red", command=root.destroy)
    #self.QUIT.grid()
    self.OutputText = tk.Text(self)
    self.OutputText.grid(row=10, rowspan=10, column=0, columnspan=4)
    
  def run_acc_command(self):
    text = self.AccCmdText.get('0.0', END)
    
    resp = execute_command_hex_string( text, )
    s = ByteArrayToString( resp )
    self.AccCmdText.insert( END, s )
    #self.OutputText.insert( INSERT, s )
    return

  def run_acc_function(self):
    text = self.AccFuncText.get('0.0', END)
    print( text )
    self.OutputText.insert( INSERT, text )
    #self.AccFuncText.insert( END, text )
    


root = tk.Tk()

#(tk.Tk()).title("App Title again")
root.title("ACC Command X")

app = Application(master=root)

app.mainloop()





## ----------------------------------------------------------------------------
# Resources
#
# http://www.tutorialspoint.com/python/python_gui_programming.htm
# 
# https://docs.python.org/3.4/tutorial/modules.html
#
# http://www.tutorialspoint.com/python/tk_cursors.htm <-- cursor names
#
#


"""
#------------------------------------------------------------------------------
tkinter Widgets:
  - BitmapImage
  - Button
  - Canvas
  - Checkbutton
  - Entry
  - Frame
  - Label
  - LabelFrame
  - Listbox
  - Menu
  - Menubutton
  - Message
  - OptionMenu
  - PanedWindow
  - PhotoImage
  - Radiobutton
  - Scale
  - Scrollbar
  - Text
  - Toplevel
  - scrolledtext  <- ?
  - Spinbox
  - tkMessageBox <- not in 3.x ?
#------------------------------------------------------------------------------
"""

"""
#------------------------------------------------------------------------------
tkinter has following method and properties:
  - ACTIVE
  - ALL
  - ANCHOR
  - ARC
  - BASELINE
  - BEVEL
  - BOTH
  - BOTTOM
  - BROWSE
  - BUTT
  - BaseWidget
  - BitmapImage
  - BooleanVal
  - Button
  - CASCADE
  - CENTER
  - CHAR
  - CHECKBUTTON
  - CHORD
  - COMMAND
  - CURRENT
  - CallWrapper
  - Canvas
  - Checkbutton
  - DISABLED
  - DOTBOX
  - DoubleVar
  - E
  - END
  - EW
  - EXCEPTION
  - EXTENDED
  - Entry
  - Event
  - FALSE
  - FIRST
  - FLAT
  - Frame
  - GROOVE
  - Grid
  - HIDDEN
  - HORIZONTAL
  - INSERT
  - INSIDE
  - Image
  - IntVar
  - LAST
  - LEFT
  - Label
  - LabelFrame
  - Listbox
  - MITER
  - MOVETO
  - MULTIPLE
  - Menu
  - Menubutton
  - Message
  - Misc
  - N
  - NE
  - NO
  - NONE
  - NORMAL
  - NS
  - NSEW
  - NUMERIC
  - NW
  - NoDefaultRoot
  - OFF
  - ON
  - OUTSIDE
  - OptionMenu
  - PAGES
  - PIESLICE
  - PROJECTING
  - Pack
  - PanedWindow
  - PhotoImage
  - Place
  - RADIOBUTTON
  - RAISED
  - READABLE
  - RIDGE
  - RIGHT
  - ROUND
  - Radiobutton
  - S
  - SCROLL
  - SE
  - SEL
  - SEL_FIRST
  - SEL_LAST
  - SEPARATOR
  - SINGLE
  - SOLID
  - SUNKEN
  - SW
  - Scale
  - Scrollbar
  - Spinbox
  - StringVar
  - Studbutton
  - TOP
  - TRUE
  - Tcl
  - TclError
  - TclVersion
  - Text
  - Tk
  - TkVersion
  - Toplevel
  - Tributton
  - UNDERLINE
  - UNITS
  - VERTICAL
  - Variable
  - W
  - WORD
  - WRITABLE
  - Widget
  - Wm
  - X
  - XView
  - Y
  - Yes
  - YView
  - __builtins__
  - __cached__
  - __doc__
  - __file__
  - __loader__
  - __name__
  - __package__
  - __path__
  - __spec__
  - _cnfmerge
  - _default_root
  - _exit
  - _fix
  - _flatten
  - _join
  - _magic_re
  - _setit
  - _space_re
  - _splitdict
  - _stringify
  - _support_default_root
  - _test
  - _tkerror
  - _tkinter
  - _varnum
  - colorchoose
  - commondialog
  - constants
  - dialog
  - filedialog
  - font
  - getboolean
  - getdouble
  - getint
  - image_names
  - image_types
  - mainloop
  - messagebox
  - re
  - simpledialog
  - sys
  - wantobjects
#------------------------------------------------------------------------------
"""
