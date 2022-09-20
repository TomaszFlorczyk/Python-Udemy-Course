import tkinter as tk

window = tk.Tk()

value = tk.DoubleVar()
scale = tk.Scale(window, from_= 0, to=60, orient=tk.VERTICAL, variable=value)

scale.pack(anchor=tk.CENTER)

label = tk.Label(window)
label.pack()

def selected():
    selection = "Value: " + str(value.get())
    label.config(text= selection)
    label.after(200, selected)


selected()

window.mainloop()