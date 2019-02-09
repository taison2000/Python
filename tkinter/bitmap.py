#!/usr/bin/python

from tkinter import *
import tkinter

def PrintError():
  print("Error bitmap")
  return;

def PrintHourglass():
  print("Hourglass bitmap")
  return;
  
def PrintInfo():
  print("Info bitmap")
  return;
  
def PrintQuestion():
  print("Question bitmap")
  return;
  
def PrintWarning():
  print("Warning bitmap")
  return;
  
top = Tk()

B1 = Button(top, text="error", relief=RAISED, bitmap="error", command=PrintError )
B2 = Button(top, text="hourglass", relief=RAISED, bitmap="hourglass", command=PrintHourglass )
B3 = Button(top, text="info", relief=RAISED, bitmap="info", command=PrintInfo )
B4 = Button(top, text="question", relief=RAISED, bitmap="question", command=PrintQuestion )
B5 = Button(top, text="warning", relief=RAISED, bitmap="warning", command=PrintWarning )

B1.grid()
B2.grid()
B3.grid()
B4.grid()
B5.grid()

top.mainloop()

