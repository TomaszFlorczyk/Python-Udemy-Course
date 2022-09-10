from cgitb import text
import tkinter as tk
import os

scriptDir = os.path.dirname(__file__)
os.chdir(scriptDir)



window = tk.Tk()
window.title("Application")
logo = tk.PhotoImage(file="obrazek.png")

label1 = tk.Label(window, text="Hello world!", 
foreground= "white", 
background= "black",
width = 20,
height = 3,
cursor= "dot",
font = "Times 18 bold italic underline",
anchor= tk.W, 
padx= 5,
pady= 5
)
label1.pack()

label2 = tk.Label(window, text="Hello again!")
label2.pack()

label3 = tk.Label(window,
            text="Hello world!",
            image=logo,
            width=200,
            height=200,
            foreground="red",
            compound=tk.CENTER)
label3.pack()

label3.config(text="Hello world \n Hello again!")


window.mainloop()