from tkinter import *
import ttkbootstrap as tkboot

def login_window(parent):

    def transition_to_signup_page():
        signin_window.destroy()
        parent.deiconify()

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
    signin_window.protocol('WM_DELETE_WINDOW', parent.quit)

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
                                       cursor='hand2')
                                       # command=signup_page)
    new_account_button.grid(row=5, column=0, padx=(0, 125), pady=(0,10), sticky="E")

    # Set up layers
    signin_window.columnconfigure(0, weight=1)
    login_frame.columnconfigure(0, weight=1)