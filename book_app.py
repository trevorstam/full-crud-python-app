from tkinter import Tk, Button, Label, Scrollbar, Listbox, StringVar, Entry, W, E, N, S, END
from tkinter import ttk
from tkinter import messagebox

window = Tk()

# set dimensions and properties of the window
window.title("Books database app")
window.configure(background = "light cyan")
window.geometry("850x500")
window.resizable(width = False, height = False)

# title search field
title_label = ttk.Label(window, text="Title", background = "burlywood3", font = ("TkDefaultFont", 16))
title_label.grid(row = 0, column = 0, sticky = W) # this puts it on row and column 0 (like table) and to the left (W)
title_text = StringVar() # this takes a string input
title_entry = ttk.Entry(window, width = 24, textvariable = title_text)
title_entry.grid(row = 0, column = 1, sticky = W)

# Author search field
author_label = ttk.Label(window, text = "Author", background = "burlywood3", font = ("TkDefaultFont", 16))
author_label.grid(row = 0, column = 4, sticky = W)
author_text = StringVar()
author_entry = ttk.Entry(window, width = 24, textvariable = author_text)
author_entry.grid(row = 0, column = 5, sticky = W)

# ISBN seach field
isbn_label = ttk.Label(window, text = "ISBN", background = "burlywood3", font = ("TkDefaultFont", 16))
isbn_label.grid(row = 0, column = 7, sticky = W)
isbn_text = StringVar()
isbn_entry = ttk.Entry(window, width = 24, textvariable = isbn_text)
isbn_entry.grid(row = 0, column = 8, sticky = W)


window.mainloop()