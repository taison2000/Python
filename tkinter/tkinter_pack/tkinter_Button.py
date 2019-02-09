#!/usr/bin/python

# Comment start with #
# No multiple line comment

   
import tkinter as tk
from tkinter import messagebox as msgBox  #import tkMessageBox
## tkMessageBox no longer available in Python 3. Replace with 'messagebox'

top = tk.Tk()

def helloCallBack():
   msgBox.showinfo ("Title Python", "Message : Hello")

def InfoCallBack():
   msgBox.showinfo ("Information", "This is info Only")

colorBG = "#0000f0"   # notice color must be 6 hex digits (#123abc)
btnHello = tk.Button (top, text = "Hello", command = helloCallBack, fg="gray", highlightcolor="red")
#btnInfo = tk.Button (top, text = " Info ", command = InfoCallBack, fg="Green", bg="gray")
btnInfo = tk.Button (top, text = " Info ", command = InfoCallBack, fg="#ff0000", bg=colorBG, justify="right", width=20)


btnHello.pack(side="left")
#btnInfo.pack()
#btnInfo.pack(fill=BOTH, expand=1)
btnInfo.pack( expand=1)
#btnInfo.pack()



top.mainloop() 


# NOTE:
# https://mail.python.org/pipermail//tkinter-discuss/2011-August/002916.html
#  - tkMessageBox has been renamed to messagebox in Python 3.x.
#  - Module is not available in tkinter
#  - code : from tkinter import messagebox

# http://www.tutorialspoint.com/python/tk_button.htm
# http://www.tutorialspoint.com/python/python_gui_programming.htm    # GUI Programming
#
# http://www.tutorialspoint.com/python/tk_colors.htm
#