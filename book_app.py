from tkinter import Tk, Button, Label, Scrollbar, Listbox, StringVar, Entry, W, E, N, S, END
from tkinter import ttk
from tkinter import messagebox

import pyodbc as pyo

import os
from dotenv import load_dotenv
load_dotenv()

connection_string = os.getenv('CONNECTION_STRING')

conn = pyo.connect(connection_string) # double asterisk signifies dictionary, will extract and pass it parameters
print(conn)

cursor = conn.cursor()

class Bookdb:
    def __init__(self):
        self.conn = pyo.connect(connection_string)
        self.cursor = conn.cursor()
        print('You have established a connection with the database')
        print(conn)

    def __del__(self):
        self.conn.close()
    
    def view(self):
        self.cursor.execute('SELECT * FROM book')
        rows = self.cursor.fetchall()
        return rows
    
    def insert(self, title, author, isbn):
        insert_query = 'INSERT INTO book(title, author, isbn)VALUES (?,?,?)'
        values = (title, author, isbn)
        self.cursor.execute(insert_query, values)
        self.conn.commit()
        messagebox.showinfo(title='Book Database', message='New book added to db')

    def update(self, id, title, author, isbn):
        update_query = 'UPDATE book SET title = ? author = ? isbn = ? where id = ?'
        values = (title, author, isbn, id)
        self.cursor.execute(update_query, values)
        self.conn.commit()
        messagebox.showinfo(title='Book Database', message='DB record is updated')
    
    def delete(self, id):
        del_query = 'DELETE FROM book WHERE id = ?'
        values = (id)
        self.cursor.execute(del_query, values)
        self.conn.commit()
        messagebox.showinfo(title='Book Database', message='DB record deleted')

db = Bookdb()

# this is a function that interacts with the rows within the listbox
def get_selected_row(event):
    # if you want to modify a variable outside of the function scope 
    # you need to add global before the variable
    global selected_tuple
    # set the index to the listbox's current selection at the very first element
    # curselection creates a list and index. It is a method of tkinter
    index = list_bx.curselection()[0]
    # assign to variable tuple selection <- get value at index of listbox
    selected_tuple = list_bx.get(index)
    # method to clear entry box before listbox is populated with entries
    # when clicking on list_box records
    title_entry.delete(0, 'end')
    title_entry.insert('end', selected_tuple[1])
    author_entry.delete(0, 'end')
    author_entry.insert('end', selected_tuple[2])
    isbn_entry.delete(0, 'end')
    isbn_entry.insert('end', selected_tuple[3])


def view_records():
    # it should first clear the list box
    list_bx.delete(0, 'end')
    # it should iterate over each row in the db view
    # and then insert in the listbox (it interacts with the function in the bookDB class)
    for row in db.view():
        list_bx.insert('end', row)

def add_book():
    # it uses the insert method from bookdb class and inserts a title, author and isbn
    # and grabs values from the text
    db.insert(title_text.get(), author_text.get(), isbn_text.get())
    # first the list box needs to be cleared
    list_bx.delete(0, 'end')
    # then all info needs to get inserted into list_box
    list_bx.insert('end',(title_text.get(), author_text.get(), isbn_text.get()))
    # then input from input boxes above need to be cleared after inserting
    title_entry.delete(0, 'end')
    author_entry.delete(0, 'end')
    isbn_entry.delete(0, 'end')
    # finally the connection needs to be committed
    conn.commit()

def delete_records():
    # it should delete records from the instantiated bookDB
    db.delete(selected_tuple[0])
    # connection needs to be committed
    conn.commit()

def clear_screen():
    # delete entries from listbox
    list_bx.delete(0, 'end')
    #delete entries from each input box
    title_entry.delete(0, 'end')
    author_entry.delete(0, 'end')
    isbn_entry.delete(0, 'end')

def update_records():
    # update db instance get the info from text for the selected record
    db.update(selected_tuple[0], title_text.get(), author_text.get(), isbn_text.get())
    # clear input after inserting for each input box
    title_entry.delete(0, 'end')
    author_entry.delete(0, 'end')
    isbn_entry.delete(0, 'end')
    # commit connection
    conn.commit()

def on_closing():
    # create a variable destroy_db and set it to db
    destroy_db = db
    # check if message box isokcancel
    # if so then destroy() window
    # and delete destroy_db
    if messagebox.askokcancel('Quit', 'Do you want to quit?'):
        window.destroy()
        del destroy_db

   

###############################################
##GUI
###############################################

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
add_btn = Button(window, text = "Add Book", bg = "blue", fg = "white", font = "helvetica 10 bold", command = add_book)
add_btn.grid(row = 0, column = 6, sticky = W)

# list box that shows all the books
list_bx = Listbox(window, height = 16, width = 40, font = "helvetica 13", background = "ghost white")
list_bx.grid(row = 3, column = 1, columnspan = 14, sticky = W + E, pady = 40, padx = 15)
list_bx.bind('<<ListboxSelect>>', get_selected_row)


# scroll bar on right of listbox to enable scrolling
scroll_bar = Scrollbar(window)
scroll_bar.grid(row = 1, column = 8, rowspan = 14, sticky = W)

list_bx.configure(yscrollcommand = scroll_bar.set) # command enables vertical scrolling
scroll_bar.configure(command = list_bx.yview) # yview makes listbox vertically scrollable

# Modify button
modify_btn = Button(window, text = "Modify Record", bg = "tomato3", fg = "white", font = "helvetica 10 bold", command = update_records)
modify_btn.grid(row = 15, column = 4)

# delete
delete_btn = Button(window, text = "Delete Record", bg = "red", fg = "white", font = "helvetica 10 bold", command = delete_records)
delete_btn.grid(row = 15, column = 5)

view_btn = Button(window, text = "View all records", bg = "black", fg = "white", font = "helvetica 10 bold", command = view_records)
view_btn.grid(row = 15, column = 1)

clear_btn = Button(window, text = "Clear Screen", bg = "maroon", fg = "white", font = "helvetica 10 bold", command = clear_screen)
clear_btn.grid(row = 15, column = 2)

destroy_btn = Button(window, text = "Exit Application", bg = "blue", fg = "white", font = "helvetica 10 bold", command = on_closing)
destroy_btn.grid(row = 15, column = 3)

window.mainloop()