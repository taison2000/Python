#!/usr/bin/python

# Comment start with #
# No multiple line comment

##-----------------------------------------------------------------------------
## --- grid ---
"""
  Methods
   - WidgetName.grid( option=value )
   - WidgetName.grid_bbox()
   - WidgetName.grid_columnconfigure()
   - WidgetName.grid_configure()
   - WidgetName.grid_forget()
   - WidgetName.grid_info()
   - WidgetName.grid_location()
   - WidgetName.grid_propagate()
   - WidgetName.grid_remove()
   - WidgetName.grid_rowconfigure()
   - WidgetName.grid_size()
   - WidgetName.grid_slaves()

  grid( option=value )
   options
   - column
   - columnspan
   - in_
   - ipadx
   - ipady
   - padx
   - pady
   - row
   - rowspan
   - sticky
  
  grid_bbox( self, column=None, row=None, col2=None, row2=None )
   options
   - column
   - columnspan
   - in_
   - ipadx

#------------------------------------------------------------------------------
"""

##-----------------------------------------------------------------------------
## grid(**options)
"""
  **options
    Geometry options.
  column=
    Insert the widget at this column. Column numbers start with 0. If omitted, defaults to 0.
  columnspan=
    If given, indicates that the widget cell should span multiple columns. The default is 1.
  in=
    Place widget inside to the given widget. 
    You can only place a widget inside its parent, or in any decendant of its parent. 
    If this option is not given, it defaults to the parent.
    Note that in is a reserved word in Python. 
    To use it as a keyword option, append an underscore (in_). 
  in_=
    Same as 'in'. See above.
  ipadx=
    Optional horizontal internal padding. Works like padx, but the padding is 
    added inside the widget borders. Default is 0. 
  ipady=
    Optional vertical internal padding. Works like pady, but the padding is added 
    inside the widget borders. Default is 0. 
  padx=
    Optional horizontal padding to place around the widget in a cell. 
    Default is 0.
  pady=
    Optional vertical padding to place around the widget in a cell. 
    Default is 0.
  row=
    Insert the widget at this row. Row numbers start with 0. 
    If omitted, defaults to the first empty row in the grid.
  rowspan=
    If given, indicates that the widget cell should span multiple rows. 
    Default is 1.
  sticky=
    Defines how to expand the widget if the resulting cell is larger than 
    the widget itself. This can be any combination of the constants 
    S, N, E, and W, or NW, NE, SW, and SE.

    For example, W (west) means that the widget should be aligned to the left
    cell border. W+E means that the widget should be stretched horizontally 
    to fill the whole cell. W+E+N+S means that the widget should be expanded 
    in both directions. Default is to center the widget in the cell. 
"""

##-----------------------------------------------------------------------------
# help( tkinter.Grid )
#  Notice capital 'G'


import tkinter as tk
from tkinter import messagebox as msgBox  #import tkMessageBox


def helloCallBack():
  msgBox.showinfo ("Title Python", "Message : Hello")
  return

def InfoCallBack():
  msgBox.showinfo ("Information", "This is info Only")
  return;


##-----------------------------------------------------------------------------
top = tk.Tk()
top.title("Grid Manager")


colorBG = "#0000f0"   # notice color must be 6 hex digits (#123abc)
btnHello = tk.Button (top, text = "Hello", command = helloCallBack, fg="gray", highlightcolor="red")
#btnHello.grid(side="left")
btnHello.grid()
bboxHello = btnHello.grid_bbox()
print( bboxHello )


#btnInfo = tk.Button (top, text = " Info ", command = InfoCallBack, fg="Green", bg="gray")
btnInfo = tk.Button (top, text = " Info ", command = InfoCallBack, fg="#ff0000", bg=colorBG, justify="right", width=20)
#btnInfo.grid(fill=BOTH, expand=1)
#btnInfo.grid()
btnInfo.grid()
bboxInfo = btnInfo.grid_bbox()
print( bboxInfo )


#
lbl_1 = tk.Label(top, text="col=5", bg="Red", fg="white")
lbl_1.grid(column=1, columnspan=50)
lbl_2 = tk.Label(top, text="Green Label", bg="green", fg="black")
lbl_2.grid()
lbl_3 = tk.Label(top, text="Blue Label", bg="BLUE", fg="white")
lbl_3.grid()

top.mainloop() 

##-----------------------------------------------------------------------------
# sticky:
#   label.grid(sticky=W+E+N+S)
#



#------------------------------------------------------------------------------
# http://effbot.org/tkinterbook/grid.htm
#
#
#  pack vs grid
#     Pack is more easier to use
#     grid is more powerful
#   Don't mix pack and grid in the same master window
#


# NOTE:
#
# http://www.tutorialspoint.com/python/tk_button.htm
# http://www.tutorialspoint.com/python/python_gui_programming.htm    # GUI Programming
#
# http://www.tutorialspoint.com/python/tk_colors.htm
# http://effbot.org/tkinterbook/grid.htm
#


##-----------------------------------------------------------------------------
## tkinter Widgets:
"""
  - Button
  - Canvas
  - Checkbutton
  - Entry
  - Frame
  - Label
  - LabelFrame
  - Listbox
  - Menubutton
  - Menu
  - Message
  - messagebox ( v2.x -> tkMessageBox )
  - PaneWindow
  - Radiobutton
  - Scale
  - Scrollbar
  - Spinbox
  - Text
  - Toplevel
#------------------------------------------------------------------------------
"""


