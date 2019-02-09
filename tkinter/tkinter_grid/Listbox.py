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

"""
#------------------------------------------------------------------------------
Listbox Widgets:
  Methods
  - activate( index )
  - bbox( index )
  - curselection()
  - delete( startIndex [, endIndex=None] )
  - get( startIndex [, endIndex=None] )
  - index ( i )
  - insert ( index, *element )
  - nearest( y )
  - see( index )
  - size()
  - xview()
  - xview_moveto( fraction )
  - xview_Scroll( number, what )
  - yview()
  - yview_moveto( fraction )
  - yview_Scroll( number, what )
#------------------------------------------------------------------------------
"""


from tkinter import *
from tkinter import ttk

def entryChanges():
    print ("Entry has been changed")
    return

## --- activate method --- 
def Listbox_activate():
    lbx_index = int(entry.get())
    print( "Listbox Index : %d" %lbx_index )
    lbx.activate( lbx_index )
    return

## --- delete method --- 
def method_delete():
    lbx.delete( 0 ) # delete first item
    lbx.delete( 1, 5 )  # delete line 1~4 (not 5)
    lbx.delete(0, END)  # delete all content
    return

## --- get method --- 
def ListboxGet():
    #lbxGetResult = lbx.get(0) # get item with index==0
    #lbxGetResult = lbx.get(5) # get item with index==5
    #lbxGetResult = lbx.get(0, 1)  # get items from index==0 to 1
    lbxGetResult = lbx.get(4, 8)
    print( type(lbxGetResult) )
    messagebox.showinfo ("Listbox Get", lbxGetResult)
    return

## --- curselection method --- 
def ListboxCurselection():
    lbx_Curselection = lbx.curselection() # Return the index of the current selection
    if lbx_Curselection==():
        lbx_Curselection = "Nothing selected"
    messagebox.showinfo("Listbox Curselection", lbx_Curselection)
    return

## --- index method ---   
def Listbox_index():
    lbx_index = int(entry.get())
    lbx.index( lbx_index )
    return

##-----------------------------------------------------------------------------
top = Tk()
top.title ("Listbox widget")


#lbx = Listbox(top, listvariable=("opt1", 'opt2', 'opt3'), command=entryChanges())
lbx = Listbox(top, listvariable=("opt1", 'opt2', 'opt3'))
lbx.insert(1, "Listbox Item_1")
lbx.insert(2, "Listbox Item_2")
lbx.insert(3, "Listbox Item_3")
lbx.insert(4, "Listbox Item_4")
lbx.insert(5, "Listbox Item_5")
lbx.insert(6, "Listbox Item_6")
lbx.insert(7, "Listbox Item_7")
lbx.insert(8, "Listbox Item_8")
lbx.insert(9, "Listbox Item_9")
lbx.insert(10, "Listbox Item_10")
lbx.grid( row=0, column=0, rowspan=3 )

label = Label( top, bd=5, text="Index" )
label.grid(row=0, column=1)
entry = Entry(top, bd=5)
entry.grid(row=1, column=1)

btnActivateIndex = ttk.Button( top, text="activate", command=Listbox_activate )
btnActivateIndex.grid(row=2, column=1)

btnListboxIndex = ttk.Button( top, text="Listbox index", command=Listbox_index)
btnListboxIndex.grid()

butListboxGet = ttk.Button(top, text="Listbox get", command=ListboxGet)
butListboxGet.grid()

butListboxCurselection = ttk.Button(top, text="Listbox Curselection", command=ListboxCurselection )
butListboxCurselection.grid()

top.mainloop()

""""
import tkinter as tk

class Application(tk.Frame):
   def __init__(self, master=None): # master is the parent widget, optional, default=None
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

##-----------------------------------------------------------------------------
"""
NOTE:
 - There is no Theme(ttk) Listbox
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
