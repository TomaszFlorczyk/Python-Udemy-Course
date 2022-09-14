import tkinter as tk

window = tk.Tk()

def menuItemSelected():
    print("menu item selected")

def menuItemClose():
    quit()

rootMenu = tk.Menu()
fileMenu = tk.Menu()
fileMenu.add_command(label="New", command=menuItemSelected)
fileMenu.add_command(label="Open", command=menuItemSelected)
fileMenu.add_command(label="Save", command=menuItemSelected)
fileMenu.add_command(label="Save as", command=menuItemSelected)
fileMenu.add_separator()
fileMenu.add_command(label="Close", command=menuItemClose)



editMenu = tk.Menu()
editMenu.add_command(label="Cut", command=menuItemSelected)
editMenu.add_command(label="Copy", command=menuItemSelected)
editMenu.add_command(label="Paste", command=menuItemSelected)
editMenu.add_command(label="Config", command=menuItemSelected)

rootMenu.add_cascade(label="File", menu=fileMenu)
rootMenu.add_cascade(label="Edit", menu=editMenu)

window.config(menu=rootMenu)








window.mainloop()