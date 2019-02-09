from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry("480x300+0+0")

# Main Frame "content"
content = ttk.Frame(root, padding=(3,3,12,12))

# Upper Left 'Frame'
#frame = ttk.Frame(content, borderwidth=5, relief="sunken", width=200, height=100)
frame = ttk.Frame(content, borderwidth=5, relief="raised", width=200, height=100)

namelbl = ttk.Label(content, text="Name")
name = ttk.Entry(content)

onevar = BooleanVar()
twovar = BooleanVar()
threevar = BooleanVar()

onevar.set(True)
twovar.set(False)
threevar.set(True)

# ttk
one = ttk.Checkbutton(content, text="One", variable=onevar, onvalue=True)
two = ttk.Checkbutton(content, text="Two", variable=twovar, onvalue=True)
three = ttk.Checkbutton(content, text="Three", variable=threevar, onvalue=True)
ok = ttk.Button(content, text="Okay")
cancel = ttk.Button(content, text="Cancel")
# tk
oneTk = Checkbutton(content, text="One", variable=onevar, onvalue=True)
twoTk = Checkbutton(content, text="Two", variable=twovar, onvalue=True)
threeTk = Checkbutton(content, text="Three", variable=threevar, onvalue=True)
okTk = Button(content, text="Okay")
cancelTk = Button(content, text="Cancel")

content.grid(column=0, row=0, sticky=(N, S, E, W))
frame.grid(column=0, row=0, columnspan=3, rowspan=2, sticky=(N, S, E, W))
namelbl.grid(column=3, row=0, columnspan=2, sticky=(N, W), padx=5)
name.grid(column=3, row=1, columnspan=2, sticky=(N, E, W), pady=5, padx=5)

# ttk
one.grid(column=0, row=3)
two.grid(column=1, row=3)
three.grid(column=2, row=3)
ok.grid(column=3, row=3)
cancel.grid(column=4, row=3)
# tk
oneTk.grid(column=0, row=4)
twoTk.grid(column=1, row=4)
threeTk.grid(column=2, row=4)
okTk.grid(column=3, row=4)
cancelTk.grid(column=4, row=4)

# Important: the root has to be resizable
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

content.columnconfigure(0, weight=3)
content.columnconfigure(1, weight=3)
content.columnconfigure(2, weight=3)
content.columnconfigure(3, weight=1)
content.columnconfigure(4, weight=1)
content.rowconfigure(1, weight=1)

root.mainloop()
