#!/usr/bin/python
# Comment start with #

##-----------------------------------------------------------------------------
# get help from IDLE
#   1. import tkinter
#   2. help(tkinter.Listbox)


#------------------------------------------------------------------------------
# E1 = Entry (master, option, ...)
#   Parameters:
#     * master : represents the parent window
#     * options: 
#
#   --- Options ---
#     - bg : background color
#     - bd : border size
#     - command : A procedure to be called when 
#     - cursor
#     - font
#     - exportselection
#     - fg
#     - highlightcolor
#     - justify
#     - relief
#     - selectbackground
#     - selectforeground
#     - show
#     - state
#     - textvariable
#------------------------------------------------------------------------------


"""
#------------------------------------------------------------------------------
Entry Widgets:
  Methods
  - delete(first, last=None)
  - get()
  - icursor(index)
  - index (index)
  - insert (index, s)
  - select_adjust(index)
  - select_clear()
  - select_from(index)
  - select_present()
  - select_range(start, end)
  - select_to (index)
  - xview(index)
  - xview_Scroll(number, what)
#------------------------------------------------------------------------------
"""

# # String index
# text="String Index"
# # text[0]==S text[1]==t text[2]==r text[3]==i text[4]==n
# # text[-1]==x text[-2]==e text[-3]==d text[-4]==n text[-5]==I
# print(text)
# print("Negative index")
# Length=len(text)
# print(Length)
# for i in range(Length):
   # print(text[-i-1], -i-1)

from tkinter import *
from tkinter import ttk

def entryChanges():
  print ("Entry has been changed")
  
top = Tk()

top.title ("entry widget example")

#L1 = Label(top, text="User Name")   
L1 = Label(top, text="User Name", command=entryChanges())
L1.pack (side = LEFT)

E1 = Entry(top, bd=5)
E1.pack(side = RIGHT)

E2 = ttk.Entry(top)
E2.pack()

e2Config = E2.config()
for item in e2Config:
  print("%-15s"%item, " : ", e2Config[item])

val = StringVar()
val.set("This is variable")
E2.config(textvariable=val)
print( val.get() )
print( E2.get() )

## Note:
# Can not use val="String Data".
#   Has to use "val.get()" and "val.set" to get or set value.
#   val = StringVar()   => type(val) == <class 'tkinter.StringVar'>
#   val = "String Data" => type(val) == <class 'str'>


top.mainloop()

""""
import tkinter as tk

class Application(tk.Frame):
   def __init__(self, master=None):
      tk.Frame.__init__(self, master)
      self.pack()
      self.createWidgets()
      
   def createWidgets(self):
      self.hi_there = tk.Button(self)
      self.hi_there["text"] = "Hello World\n(click me)"
      self.hi_there["command"] = self.say_hi
      self.hi_there.pack(side="top")
      
      self.QUIT = tk.Button(self, text="QUIT", fg="red", command=root.destroy)
      self.QUIT.pack(side="bottom")
      
   def say_hi(self):
      print("hi there, everyone!")


root = tk.Tk()
app = Application(master=root)

app.mainloop()
"""

"""
#------------------------------------------------------------------------------
tkinter Widgets:
  - Button
  - Canvas
  - Checkbutton
  - Entry
  - Frame
  - Label
  - Listbox
  - Menubutton
  - Menu
  - Message
  - Radiobutton
  - Scale
  - Scrollbar
  - Text
  - Toplevel
  - Spinbox
  - PaneWindow
  - LabelFrame
  - tkMessageBox
#------------------------------------------------------------------------------
"""
