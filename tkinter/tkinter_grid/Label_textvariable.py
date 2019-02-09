#!/usr/bin/python
# Comment start with #



import sys
import tkinter as tk
#from tkinter import messagebox as msgBox  #import tkMessageBox

top = tk.Tk()
top.title("Label Widget")

lbl1 = tk.Label(None, text='This is a label #1')
lbl2 = tk.Label(None, text=' label #2', bg="light green")

lbl1.grid()
lbl2.grid()

lbl3 = tk.Label(None, text=' Font=Harrington Size=16', bg="gray", height=5, width=25, \
         font=("Harrington", 16), fg="green", cursor='cross')

lbl3.grid()


newLabelContent = StringVar()
lbl1['textvariable'] = newLabelContent
newLabelContent.set("Test from textvariable")

top.mainloop()



# -----------------------------------------------------------------------------
# Resources
# http://www.tutorialspoint.com/python/python_gui_programming.htm
# 
# https://docs.python.org/3.4/tutorial/modules.html

# http://www.tutorialspoint.com/python/tk_label.htm <-- Label
# http://www.tutorialspoint.com/python/tk_cursors.htm <-- cursor names
# http://effbot.org/tkinterbook/label.htm  <-- Label
#
