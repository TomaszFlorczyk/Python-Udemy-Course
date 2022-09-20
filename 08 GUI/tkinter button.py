<<<<<<< HEAD
import tkinter as tk

window = tk.Tk()
def buttonClicked():
    print("cliked")
    quit()
button = tk.Button(
    window,
    text="Quit",
    bd=10,
    fg="red",
    bg="green",
    activeforeground="black",
    activebackground="silver",
    font="Times 18 bold",
    height=3,
    width="20",
    padx=10,
    pady=10,
    relief="groove",
    command= buttonClicked


)
button.pack()
=======
import tkinter as tk

window = tk.Tk()
def buttonClicked():
    print("cliked")
    quit()
button = tk.Button(
    window,
    text="Quit",
    bd=10,
    fg="red",
    bg="green",
    activeforeground="black",
    activebackground="silver",
    font="Times 18 bold",
    height=3,
    width="20",
    padx=10,
    pady=10,
    relief="groove",
    command= buttonClicked


)
button.pack()
>>>>>>> d4f06d970b4d665710026f2d53dde28fad90b685
window.mainloop()