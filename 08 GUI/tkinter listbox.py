import tkinter as tk


window = tk.Tk()
scrollBar = tk.Scrollbar(window)
listBox = tk.Listbox(window, selectmode=tk.MULTIPLE)

scrollBar.pack(side=tk.RIGHT, fill=tk.Y)
listBox.pack(fill=tk.Y)
scrollBar.config(command=listBox.yview)
listBox.config(yscrollcommand=scrollBar.set)

for i in range(15):
    listBox.insert(tk.END, str(i))

label = tk.Label(window)
label.pack()

def checkList():
    selection = listBox.curselection()
    label.config(text=str(selection))
    label.after(300, checkList)

checkList()


window.mainloop()