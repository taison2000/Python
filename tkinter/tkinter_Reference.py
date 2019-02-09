#!/usr/bin/python

from tkinter import *

##-----------------------------------------------------------------------------
def NewFile():
    print ("New File")

def OpenFile():
    name = askopenfilename()
    print (name)

def About():
    print ("This is a example of menu")

root = Tk()
menu = Menu(root)
root.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="New", command=NewFile)
filemenu.add_command(label="Open...", command=OpenFile)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)

helpmenu = Menu(menu)
menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About...", command=About)

mainloop()

##-----------------------------------------------------------------------------
"""
geometry:
  format : 'wxh±x±y' ("Width x Height ± x_pos ± y_pos")
    description: w=width h=Height x=Windows_x_pos y=Windows_y_pos
  example: geometry = '120x50-0+20'
    A window would be 120 pixels wide by 50 pixels high.
    Its top right corner will be (-0, 20) pixels position
    
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

##-----------------------------------------------------------------------------
## tkinter Python 2x vs Python 3x:
"""
  Ver_2x          Ver_3x
  ------------------------------------------
  Tkinter         tkinter
  tkMessageBox    tkinter.messagebox
  tkColorChooser  tkinter.colorchooser
  tkFileDialog    tkinter.filedialog
  tkCommonDialog  tkinter.commondialog
  tkSimpleDialog  tkinter.simpledialog
  tkFont          tkinter.font
  Tkdnd           tkinter.dnd
  ScrolledText    tkinter.scrolledtext
  Tix             tkinter.tix
  ttk             tkinter.ttk
"""
# http://stackoverflow.com/questions/673174/file-dialogs-of-tkinter-in-python-3/673309#673309




