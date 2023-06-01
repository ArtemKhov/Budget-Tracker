import sqlite3
from tkinter import *
from tkinter import ttk
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

    def update(self, id, product, price):
        self.cur.execute("UPDATE purchases SET product=?, price=? WHERE id=?", (product, price, id,))
        self.conn.commit()

    def delete(self, id):
        self.cur.execute("DELETE FROM purchase WHERE id=?", (id,))
        self.conn.commit()

    def search(self, product="", price=""):
        self.cur.execute("SELECT * FROM purchase WHERE product=?", (product,))
        rows = self.cur.fetchall()
        return rows


def add_entry():
    budget.insert(product_text.get(), price_text.get(), comment_text.get(), category_text.get())
    show_all_entries()
    focus_to_last_row()


def show_all_entries():
    tree.delete(*tree.get_children())

    for row in budget.view():
        tree.insert("", END, values=row)


def focus_to_last_row():
    child_id = tree.get_children()[-1]
    tree.focus(child_id)
    tree.selection_set(child_id)
    tree.yview_moveto(1)


budget = Budget()

window = tkboot.Window(themename="superhero")

# Create Labels
title_label = Label(window, text="Title")
title_label.grid(row=0, column=0, padx=20, sticky="W")

price_label = Label(window, text="Price")
price_label.grid(row=1, column=0, padx=20, sticky="W")

comment_label = Label(window, text="Category")
comment_label.grid(row=2, column=0, padx=20, sticky="W")

category_label = Label(window, text="Comment")
category_label.grid(row=3, column=0, padx=20, sticky="W")

# Create Entries
product_text = StringVar()
title_entry = Entry(window, textvariable=product_text)
title_entry.grid(row=0, column=0, columnspan=2, padx=(110, 0), sticky="EW")

price_text = StringVar()
price_entry = Entry(window, textvariable=price_text)
price_entry.grid(row=1, column=0, columnspan=2, padx=(110, 0), sticky="EW")

category_text = StringVar()
category_entry = Entry(window, textvariable=category_text)
category_entry.grid(row=2, column=0, columnspan=2, padx=(110, 0), sticky="EW")

comment_text = StringVar()
comment_entry = Entry(window, textvariable=comment_text)
comment_entry.grid(row=3, column=0, columnspan=2, padx=(110, 0), sticky="EW")



# Create Buttons
add_button = tkboot.Button(window, text="Add", width=15, style="success", takefocus=False, command=add_entry)
add_button.grid(row=5, column=3)

show_all_button = tkboot.Button(text="Show All", width=15, takefocus=False, command=show_all_entries)
show_all_button.grid(row=6, column=3)

search_button = tkboot.Button(text="Search", width=15, takefocus=False)
search_button.grid(row=7, column=3)

update_button = tkboot.Button(text="Update", width=15, takefocus=False)
update_button.grid(row=8, column=3)

remove_button = tkboot.Button(text="Delete", width=15, takefocus=False)
remove_button.grid(row=9, column=3)

# Create Budget Table
tree = ttk.Treeview(window, columns=("c1", "c2", "c3", "c4", "c5"), show="headings", style="info")

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

tree.grid(row=5, column=0, columnspan=2, rowspan=5)


def get_selected_row(event):

    title_entry.delete(0, END)
    price_entry.delete(0, END)
    category_entry.delete(0, END)
    comment_entry.delete(0, END)

    selected = tree.focus()
    values = tree.item(selected, "values")

    title_entry.insert(0, values[1])
    price_entry.insert(0, values[2])
    category_entry.insert(0, values[3])
    comment_entry.insert(0, values[4])

# Show values in Entries box when row is selected
tree.bind("<ButtonRelease-1>", get_selected_row)



window.mainloop()


