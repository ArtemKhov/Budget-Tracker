from tkinter import *
import ttkbootstrap as tkboot


def login_window(parent):

    def transition_to_main_window():
        signin_window.destroy()
        parent.deiconify()

    def user_enter_focus(event):
        if username_form.get() == "username":
            username_form.delete(0, END)
            username_form.configure(foreground="white")
        elif username_form.get() == '':
            username_form.insert(0, "username")
            username_form.configure(foreground="grey")

    # creating signin window
    signin_window = tkboot.Toplevel()
    signin_window.geometry("600x360")
    signin_window.title('Login')
    # signin_window.protocol('WM_DELETE_WINDOW', parent.quit)

    # Style
    app_Style = tkboot.Style()
    app_Style.configure("dark.TButton",
                        font=("Microsoft Yeahei UI Light", 9, "bold underline"),
                        foreground="white",
                        background="#20374C")
    app_Style.configure("success.TButton", font=('', 12, "bold"))
    app_Style.configure("dark.TLabel")

    # Login Frame
    login_frame = tkboot.Frame(signin_window, style="dark")
    login_frame.grid(row=0, column=0, padx=50, pady=50, sticky="WE")

    # Welcome Label
    welcome_text = tkboot.Label(login_frame, text="Quick Start", font=("", 20, "bold"), background="#20374C")
    welcome_text.grid(row=0, column=0, pady=(20,5))

    # Instruction block
    instruction_text = tkboot.Label(login_frame,
                                    text="The username will be tied to your budget",
                                    font=("", 11),
                                    background="#20374C")
    instruction_text.grid(row=1, column=0, pady=(0, 20))

    # Username Block
    username_text = tkboot.Label(login_frame,
                                 text="Username",
                                 font=("", 12))
    username_text.grid(row=2, column=0, sticky="W", padx=107, pady=(0, 2))

    username_form = tkboot.Entry(login_frame, style="info", width=30, font=("", 12), foreground="grey")
    username_form.grid(row=3, column=0, pady=(0, 10), ipady=5)
    username_form.insert(0, 'username')
    username_form.bind("<FocusIn>", user_enter_focus)
    username_form.bind("<FocusOut>", user_enter_focus)

    # Login Button
    sign_in_button = tkboot.Button(login_frame,
                                   text="Start",
                                   style='success.TButton',
                                   takefocus=False,
                                   width=20,
                                   command=transition_to_main_window)
    sign_in_button.grid(row=4, column=0, pady=20, ipady=5)

    # Set up layers
    signin_window.columnconfigure(0, weight=1)
    login_frame.columnconfigure(0, weight=1)

