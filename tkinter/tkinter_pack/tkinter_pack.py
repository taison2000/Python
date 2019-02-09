#!/usr/bin/python

# Comment start with #
# No multiple line comment

   
import tkinter as tk
from tkinter import messagebox as msgBox  #import tkMessageBox

top = tk.Tk()

def helloCallBack():
   msgBox.showinfo ("Title Python", "Message : Hello")

def InfoCallBack():
   msgBox.showinfo ("Information", "This is info Only")

colorBG = "#0000f0"   # notice color must be 6 hex digits (#123abc)
btnHello = tk.Button (top, text = "Hello", command = helloCallBack, fg="gray", highlightcolor="red")
#btnInfo = tk.Button (top, text = " Info ", command = InfoCallBack, fg="Green", bg="gray")
btnInfo = tk.Button (top, text = " Info ", command = InfoCallBack, fg="#ff0000", bg=colorBG, justify="right", width=20)


#btnHello.pack(side="left")
btnHello.pack(side="right")
#btnInfo.pack()
#btnInfo.pack(fill=BOTH, expand=1)
btnInfo.pack( expand=1)
#btnInfo.pack()

#
lbl_1 = tk.Label(top, text="Red", bg="Red", fg="white")
lbl_1.pack(side="left", fill="both")
lbl_2 = tk.Label(top, text="Green", bg="green", fg="black")
lbl_2.pack(side="left", expand=1)
lbl_3 = tk.Label(top, text="Blue", bg="BLUE", fg="white")
lbl_3.pack()

top.mainloop() 

#------------------------------------------------------------------------------
#  http://effbot.org/tkinterbook/pack.htm    <-- pack
#     anchor   - Where the packer is to place each slave in its parcel
#     both     - 
#     expand   - Boolean (0, 1)
#     fill     - 'x', 'y', 'both', 'none'
#     ipadx    - designating internal padding on each side of the slave widget
#     ipady
#     padx     - designating external padding on each side of the slave widget
#     pady
#     sied = "left", "right", "top", "bottom"
#
#
#  pack vs grid
#     Pack is more easier to use
#     grid is more powerful
#   Don't mix pack and grid in the same master window
#


# NOTE:
# https://mail.python.org/pipermail//tkinter-discuss/2011-August/002916.html
#  - tkMessageBox has been renamed to messagebox in Python 3.x.
#  - Module is not available in tkinter
#  - code : from tkinter import messagebox

# http://www.tutorialspoint.com/python/tk_button.htm
# http://www.tutorialspoint.com/python/python_gui_programming.htm    # GUI Programming
#
# http://www.tutorialspoint.com/python/tk_colors.htm


##-----------------------------------------------------------------------------
## Examples:
# Radiobutton_1.pack( anchor=W )
#
#



