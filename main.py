from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter.font as TkFont
import ttkbootstrap as tkboot
from ttkbootstrap.constants import *
from PIL import Image, ImageTk
import pandas as pd
import plotly.express as px
from budget_db import Budget
from welcome_screen import login_window


def main_window():

    def add_record():
        if product_text.get() == "":
            messagebox.showwarning(title="Empty Title", message="Title can not be empty!")
        elif int(len(product_text.get())) > 32:
            messagebox.showwarning(title="Too long", message="The Title cannot be longer than 32 characters")
        elif price_text.get() == "":
            messagebox.showwarning(title="Empty Price", message="Price can not be empty!")
        elif category_combobox.get() == "":
            messagebox.showwarning(title="Empty Category", message="Category can not be empty!")
        elif int(len(comment_text.get())) > 175:
            messagebox.showwarning(title="Too long", message="The Comment cannot be longer than 175 characters")
        else:
            budget.insert(product_text.get(), price_text.get(), category_combobox.get(), comment_text.get())
            show_table()
            focus_to_the_last_row()
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
        if product_text.get() == "" or price_text.get() == "" or category_combobox.get() == "":
            messagebox.showwarning(title='Empty Fields', message="Select the record and fill in the *required fields")
        elif int(len(product_text.get())) > 32:
            messagebox.showwarning(title="Too long", message="The Title cannot be longer than 32 characters")
        elif int(len(comment_text.get())) > 175:
            messagebox.showwarning(title="Too long", message="The Comment cannot be longer than 175 characters")
        else:
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
        warning = messagebox.askokcancel(title="Confirmation",
                                         message="Are you sure you want to delete all data?")

        if warning:
            budget.delete_all_rows()
            show_table()


    def focus_to_the_last_row():
        try:
            child_id = tree.get_children()[-1]
            tree.focus(child_id)
            tree.selection_set(child_id)
            tree.yview_moveto(1)
        except IndexError:
            pass


    def clear_all_entries():
        title_entry.delete(0, END)
        price_entry.delete(0, END)
        category_combobox.set("")
        comment_entry.delete(0, END)


    def clear_table():
        tree.delete(*tree.get_children())


    def disable_expand_tree_columns(event):
        if tree.identify_region(event.x, event.y) == "separator":
            return "break"


    def open_categories_file():
        with open("budget_categories/categories.txt", "r", encoding="UTF-8") as file:
            categories = file.read().splitlines()
            return categories


    def switch_to_home():
        home_frame.grid(row=0, column=1, pady=(20, 10))
        graph_frame.grid_forget()


    def switch_to_graph():
        if budget.view() == []:
            messagebox.showwarning(title="Empty Table",
                                   message="There's nothing in the purchases."
                                           "\n\nAdd your purchase records in Home menu to form a Graph.")
        else:
            graph_frame.grid(row=0, column=1, pady=(20, 10))
            home_frame.grid_forget()
            create_pie_chart()
            update_chart_image()


    def summarize_prices_by_category():
        data = budget.conn
        df = pd.read_sql_query("SELECT * FROM purchases", data)

        # group category columns and show sum of the values from the Price field
        category_sum_price = df.groupby("category")["price"].sum()

        return category_sum_price


    def create_pie_chart():
        fig = px.pie(title="Total amount of money spent by category",
                     values=summarize_prices_by_category().values,
                     names=summarize_prices_by_category().index,
                     hole=0.3)
        fig.update_traces(textinfo="value+label", textfont_color="white")
        fig.update_layout(margin=dict(t=50, b=20, l=20, r=20), paper_bgcolor='#2b3e50', font=dict(color="white"))
        fig.write_image("pie_chart/pie_budget.png")


    # Update image into Canvas every time when update any values in the DataBase
    def update_chart_image():
        pie_chart_img.configure(file="pie_chart/pie_budget.png")
        canvas.itemconfig(image_container, image=pie_chart_img)



    budget = Budget()

    window = tkboot.Window(themename="superhero")
    window.title("Budget Tracker")
    window.resizable(False, False)
    window.iconbitmap(bitmap="images/app_logo.ico")
    window.iconbitmap(default="images/app_logo.ico")

    HOME_LABELS_FONT = ("", 12, "bold")
    HOME_ENTRIES_FONT = ("", 11)
    TREEVIEW_HEADINGS_FONT = ("", 10, "bold")
    TREEVIEW_ROW_FONT = ("", 10)

    # Style
    app_Style = tkboot.Style()
    # Style Sidebar's buttons
    app_Style.configure("primary.TButton", font=("", 14, "bold"), foreground="white")
    # Style Sidebar logo
    app_Style.configure("TLabel", background="#20374C")
    # Style Table Headings and Rows
    app_Style.configure("info.Treeview.Heading", font=TREEVIEW_HEADINGS_FONT, foreground="black")
    app_Style.configure("info.Treeview", font=TREEVIEW_ROW_FONT, rowheight=22)
    # Style primary buttons in home sections
    app_Style.configure("TButton", font=("", 12, "bold"))
    # Style Font In the Listbox (Combobox)
    listbox_font = TkFont.Font(None, size=11)
    window.option_add("*TCombobox*Listbox*Font", listbox_font)


    # Sidebar Frame
    sidebar_frame = tkboot.Frame(window, style="dark")
    sidebar_frame.grid(row=0, column=0, ipadx=30, padx=(0,10), sticky="NSW")

    # Sidebar Logo
    image = Image.open("images/sidebar/logo_sidebar.png")
    img = image.resize((128, 128))
    logo_image = ImageTk.PhotoImage(img)
    logo_sidebar = tkboot.Label(sidebar_frame, image=logo_image)
    logo_sidebar.grid(row=0, column=0, pady=(20, 45))

    # Sidebar Buttons
    image_home = Image.open("images/sidebar/home.png")
    img_home = image_home.resize((42, 42))
    home_image = ImageTk.PhotoImage(img_home)
    home_button = tkboot.Button(sidebar_frame,
                                    text="Home",
                                    takefocus=False,
                                    style="primary.TButton",
                                    image=home_image,
                                    compound=LEFT,
                                    command=switch_to_home)
    home_button.grid(row=1, column=0, sticky="WE", padx=10)

    image_graph = Image.open("images/sidebar/pie-chart.png")
    img_graph = image_graph.resize((42, 42))
    graph_image = ImageTk.PhotoImage(img_graph)
    graph_button = tkboot.Button(sidebar_frame,
                                 text="Graph",
                                 takefocus=False,
                                 style="primary.TButton",
                                 image=graph_image,
                                 compound=LEFT,
                                 command=switch_to_graph)
    graph_button.grid(row=2, column=0, pady=20, sticky="WE", padx=10)



    # Graph Frame
    graph_frame = Frame(window)

    # Create Canvas container for Pie Chart
    canvas = Canvas(graph_frame, width=750, height=550)
    canvas.grid(row=0, column=0)
    pie_chart_img = PhotoImage(file="pie_chart/pie_budget.png")
    image_container = canvas.create_image(350, 250, image=pie_chart_img)


    # home Frame
    home_frame = tkboot.Frame(window)
    home_frame.grid(row=0, column=1, pady=(20, 10))

    # Create home Labels
    title_label = Label(home_frame, text="Title*", font=HOME_LABELS_FONT)
    title_label.grid(row=0, column=0, sticky="W", pady=(0, 10))

    price_label = Label(home_frame, text="Price*", font=HOME_LABELS_FONT)
    price_label.grid(row=1, column=0, sticky="W", pady=(0, 10))

    category_label = Label(home_frame, text="Category*", font=HOME_LABELS_FONT)
    category_label.grid(row=2, column=0, sticky="W", pady=(0, 10))

    comment_label = Label(home_frame, text="Comment", font=HOME_LABELS_FONT)
    comment_label.grid(row=3, column=0, sticky="W")

    required_fields_label = Label(home_frame, text="* required fields")
    required_fields_label.grid(row=4, column=0, padx=(110,0), sticky="W")

    # Create home Entries
    product_text = StringVar()
    title_entry = tkboot.Entry(home_frame, textvariable=product_text, font=HOME_ENTRIES_FONT)
    title_entry.grid(row=0, column=0, padx=(110, 12), pady=(0, 10), sticky="EW")

    price_text = StringVar()
    price_entry = tkboot.Entry(home_frame, textvariable=price_text, font=HOME_ENTRIES_FONT)
    price_entry.grid(row=1, column=0, padx=(110, 12), pady=(0, 10), sticky="EW")

    comment_text = StringVar()
    comment_entry = tkboot.Entry(home_frame, textvariable=comment_text, font=HOME_ENTRIES_FONT)
    comment_entry.grid(row=3, column=0, padx=(110, 12), sticky="EW")

    # Create home Combobox
    categories = open_categories_file()
    category_combobox = ttk.Combobox(home_frame, values=categories, font=HOME_ENTRIES_FONT, state="readonly")
    category_combobox.grid(row=2, column=0, padx=(110, 12), pady=(0, 10), sticky="EW")

    # Create home Buttons
    add_button = tkboot.Button(home_frame, text="Add Record", width=15, style="success", takefocus=False, command=add_record)
    add_button.grid(row=1, column=1, rowspan=2, padx=(0, 10), ipady=5)

    show_all_button = tkboot.Button(home_frame, text="Show All", width=15, takefocus=False, command=show_table)
    show_all_button.grid(row=6, column=1, padx=(0, 10))

    search_button = tkboot.Button(home_frame, text="Search", width=15, takefocus=False, command=search_row)
    search_button.grid(row=7, column=1, padx=(0, 10))

    update_button = tkboot.Button(home_frame, text="Update Record", width=15, takefocus=False, command=update_record)
    update_button.grid(row=8, column=1, padx=(0, 10))

    remove_record_button = tkboot.Button(home_frame, text="Remove Selected Record", width=25, takefocus=False, command=delete_record)
    remove_record_button.grid(row=10, column=0, padx=(0, 250), sticky="E")

    remove_all_records_button = tkboot.Button(home_frame, text="Remove All Records", width=20, takefocus=False, command=delete_all_records)
    remove_all_records_button.grid(row=10, column=0,  padx=(0, 25), sticky="E")

    # Create home Budget Table
    tree_frame = Frame(home_frame)
    tree_frame.grid(row=5, column=0, rowspan=5, pady=(10, 15), padx=(0, 10))

    tree_vertical_scroll = tkboot.Scrollbar(tree_frame, style="info-round")
    tree_vertical_scroll.grid(row=0, column=1, rowspan=5, sticky="NS")

    tree_horizontal_scroll = tkboot.Scrollbar(tree_frame, style="info-round", orient=HORIZONTAL)
    tree_horizontal_scroll.grid(row=6, column=0, rowspan=5, sticky="WE")

    tree = ttk.Treeview(tree_frame,
                        columns=("c1", "c2", "c3", "c4", "c5"),
                        yscrollcommand=tree_vertical_scroll.set,
                        xscrollcommand=tree_horizontal_scroll.set,
                        height=20,
                        show="headings",
                        selectmode="browse",
                        style="info")

    tree.column("#1", anchor=CENTER, width=50, stretch=False)
    tree.heading("#1", text="ID")

    tree.column("#2", anchor=CENTER, stretch=False)
    tree.heading("#2", text="Title")

    tree.column("#3", anchor=CENTER, width=50, stretch=False)
    tree.heading("#3", text="Price")

    tree.column("#4", anchor=CENTER, stretch=False)
    tree.heading("#4", text="Category")

    tree.column("#5", anchor=W, minwidth=1000, stretch=True)
    tree.heading("#5", text="Comment", anchor=W)

    tree.grid(row=0, column=0)

    tree_vertical_scroll.configure(command=tree.yview)
    tree_horizontal_scroll.configure(command=tree.xview)

    # Show values in Entries box when row is selected
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

    tree.bind("<ButtonRelease-1>", get_selected_row)
    tree.bind("<Button-1>", disable_expand_tree_columns)


    # Show the whole table when app is launched
    show_table()


    window.columnconfigure(0, weight=1)
    sidebar_frame.columnconfigure(0, weight=1)

    window.withdraw()
    login_window(window)
    window.mainloop()



if __name__ == '__main__':
    main_window()