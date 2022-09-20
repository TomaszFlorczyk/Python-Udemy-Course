<<<<<<< HEAD
import tkinter as tk

window = tk.Tk()

def radioClicked():
    print("radioValue: ", radioValue.get())

radioValue = tk.IntVar()

radio1 = tk.Radiobutton(window, text="Option1", variable=radioValue, value=1, command=radioClicked)
radio2 = tk.Radiobutton(window, text="Option2", variable=radioValue, value=2, command=radioClicked)
radio3 = tk.Radiobutton(window, text="Option3", variable=radioValue, value=3, command=radioClicked)

radio1.pack()
radio2.pack()
radio3.pack()

=======
import tkinter as tk

window = tk.Tk()

def radioClicked():
    print("radioValue: ", radioValue.get())

radioValue = tk.IntVar()

radio1 = tk.Radiobutton(window, text="Option1", variable=radioValue, value=1, command=radioClicked)
radio2 = tk.Radiobutton(window, text="Option2", variable=radioValue, value=2, command=radioClicked)
radio3 = tk.Radiobutton(window, text="Option3", variable=radioValue, value=3, command=radioClicked)

radio1.pack()
radio2.pack()
radio3.pack()

>>>>>>> d4f06d970b4d665710026f2d53dde28fad90b685
window.mainloop()