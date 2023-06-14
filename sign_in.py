from tkinter import *
import ttkbootstrap as tkboot


def login_window(parent):

    def transition_to_signup_page():
        signin_window.destroy()
        registration_window(signin_window)

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

    def password_enter_focus(event):
        if password_form.get() == "password":
            password_form.delete(0, END)
            password_form.configure(show="*", foreground="white")
            eyeButton.grid(row=2, column=0, padx=(0, 60), sticky="E")
        elif password_form.get() == "":
            password_form.insert(0, "password")
            password_form.configure(show="", foreground="grey")
            eyeButton.grid_forget()

    def show_password():
        close_eye_image.config(file="images/password/hide_password.png")
        password_form.config(show="*")
        eyeButton.config(command=hide_password)

    def hide_password():
        close_eye_image.config(file='images/password/view_password.png')
        password_form.config(show="")
        eyeButton.config(command=show_password)

    # creating signin window
    signin_window = tkboot.Toplevel()
    signin_window.geometry("600x440")
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

    # Login Label
    login_text = tkboot.Label(login_frame, text="SIGN IN", font=("", 20, "bold"), background="#20374C")
    login_text.grid(row=0, column=0, pady=20)

    # Username and password entries
    username_form = tkboot.Entry(login_frame, style="info", width=30, font=("", 12), foreground="grey")
    username_form.grid(row=1, column=0, pady=(0, 10), ipady=5)
    username_form.insert(0, 'username')
    username_form.bind("<FocusIn>", user_enter_focus)
    username_form.bind("<FocusOut>", user_enter_focus)

    password_form = tkboot.Entry(login_frame, style="info", width=30, font=("", 12), foreground="grey")
    password_form.grid(row=2, column=0, ipady=5)
    password_form.insert(0, "password")
    password_form.bind("<FocusIn>", password_enter_focus)
    password_form.bind("<FocusOut>", password_enter_focus)

    # Show/Hide password
    close_eye_image = PhotoImage(file='images/password/hide_password.png')
    eyeButton = tkboot.Button(login_frame,
                              style="dark",
                              takefocus=False,
                              image=close_eye_image,
                              cursor='hand2',
                              command=hide_password)

    forget_button = tkboot.Button(login_frame, text='Forgot password?', style="dark.TButton", takefocus=False,
                                  cursor='hand2')
    forget_button.grid(row=3, column=0, sticky="E", padx=(0, 100))

    # Login Button
    sign_in_button = tkboot.Button(login_frame,
                                   text="Sign In",
                                   style='success.TButton',
                                   takefocus=False,
                                   width=20,
                                   command=transition_to_main_window)
    sign_in_button.grid(row=4, column=0, pady=20, ipady=5)

    # Create new account block
    signupLabel = tkboot.Label(login_frame, style="dark.TLabel",
                               text="Don't have an account?",
                               foreground="white",
                               background="#20374C",
                               font=("", 9))
    signupLabel.grid(row=5, column=0, padx=(125, 0), pady=(0,10), sticky="W")

    new_account_button = tkboot.Button(login_frame,
                                       style="dark.TButton",
                                       text='Create New One',
                                       takefocus=False,
                                       cursor='hand2',
                                       command=transition_to_signup_page)
    new_account_button.grid(row=5, column=0, padx=(0, 125), pady=(0,10), sticky="E")

    # Set up layers
    signin_window.columnconfigure(0, weight=1)
    login_frame.columnconfigure(0, weight=1)


