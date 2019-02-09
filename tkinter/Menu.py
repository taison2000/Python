from tkinter import *

def donothing():
  filewin = Toplevel( root )
  button = Button( filewin, text="Do nothing button")
  button.pack()

def new_file():
    newfile = Toplevel( root )
    button = Button( newfile, text="New File")
    button.pack()
    
##-----------------------------------------------------------------------------
root = Tk()
root.title("Menu Demo")
root.geometry("700x500+450+250")

## Menu
menubar = Menu( root )
root.config( menu=menubar )

## File
filemenu = Menu( menubar, tearoff=0 )
menubar.add_cascade( label="File", menu=filemenu )

filemenu.add_command( label="New", command=new_file )
filemenu.add_command( label="Open", command=donothing )
filemenu.add_command( label="Save", command=donothing )
filemenu.add_command( label="Save as ...", command=donothing )
filemenu.add_command( label="Close", command=donothing )
filemenu.add_separator()
filemenu.add_command( label="Exit", command=root.quit )


## Edit
editmenu = Menu( menubar, tearoff=0 )
menubar.add_cascade( label="Edit", menu=editmenu )

editmenu.add_command( label="Undo", command=donothing )
editmenu.add_separator()
editmenu.add_command( label="Cut", command=donothing )
editmenu.add_command( label="Copy", command=donothing )
editmenu.add_command( label="Paste", command=donothing )
editmenu.add_command( label="Delete", command=donothing )
editmenu.add_command( label="Select All", command=donothing )



## Help
helpmenu = Menu( menubar, tearoff=0 )
menubar.add_cascade( label="Help", menu=helpmenu )

helpmenu.add_command( label="Help Index", command=donothing )
helpmenu.add_command( label="About ...", command=donothing )


root.mainloop()

