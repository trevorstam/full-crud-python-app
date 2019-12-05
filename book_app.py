from tkinter import Tk, Button, Label, Scrollbar, Listbox, StringVar, Entry, W, E, N, S, END
from tkinter import ttk
from tkinter import messagebox

window = Tk()

# set dimensions and properties of the window
window.title("Books database app")
window.configure(background = "light cyan")
window.geometry("850x500")
window.resizable(width = False, height = False)

window.mainloop()