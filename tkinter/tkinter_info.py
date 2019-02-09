#!/usr/bin/python
# Comment start with #



import sys
import tkinter as tk
from tkinter import messagebox as msgBox  #import tkMessageBox

## ----------------------------------------------------------------------------

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

##------------------------------------------------------------------------------
"""
#------------------------------------------------------------------------------
  Parameters
   - bg  (Text, Listbox, Radiobutton)
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
   - 
  
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



'''-------------------------------------------------------------------------'''
#------------------------------------------------------------------------------

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

## ----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# Resources
# https://wiki.python.org/moin/TkInter
# http://www.tkdocs.com/tutorial/index.html
# http://www.tutorialspoint.com/python/python_gui_programming.htm
# 
# https://docs.python.org/3.4/tutorial/modules.html
# http://www.tutorialspoint.com/python/tk_cursors.htm <-- cursor names
#
#

