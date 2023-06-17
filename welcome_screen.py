import ttkbootstrap as tkboot


def login_window(parent):

    def transition_to_main_window():
        signin_window.destroy()
        parent.deiconify()

    # creating signin window
    signin_window = tkboot.Toplevel()
    signin_window.geometry("600x290")
    signin_window.title('Login')
    signin_window.resizable(False, False)
    signin_window.iconbitmap(bitmap="images/app_logo.ico")
    signin_window.protocol('WM_DELETE_WINDOW', parent.quit)

    # Style
    app_Style = tkboot.Style()
    app_Style.configure("success.TButton", font=('', 12, "bold"))

    # Login Frame
    login_frame = tkboot.Frame(signin_window, style="dark")
    login_frame.grid(row=0, column=0, padx=50, pady=50, sticky="WE")

    # Welcome Label
    welcome_text = tkboot.Label(login_frame, text="Budget Tracker", font=("", 20, "bold"), background="#20374C")
    welcome_text.grid(row=0, column=0, pady=(20,5))

    # Instruction block
    instruction_text = tkboot.Label(login_frame,
                                    text="Keep track of your money expenditures",
                                    font=("", 11),
                                    background="#20374C")
    instruction_text.grid(row=1, column=0, pady=(0, 20))

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

