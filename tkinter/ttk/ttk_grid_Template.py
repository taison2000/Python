#!C:\Python34\python.exe
#!/Python34/python
#!/usr/bin/python

from tkinter import ttk
import tkinter as tk

class ExampleApp( tk.Frame ):
  def __init__(self, *args, **kwargs):
    tk.Frame.__init__(self, *args, **kwargs)
    self.var1 = tk.StringVar()
    self.var2 = tk.StringVar()

    ## ----- Frame -----
    f1 = ttk.Frame(self)
    red_button = ttk.Button(f1, text="Red", command=self.make_red)
    default_button = ttk.Button(f1, text="Default", command=self.make_default)
    default_button.grid()
    red_button.grid()

    f2 = ttk.Frame(self)
    self.cb_one = ttk.Checkbutton(f2, text="Option 1", variable=self.var1,
                                  onvalue=1, offvalue=0)
    self.cb_two = ttk.Checkbutton(f2, text="Option 2", variable=self.var2,
                                  onvalue=1, offvalue=0)
    self.cb_one.grid()
    self.cb_two.grid()

    f1.grid()
    f2.grid()

    style = ttk.Style()
    style.configure("Red.TCheckbutton", foreground="red")

    styleEntry = ttk.Style()
    styleEntry.configure("blue.Entry", background='blue')

  def make_red(self):
    self.cb_one.configure(style="Red.TCheckbutton")
    self.cb_two.configure(style="Red.TCheckbutton")

  def make_default(self):
    self.cb_one.configure(style="TCheckbutton")
    self.cb_two.configure(style="TCheckbutton")

#END class ExampleApp

if __name__ == "__main__":
  root = tk.Tk()
  ExampleApp(root).grid( )
  root.title("ttk Template")
  root.mainloop()


##-----------------------------------------------------------------------------
## Resource:
"""
 - http://effbot.org/tkinterbook/menu.htm
 - http://www.tkdocs.com/widgets/frame.html
 - http://www.tkdocs.com/tutorial/widgets.html#frame

"""
