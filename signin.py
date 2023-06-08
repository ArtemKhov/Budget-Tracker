from tkinter import *
import ttkbootstrap as tkboot
from PIL import ImageTk

def user_enter_focus_in(event):
    if username_form.get() == "username":
        username_form.delete(0, END)
        username_form.configure(foreground="white")


def user_enter_focus_out(event):
    if username_form.get() == '':
        username_form.insert(0, "username")
        username_form.configure(foreground="grey")


def password_enter_focus_in(event):
    if password_form.get() == "password":
        password_form.delete(0, END)
        password_form.configure(show="*", foreground="white")
        eyeButton.grid(row=2, column=1)


def password_enter_focus_out(event):
    if password_form.get() == "":
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

def signup_page():
    pass

# creating signin window
signin_window = tkboot.Window(themename="superhero")
signin_window.geometry("600x440")
signin_window.title('Login')

# Style
app_Style = tkboot.Style()
app_Style.configure("dark.TButton",
                    font=('Microsoft Yeahei UI Light', 9, 'bold underline'),
                    foreground="white",
                    background="#20374C")

# Login Frame
login_frame = tkboot.Frame(signin_window, style="dark")
login_frame.grid(row=0, column=0, padx=50, pady=50, sticky="WE")

# Login Label
login_text = tkboot.Label(login_frame, text="Sign In", font=("", 20, "bold"), background="#20374C")
login_text.grid(row=0, column=0)

# Username and password entries
username_form = tkboot.Entry(login_frame, style="info", foreground="grey")
username_form.grid(row=1, column=0)
username_form.insert(0, 'username')
username_form.bind("<FocusIn>", user_enter_focus_in)
username_form.bind("<FocusOut>", user_enter_focus_out)

password_form = tkboot.Entry(login_frame, style="info", foreground="grey")
password_form.grid(row=2, column=0)
password_form.insert(0, "password")
password_form.bind("<FocusIn>", password_enter_focus_in)
password_form.bind("<FocusOut>", password_enter_focus_out)

# Show/Hide
close_eye_image = PhotoImage(file='images/password/hide_password.png')
eyeButton = tkboot.Button(login_frame,
                          style="dark",
                          takefocus=False,
                          image=close_eye_image,
                          cursor='hand2',
                          command=hide_password)


forget_button = tkboot.Button(login_frame, text='Forgot password?', style="dark.TButton", takefocus=False, cursor='hand2')
forget_button.grid(row=3, column=0)

sign_in_button = tkboot.Button(login_frame,
                               text="Sign In",
                               style='success',
                               takefocus=False,
                               command=signup_page)
sign_in_button.grid(row=4, column=0)

signupLabel = tkboot.Label(login_frame, text="Don't have an account?", background="#20374C")
signupLabel.grid(row=5, column=0)

new_account_button = tkboot.Button(login_frame,text='Create New One', style="dark.TButton", takefocus=False, cursor='hand2')
new_account_button.grid(row=5, column=1)


signin_window.columnconfigure(0, weight=1)
login_frame.columnconfigure(0, weight=1)

signin_window.mainloop()