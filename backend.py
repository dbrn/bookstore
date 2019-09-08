# backend
import sqlite3
from tkinter import END


def print_list(listbox, data):
    listbox.delete(0, END)
    for piece in data:
        book = ""
        for info in piece:
            book += str(info) + ", "
        listbox.insert(END, book.rstrip(", "))


def create():
    connection = sqlite3.connect("books.db")
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS bookstore "
                   "(id INTEGER UNIQUE PRIMARY KEY AUTOINCREMENT, title TEXT,"
                   "author TEXT, year INTEGER, isbn INTEGER);")
    connection.commit()
    connection.close()


def print_all(listbox):
    connection = sqlite3.connect("books.db")
    cursor = connection.cursor()
    data = cursor.execute("SELECT * FROM bookstore;")
    data = data.fetchall()
    print_list(listbox, data)
    connection.close()


def insert(listbox, title, author, year, isbn):
    connection = sqlite3.connect("books.db")
    cursor = connection.cursor()
    cursor.execute(f"INSERT INTO bookstore(title, author, year, isbn) "
                   f"VALUES('{title}', '{author}', {year}, {isbn});")
    connection.commit()
    connection.close()
    search(listbox, title, author, year, isbn)


def search(listbox, title="", author="", year="", isbn=""):
    connection = sqlite3.connect("books.db")
    cursor = connection.cursor()
    data = cursor.execute("SELECT * FROM bookstore WHERE title=? OR author=? "
                          "OR year=? OR isbn=?;", (title, author, year, isbn))
    data = data.fetchall()
    print_list(listbox, data)
    connection.close()


def delete(listbox):
    selected_item = listbox.get(listbox.curselection())
    connection = sqlite3.connect("books.db")
    cursor = connection.cursor()
    cursor.execute("DELETE FROM bookstore WHERE id=?", (selected_item[0]))
    connection.commit()
    connection.close()
    listbox.delete(listbox.curselection())


def update(listbox, title, author, year, isbn):
    selected_item = listbox.get(listbox.curselection())
    selected_array = selected_item.split(", ")
    if title.get() == "":
        title.insert(END, selected_array[1])
    if author.get() == "":
        author.insert(END, selected_array[2])
    if year.get() == "":
        year.insert(END, selected_array[3])
    if isbn.get() == "":
        isbn.insert(END, selected_array[4])
    connection = sqlite3.connect("books.db")
    cursor = connection.cursor()
    cursor.execute("UPDATE bookstore SET title=?, author=?, year=?, "
                   "isbn=? WHERE id=?",
                   (title.get(), author.get(), year.get(), isbn.get(),
                    selected_array[0]))
    connection.commit()
    connection.close()
    print_all(listbox)
