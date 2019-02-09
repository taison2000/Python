#!/usr/bin/python
# Comment start with #



import tkinter as tkWin
from tkinter import messagebox as msgBox  #import tkMessageBox

top = tkWin.Tk()
# Code to add widgets will go here ...
top.columnconfigure(0, weight=1)  # col_0

CheckVar1 = tkWin.IntVar()
CheckVar2 = tkWin.IntVar()
# defined subclasses Variable : StringVar, IntVar, DoubleVar, and BooleanVar. 
#   To read the current value of such a variable, call the get() method on it, 
#   to change its value you call the set() method

chk1 = tkWin.Checkbutton (top, text="Music", variable=CheckVar1, \
               onvalue=1, offvalue=0, height=5, width=20)

chk2 = tkWin.Checkbutton (top, text="Video", variable=CheckVar2, \
               onvalue=1, offvalue=0, height=5, width=20)
                              
#chk1.pack()
#chk2.pack()
chk1.grid()
chk2.grid()

## ----- Water Days -----
varWaterDays = tkWin.IntVar()
frameWaterDays = tkWin.Frame(top)
for i in range(8):
  frameWaterDays.columnconfigure(i, weight=1)
frameWaterDays.grid(row=0, column=0, rowspan=6, columnspan=6, sticky=tkWin.W+tkWin.E+tkWin.N+tkWin.S)
chkBtnMon = tkWin.Checkbutton( frameWaterDays, text='Mon', variable=varWaterDays, onvalue=1, offvalue=0 )
chkBtnTue = tkWin.Checkbutton( frameWaterDays, text='Tue', variable=varWaterDays, onvalue=1, offvalue=0 )
chkBtnWed = tkWin.Checkbutton( frameWaterDays, text='Wed', variable=varWaterDays, onvalue=1, offvalue=0 )
chkBtnThu = tkWin.Checkbutton( frameWaterDays, text='Thu', variable=varWaterDays, onvalue=1, offvalue=0 )
chkBtnFri = tkWin.Checkbutton( frameWaterDays, text='Fri', variable=varWaterDays, onvalue=1, offvalue=0 )
chkBtnSat = tkWin.Checkbutton( frameWaterDays, text='Sat', variable=varWaterDays, onvalue=1, offvalue=0 )
chkBtnSun = tkWin.Checkbutton( frameWaterDays, text='Sun', variable=varWaterDays, onvalue=1, offvalue=0 )
chkBtnMon.grid( row=0, column=1, padx=2, pady=2, sticky=tkWin.E+tkWin.W ) 
chkBtnTue.grid( row=0, column=2, padx=2, pady=2, sticky=tkWin.E+tkWin.W ) 
chkBtnWed.grid( row=0, column=3, padx=2, pady=2, sticky=tkWin.E+tkWin.W ) 
chkBtnThu.grid( row=0, column=4, padx=2, pady=2, sticky=tkWin.E+tkWin.W ) 
chkBtnFri.grid( row=0, column=5, padx=2, pady=2, sticky=tkWin.E+tkWin.W ) 
chkBtnSat.grid( row=0, column=6, padx=2, pady=2, sticky=tkWin.E+tkWin.W ) 
chkBtnSun.grid( row=0, column=7, padx=2, pady=2, sticky=tkWin.E+tkWin.W ) 
            
top.mainloop()



# -----------------------------------------------------------------------------
# Resources
# http://www.tutorialspoint.com/python/python_gui_programming.htm
# 
## double
'''
Hello world
'''

"""
Hello world
"""
