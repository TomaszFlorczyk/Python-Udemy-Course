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
window.mainloop()