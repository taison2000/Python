#!/usr/bin/python
# Comment start with #



import sys
import tkinter as tk
#from tkinter import messagebox as msgBox  #import tkMessageBox

global j
j=0

top = tk.Tk()

lbl1 = tk.Label(None, text='This is a label #1')
lbl2 = tk.Label(None, text=' label #2', bg="light green")
lbl3 = tk.Label(None, text=' Font=Harrington Size=16', bg="gray", height=5, width=25, \
         font=("Harrington", 16), fg="green", cursor='cross')


lbl1.grid()
lbl2.grid()
lbl3.grid()

top.title("Label Widget")

## ----- Function run alongside with mainloop -----
def runFunc():
  global j
  for i in range(20):
    print (i)
  j+=1
  lbl2['text']='Label #2 : %02d'%j
  top.after(2000, runFunc)  # <- call the function again

top.after(2000, runFunc)

#lbl1.mainloop()
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
