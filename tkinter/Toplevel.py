from tkinter import *

# the order of the following two lines make a different
root = Tk()
top = Toplevel()

root.title("root(Tk) at the front")
top.title("Toplevel in the back")

top.mainloop()
