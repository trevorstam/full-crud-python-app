from tkinter import Tk, Button, Label, Scrollbar, Listbox, StringVar, Entry, W, E, N, S, END
from tkinter import ttk
from tkinter import messagebox

window = Tk()

# set dimensions and properties of the window
window.title("Books database app")
window.configure(background = "light cyan")
window.geometry("1000x500")
window.resizable(width = False, height = False)

# title search field
title_label = ttk.Label(window, text="Title", background = "burlywood3", font = ("TkDefaultFont", 16))
title_label.grid(row = 0, column = 0, sticky = W) # this puts it on row and column 0 (like table) and to the left (W)
title_text = StringVar() # this takes a string input
title_entry = ttk.Entry(window, width = 24, textvariable = title_text)
title_entry.grid(row = 0, column = 1, sticky = W)

# Author search field
author_label = ttk.Label(window, text = "Author", background = "burlywood3", font = ("TkDefaultFont", 16))
author_label.grid(row = 0, column = 2, sticky = W)
author_text = StringVar()
author_entry = ttk.Entry(window, width = 24, textvariable = author_text)
author_entry.grid(row = 0, column = 3, sticky = W)

# ISBN seach field
isbn_label = ttk.Label(window, text = "ISBN", background = "burlywood3", font = ("TkDefaultFont", 16))
isbn_label.grid(row = 0, column = 4, sticky = W)
isbn_text = StringVar()
isbn_entry = ttk.Entry(window, width = 24, textvariable = isbn_text)
isbn_entry.grid(row = 0, column = 5, sticky = W)

# Button to add books
add_btn = Button(window, text = "Add Book", bg = "blue", fg = "white", font = "helvetica 10 bold", command = "")
add_btn.grid(row = 0, column = 6, sticky = W)

# list box that shows all the books
list_bx = Listbox(window, height = 16, width = 40, font = "helvetica 13", background = "ghost white")
list_bx.grid(row = 3, column = 1, columnspan = 14, sticky = W + E, pady = 40, padx = 15)

# scroll bar on right of listbox to enable scrolling
scroll_bar = Scrollbar(window)
scroll_bar.grid(row = 1, column = 8, rowspan = 14, sticky = W)

list_bx.configure(yscrollcommand = scroll_bar.set) # command enables vertical scrolling
scroll_bar.configure(command = list_bx.yview) # yview makes listbox vertically scrollable

# Modify button
modify_btn = Button(window, text = "Modify Record", bg = "tomato3", fg = "white", font = "helvetica 10 bold", command = "")
modify_btn.grid(row = 15, column = 4)

# delete
delete_btn = Button(window, text = "Delete Record", bg = "red", fg = "white", font = "helvetica 10 bold", command = "")
delete_btn.grid(row = 15, column = 5)

view_btn = Button(window, text = "View all records", bg = "black", fg = "white", font = "helvetica 10 bold", command = "")
view_btn.grid(row = 15, column = 1)

clear_btn = Button(window, text = "Clear Screen", bg = "maroon", fg = "white", font = "helvetica 10 bold", command = "")
clear_btn.grid(row = 15, column = 2)

delete_btn = Button(window, text = "Exit Application", bg = "blue", fg = "white", font = "helvetica 10 bold", command = "")
delete_btn.grid(row = 15, column = 3)

window.mainloop()