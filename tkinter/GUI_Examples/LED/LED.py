# Idle 07_02_LED ON using GUI
from time import sleep

#from Tkinter import *
from tkinter import *

class App:

  def __init__(self, master): 
    frame = Frame(master)
    frame.pack()
    #Label(frame, text='Turn LED ON').grid(row=0, column=0)
    #Label(frame, text='Turn LED OFF').grid(row=1, column=0)

    self.button = Button(frame, text='LED 0 ON', command=self.convert0)
    self.button.grid(row=2, column=0)

    ## Here is the Label to hold LED image
    #self.LED = Label(frame, image=logoGrnLed).grid(row=2, column=1) ## <- Would not able to toggle LED
    #self.LED = Label(frame, image=logoGrnLed, width=300, height=300)
    self.LED = Label(frame, image=logoGrnLed)
    self.LED.grid(row=2, column=1)

  def convert0(self, tog=[0]):
    tog[0] = not tog[0]
    if tog[0]:
      print('LED 0 OFF')
      self.button.config(text='LED 0 OFF')
      self.LED.config(image = logoRedLed)
    else:
      print('LED 0 ON')
      self.button.config(text='LED 0 ON')
      self.LED.config(image = logoGrnLed)


root = Tk()

## LED image file conversion
#logoGrnLed = PhotoImage(file="C:\My Documents\MyPictures\Green LED.gif")
#logoRedLed = PhotoImage(file="C:\My Documents\My Pictures\Red LED.gif")

logoGrnLed = PhotoImage(file=".\LED_Green_30x30.png")
#logoRedLed = PhotoImage(file=".\LED_Red_30x30.png")


#logoGrnLed = PhotoImage(file=".\LED_Green_48x48.png")
#logoRedLed = PhotoImage(file=".\LED_Red__28x28.gif")

#logoGrnLed = PhotoImage(file=".\Green_LED.png")
#logoRedLed = PhotoImage(file=".\Red_LED.png")

logoRedLed = PhotoImage(file=".\LED_Red_Flashing.gif")

#------------------------------------------------------------------------------
root.wm_title('LED On & Off ')
app = App(root)
root.mainloop()

##-----------------------------------------------------------------------------
# Resource:
# http://stackoverflow.com/questions/20926568/python-gui-button-trying-to-toggle-a-label-image
#

#-----------------------------------------------------------------------------
#-----                                END                                -----
#-----------------------------------------------------------------------------
