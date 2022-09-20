<<<<<<< HEAD
import tkinter as tk

window = tk.Tk()


def spinValue():
    label.config(text= str(spin.get()))

spin = tk.Spinbox(window, from_=0, to=50, command=spinValue)
spin.pack()

label = tk.Label(window)
label.pack()    


=======
import tkinter as tk

window = tk.Tk()


def spinValue():
    label.config(text= str(spin.get()))

spin = tk.Spinbox(window, from_=0, to=50, command=spinValue)
spin.pack()

label = tk.Label(window)
label.pack()    


>>>>>>> d4f06d970b4d665710026f2d53dde28fad90b685
window.mainloop()