def registration_window(parent):

    def transition_to_signin_page():
        signup_window.destroy()
        login_window(signup_window)

    def transition_to_main_window():
        signup_window.destroy()
        parent.deiconify()


    def email_enter_focus(event):
        if user_email_form.get() == "Enter Email":
            user_email_form.delete(0, END)
            user_email_form.configure(foreground="white")
        elif user_email_form.get() == '':
            user_email_form.insert(0, "Enter Email")
            user_email_form.configure(foreground="grey")

    def user_enter_focus(event):
        if username_form.get() == "Enter Username":
            username_form.delete(0, END)
            username_form.configure(foreground="white")
        elif username_form.get() == '':
            username_form.insert(0, "Enter Username")
            username_form.configure(foreground="grey")

    def password_enter_focus(event):
        if password_form.get() == "Create Password":
            password_form.delete(0, END)
            password_form.configure(show="*", foreground="white")
            eyeButton_1.grid(row=6, column=0, padx=(0, 60), pady=(3, 0), sticky="EN")
        elif password_form.get() == "":
            password_form.insert(0, "Create Password")
            password_form.configure(show="", foreground="grey")
            eyeButton_1.grid_forget()

    def confirm_password_enter_focus(event):
        if confirm_password_password_form.get() == "Confirm Password":
            confirm_password_password_form.delete(0, END)
            confirm_password_password_form.configure(show="*", foreground="white")
            eyeButton_2.grid(row=8, column=0, padx=(0, 60), pady=(3, 0), sticky="EN")
        elif confirm_password_password_form.get() == "":
            confirm_password_password_form.insert(0, "Confirm Password")
            confirm_password_password_form.configure(show="", foreground="grey")
            eyeButton_2.grid_forget()

    def show_password():
        close_eye_image_1.config(file="images/password/hide_password.png")
        password_form.config(show="*")
        eyeButton_1.config(command=hide_password)

    def hide_password():
        close_eye_image_1.config(file='images/password/view_password.png')
        password_form.config(show="")
        eyeButton_1.config(command=show_password)

    def show_confirmed_password():
        close_eye_image_2.config(file="images/password/hide_confirmed_password.png")
        confirm_password_password_form.config(show="*")
        eyeButton_2.config(command=hide_confirmed_password)

    def hide_confirmed_password():
        close_eye_image_2.config(file='images/password/view_confirmed_password.png')
        confirm_password_password_form.config(show="")
        eyeButton_2.config(command=show_confirmed_password)


    # creating signin window
    signup_window = tkboot.Toplevel()
    signup_window.geometry("600x640")
    signup_window.title('Registration')
    # signup_window.protocol('WM_DELETE_WINDOW', parent.quit)


    # Style
    app_Style = tkboot.Style()
    app_Style.configure("dark.TButton",
                        font=("Microsoft Yeahei UI Light", 10, "bold underline"),
                        foreground="white",
                        background="#20374C")
    app_Style.configure("success.TButton", font=('', 12, "bold"))
    app_Style.configure("dark.TLabel")

    # Login Frame
    registration_frame = tkboot.Frame(signup_window, style="dark")
    registration_frame.grid(row=0, column=0, padx=50, pady=50, sticky="WE")

    # Login Label
    create_account_text = tkboot.Label(registration_frame,
                                       text="CREATE AN ACCOUNT",
                                       font=("", 20, "bold"),
                                       background="#20374C")
    create_account_text.grid(row=0, column=0, pady=20)

    # Email block
    user_email_text = tkboot.Label(registration_frame,
                                   text="Email",
                                   font=("", 12, "bold"),
                                   background="#20374C")
    user_email_text.grid(row=1, column=0, padx=(110,0), pady=(0, 3), sticky="W")

    user_email_form = tkboot.Entry(registration_frame, style="info", width=30, font=("", 12), foreground="grey")
    user_email_form.grid(row=2, column=0, pady=(0, 15), ipady=5)
    user_email_form.insert(0, 'Enter Email')
    user_email_form.bind("<FocusIn>", email_enter_focus)
    user_email_form.bind("<FocusOut>", email_enter_focus)

    # Username block
    username_text = tkboot.Label(registration_frame,
                                 text="Username",
                                 font=("", 12, "bold"),
                                 background="#20374C")
    username_text.grid(row=3, column=0, padx=(110,0), pady=(0, 3), sticky="W")

    username_form = tkboot.Entry(registration_frame, style="info", width=30, font=("", 12), foreground="grey")
    username_form.grid(row=4, column=0, pady=(0, 15), ipady=5)
    username_form.insert(0, 'Enter Username')
    username_form.bind("<FocusIn>", user_enter_focus)
    username_form.bind("<FocusOut>",user_enter_focus)

    # Password Block
    password_text = tkboot.Label(registration_frame,
                                 text="Password",
                                 font=("", 12, "bold"),
                                 background="#20374C")
    password_text.grid(row=5, column=0, padx=(110,0), pady=(0, 3), sticky="W")

    password_form = tkboot.Entry(registration_frame, style="info", width=30, font=("", 12), foreground="grey")
    password_form.grid(row=6, column=0, pady=(0, 15), ipady=5)
    password_form.insert(0, "Create Password")
    password_form.bind("<FocusIn>", password_enter_focus)
    password_form.bind("<FocusOut>", password_enter_focus)

    # Confirm Password Block
    confirm_password_text = tkboot.Label(registration_frame,
                                 text="Confirm Password",
                                 font=("", 12, "bold"),
                                 background="#20374C")
    confirm_password_text.grid(row=7, column=0, padx=(110,0), pady=(0, 3), sticky="W")

    confirm_password_password_form = tkboot.Entry(registration_frame, style="info", width=30, font=("", 12), foreground="grey")
    confirm_password_password_form.grid(row=8, column=0, pady=(0, 15), ipady=5)
    confirm_password_password_form.insert(0, "Confirm Password")
    confirm_password_password_form.bind("<FocusIn>", confirm_password_enter_focus)
    confirm_password_password_form.bind("<FocusOut>", confirm_password_enter_focus)

    # Show/Hide password
    close_eye_image_1 = PhotoImage(file='images/password/hide_password.png')
    eyeButton_1 = tkboot.Button(registration_frame,
                              style="dark",
                              takefocus=False,
                              image=close_eye_image_1,
                              cursor='hand2',
                              command=hide_password)

    # Show/Hide confirmed password
    close_eye_image_2 = PhotoImage(file='images/password/hide_confirmed_password.png')
    eyeButton_2 = tkboot.Button(registration_frame,
                              style="dark",
                              takefocus=False,
                              image=close_eye_image_2,
                              cursor='hand2',
                              command=hide_confirmed_password)


    # Registration Button
    sign_up_button = tkboot.Button(registration_frame,
                                   text="Sign Up",
                                   style='success.TButton',
                                   takefocus=False,
                                   width=20,
                                   command=transition_to_main_window)
    sign_up_button.grid(row=9, column=0, pady=20, ipady=5)

    signinLabel = tkboot.Label(registration_frame, style="dark.TLabel",
                               text="Do you already have an account?",
                               foreground="white",
                               background="#20374C",
                               font=("", 10))
    signinLabel.grid(row=10, column=0, padx=(115, 0), pady=(0,10), sticky="W")

    signin_button = tkboot.Button(registration_frame,
                                  style="dark.TButton",
                                  text='Sign In',
                                  takefocus=False,
                                  cursor='hand2',
                                  command=transition_to_signin_page)
    signin_button.grid(row=10, column=0, padx=(0, 120), pady=(0,10), sticky="E")

    signup_window.columnconfigure(0, weight=1)
    registration_frame.columnconfigure(0, weight=1)


