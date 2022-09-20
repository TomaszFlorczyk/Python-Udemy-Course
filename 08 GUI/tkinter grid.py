<<<<<<< HEAD
import tkinter as tk

window = tk.Tk()


b1 = tk.Button(window, bg = "red", text="Button1")
b1.grid(row=0, column=0, ipadx=5, ipady=5)

b2 = tk.Button(window, bg = "yellow", text="Button2")
b2.grid(row=0, column=1, ipadx=5, ipady=5)

b3 = tk.Button(window, bg = "silver", text="Button3")
b3.grid(row=0, column=2, ipadx=5, ipady=5)

b4 = tk.Button(window, bg = "silver", text="Button4")
b4.grid(row=1, column=0, ipadx=5, ipady=5)

b5 = tk.Button(window, bg = "yellow", text="Button5")
b5.grid(row=1, column=1, ipadx=5, ipady=5)

b6 = tk.Button(window, bg = "silver", text="Button6")
b6.grid(row=1, column=2, ipadx=5, ipady=5)

b7 = tk.Button(window, bg = "silver", text="Button7")
b7.grid(row=2, column=0,columnspan=3, ipadx=5, ipady=5, sticky="EW")


=======
import tkinter as tk

window = tk.Tk()


b1 = tk.Button(window, bg = "red", text="Button1")
b1.grid(row=0, column=0, ipadx=5, ipady=5)

b2 = tk.Button(window, bg = "yellow", text="Button2")
b2.grid(row=0, column=1, ipadx=5, ipady=5)

b3 = tk.Button(window, bg = "silver", text="Button3")
b3.grid(row=0, column=2, ipadx=5, ipady=5)

b4 = tk.Button(window, bg = "silver", text="Button4")
b4.grid(row=1, column=0, ipadx=5, ipady=5)

b5 = tk.Button(window, bg = "yellow", text="Button5")
b5.grid(row=1, column=1, ipadx=5, ipady=5)

b6 = tk.Button(window, bg = "silver", text="Button6")
b6.grid(row=1, column=2, ipadx=5, ipady=5)

b7 = tk.Button(window, bg = "silver", text="Button7")
b7.grid(row=2, column=0,columnspan=3, ipadx=5, ipady=5, sticky="EW")


>>>>>>> d4f06d970b4d665710026f2d53dde28fad90b685
window.mainloop()