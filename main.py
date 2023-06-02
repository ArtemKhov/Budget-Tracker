import sqlite3
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import ttkbootstrap as tkboot
from ttkbootstrap.constants import *

class Budget:
    def __init__(self):
        self.conn = sqlite3.connect("budget.db")
        self.cur = self.conn.cursor()

        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS purchases (id INTEGER PRIMARY KEY, product TEXT, price TEXT, category TEXT, comment TEXT)"
        )

        self.conn.commit()

    def __del__(self):
        self.conn.close()

    def view(self):
        self.cur.execute("SELECT * FROM purchases")
        rows = self.cur.fetchall()
        return rows

    def insert(self, product, price, category, comment):
        self.cur.execute("INSERT INTO purchases VALUES (NULL,?,?,?,?)", (product, price, category, comment,))
        self.conn.commit()

    def update(self, id, product, price, category, comment):
        self.cur.execute("UPDATE purchases SET product=?, price=?, category=?, comment=? WHERE id=?",
                         (product, price, category, comment, id,))
        self.conn.commit()

    def delete_row(self, id):
        self.cur.execute("DELETE FROM purchases WHERE id=?", (id,))
        self.conn.commit()

    def delete_all_rows(self):
        self.cur.execute("DELETE FROM purchases")
        self.conn.commit()

    def search(self, product="", price="", category=""):
        self.cur.execute("SELECT * FROM purchases WHERE product like ? OR price like ? OR category=?",
                         (product, price, category,))
        rows = self.cur.fetchall()
        return rows


def add_record():
    if product_text.get() == "":
        messagebox.showwarning(title="Empty Title", message="Title can not be empty!")
    elif price_text.get() == "":
        messagebox.showwarning(title="Empty Price", message="Price can not be empty!")
    elif category_combobox.get() == "":
        messagebox.showwarning(title="Empty Category", message="Category can not be empty!")
    else:
        budget.insert(product_text.get(), price_text.get(), category_combobox.get(), comment_text.get())
        show_table()
        focus_to_last_row()
        clear_all_entries()


def show_table():
    clear_table()

    for row in budget.view():
        tree.insert("", END, values=row)


def search_row():
    clear_table()

    for row in budget.search(product_text.get(), price_text.get(), category_combobox.get()):
        tree.insert("", END, values=row)

    clear_all_entries()


def update_record():
    selected = tree.focus()
    values = tree.item(selected, "values")

    budget.update(values[0], title_entry.get(), price_entry.get(), category_combobox.get(), comment_entry.get())

    clear_all_entries()
    show_table()


def delete_record():
    try:
        selected = tree.focus()
        values = tree.item(selected, "values")

        budget.delete_row(values[0])
        show_table()
    except IndexError:
        pass


def delete_all_records():
    budget.delete_all_rows()
    show_table()


def focus_to_last_row():
    child_id = tree.get_children()[-1]
    tree.focus(child_id)
    tree.selection_set(child_id)
    tree.yview_moveto(1)


def clear_all_entries():
    title_entry.delete(0, END)
    price_entry.delete(0, END)
    category_combobox.set("")
    comment_entry.delete(0, END)


def clear_table():
    tree.delete(*tree.get_children())


def open_categories_file():
    with open("budget_categories/categories.txt", "r", encoding="UTF-8") as file:
        categories = file.read().splitlines()
        return categories


budget = Budget()

window = tkboot.Window(themename="superhero")

# Create Labels
title_label = Label(window, text="Title*")
title_label.grid(row=0, column=0, padx=20, sticky="W")

price_label = Label(window, text="Price*")
price_label.grid(row=1, column=0, padx=20, sticky="W")

comment_label = Label(window, text="Category*")
comment_label.grid(row=2, column=0, padx=20, sticky="W")

category_label = Label(window, text="Comment")
category_label.grid(row=3, column=0, padx=20, sticky="W")

# Create Entries
product_text = StringVar()
title_entry = tkboot.Entry(window, textvariable=product_text)
title_entry.grid(row=0, column=0, columnspan=3, padx=(110, 12), sticky="EW")

price_text = StringVar()
price_entry = tkboot.Entry(window, textvariable=price_text)
price_entry.grid(row=1, column=0, columnspan=3, padx=(110, 12), sticky="EW")

comment_text = StringVar()
comment_entry = tkboot.Entry(window, textvariable=comment_text)
comment_entry.grid(row=3, column=0, columnspan=3, padx=(110, 12), sticky="EW")

# Create Combobox
categories = open_categories_file()
category_combobox = tkboot.Combobox(values=categories, state="readonly")
category_combobox.grid(row=2, column=0, columnspan=3, padx=(110, 12), sticky="EW")

# Create Buttons
add_button = tkboot.Button(window, text="Add Record", width=15, style="success", takefocus=False, command=add_record)
add_button.grid(row=0, column=4)

show_all_button = tkboot.Button(text="Show All", width=15, takefocus=False, command=show_table)
show_all_button.grid(row=6, column=4)

search_button = tkboot.Button(text="Search", width=15, takefocus=False, command=search_row)
search_button.grid(row=7, column=4)

update_button = tkboot.Button(text="Update Record", width=15, takefocus=False, command=update_record)
update_button.grid(row=8, column=4)

remove_record_button = tkboot.Button(text="Remove Selected Record", width=25, takefocus=False, command=delete_record)
remove_record_button.grid(row=10, column=1, padx=(250,0), sticky="E")

remove_all_records_button = tkboot.Button(text="Remove All Records", width=20, takefocus=False, command=delete_all_records)
remove_all_records_button.grid(row=10, column=2)


# Create Budget Table
tree_frame = Frame(window)
tree_frame.grid(row=5, column=0, columnspan=3, rowspan=5, pady=10, padx=(0, 20))

tree_scroll = tkboot.Scrollbar(tree_frame, style="info-round")
tree_scroll.grid(row=0, column=1, rowspan=5, sticky="NS")

tree = ttk.Treeview(tree_frame, columns=("c1", "c2", "c3", "c4", "c5"), yscrollcommand=tree_scroll.set, show="headings", style="info")
tree.column("#1", anchor=CENTER, width=50)
tree.heading("#1", text="ID")

tree.column("#2", anchor=CENTER)
tree.heading("#2", text="Title")

tree.column("#3", anchor=CENTER)
tree.heading("#3", text="Price")

tree.column("#4", anchor=CENTER)
tree.heading("#4", text="Category")

tree.column("#5", anchor=CENTER)
tree.heading("#5", text="Comment")

tree.grid(row=0, column=0)
tree_scroll.configure(command=tree.yview)


def get_selected_row(event):
    clear_all_entries()

    try:
        selected = tree.focus()
        values = tree.item(selected, "values")

        title_entry.insert(0, values[1])
        price_entry.insert(0, values[2])
        category_combobox.set(values[3])
        comment_entry.insert(0, values[4])
    except IndexError:
        pass

# Show values in Entries box when row is selected
tree.bind("<ButtonRelease-1>", get_selected_row)


# Show the whole table when app is launched
show_table()
window.configure(pady=10, padx=10)
window.mainloop()


