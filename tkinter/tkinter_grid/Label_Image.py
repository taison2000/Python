#!/usr/bin/python
# Comment start with #

## ----------------------------------------------------------------------------
# PhotoImage
"""
  - PhotoImage read format : GIF and PGM/PPM 
  - For other formats, use PIL (Python Imaging Library) module
"""

import sys
import tkinter as tk
#from tkinter import messagebox as msgBox  #import tkMessageBox

top = tk.Tk()
top.title("Label Widget")

#imageData = tk.PhotoImage(file='Label_Image.bmp')
imageData = tk.PhotoImage(file='php.gif')
lbl1 = tk.Label(top, text='This is a label #1')
lbl1['image'] = imageData
lbl1.grid()

lbl2 = tk.Label(None, text=' label #2', bg="light green")
lbl3 = tk.Label(None, text=' Font=Harrington Size=16', bg="gray", height=5, width=25, \
         font=("Harrington", 16), fg="green", cursor='cross')



lbl2.grid()
lbl3.grid()



for i in range(20):
  print (i)
  
#lbl1.mainloop()
top.mainloop()



## ----------------------------------------------------------------------------
"""
# Resources
# - PhotoImage - http://effbot.org/tkinterbook/photoimage.htm
# - http://www.tutorialspoint.com/python/python_gui_programming.htm
# 
# - https://docs.python.org/3.4/tutorial/modules.html

# - http://www.tutorialspoint.com/python/tk_label.htm <-- Label
# - http://www.tutorialspoint.com/python/tk_cursors.htm <-- cursor names
# - http://effbot.org/tkinterbook/label.htm  <-- Label
#
#------------------------------------------------------------------------------
"""


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
  - messagebox (v2.x -> tkMessageBox)
  - PaneWindow
  - Radiobutton
  - Scale
  - Scrollbar
  - Spinbox
  - Text
  - Toplevel
#------------------------------------------------------------------------------
"""
