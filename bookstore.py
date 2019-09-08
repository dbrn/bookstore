from tkinter import Tk, Button, Label, Listbox, Scrollbar, Entry
import backend


def main():
    root = Tk()
    backend.create()
    root.title("Bookstore manager")
    root.resizable(False, False)
    title_label = Label(root, text="Title")
    title_entry = Entry(root)
    author_label = Label(root, text="Author")
    author_entry = Entry(root)
    year_label = Label(root, text="Year")
    year_entry = Entry(root)
    isbn_label = Label(root, text="ISBN")
    isbn_entry = Entry(root)
    scroll = Scrollbar(root, orient="vertical", width=20)
    view_all = Button(root, text="View All", width=17,
                      command=lambda: backend.print_all(listbox))
    search_entry = Button(root, text="Search Entry", width=17,
                          command=lambda: backend.search(listbox,
                                                         title_entry.get(),
                                                         author_entry.get(),
                                                         year_entry.get(),
                                                         isbn_entry.get()))
    add_entry = Button(root, text="Add Entry", width=17,
                       command=lambda: backend.insert(listbox,
                                                      title_entry.get(),
                                                      author_entry.get(),
                                                      int(year_entry.get()),
                                                      int(isbn_entry.get())))
    update = Button(root, text="Update", width=17,
                    command=lambda: backend.update(listbox, title_entry,
                                                   author_entry,
                                                   year_entry,
                                                   isbn_entry))
    delete = Button(root, text="Delete", width=17,
                    command=lambda: backend.delete(listbox))
    close = Button(root, text="Close", width=17, command=root.quit)
    listbox = Listbox(root, height=12, width=27)
    listbox.configure(yscrollcommand=scroll.set)
    scroll.configure(command=listbox.yview)
    title_label.grid(row=0, column=0, padx=10)
    title_entry.grid(row=0, column=1, padx=10, pady=2)
    author_label.grid(row=0, column=2)
    author_entry.grid(row=0, column=3, padx=10)
    year_label.grid(row=1, column=0)
    year_entry.grid(row=1, column=1, padx=10)
    isbn_label.grid(row=1, column=2)
    isbn_entry.grid(row=1, column=3, padx=10, pady=2)
    listbox.grid(row=2, column=0, rowspan=6, columnspan=2, padx=2, pady=6)
    scroll.grid(row=2, column=2, rowspan=6)
    view_all.grid(row=2, column=3)
    search_entry.grid(row=3, column=3)
    add_entry.grid(row=4, column=3)
    update.grid(row=5, column=3)
    delete.grid(row=6, column=3)
    close.grid(row=7, column=3)
    root.mainloop()


if __name__ == "__main__":
    main()
