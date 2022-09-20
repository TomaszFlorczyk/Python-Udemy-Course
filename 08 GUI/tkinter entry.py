<<<<<<< HEAD
import tkinter as tk

window =tk.Tk()

tk.Label(window, text = "First name:").grid(row=0, column=0)

entry = tk.Entry(window)
entry.grid(row=0, column=1)
entry.insert(0, "Hello")

def showData():
    print("Entry data: ", entry.get() )
    entry.delete(0, "end")

tk.Button(window, text="Show info", command=showData).grid(row=1)
=======
import tkinter as tk

window =tk.Tk()

tk.Label(window, text = "First name:").grid(row=0, column=0)

entry = tk.Entry(window)
entry.grid(row=0, column=1)
entry.insert(0, "Hello")

def showData():
    print("Entry data: ", entry.get() )
    entry.delete(0, "end")

tk.Button(window, text="Show info", command=showData).grid(row=1)
>>>>>>> d4f06d970b4d665710026f2d53dde28fad90b685
window.mainloop()