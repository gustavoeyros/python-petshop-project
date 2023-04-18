from tkinter import *


# default colors
font_default = "Inter 13 bold"


class Navbar(Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        def open_signup():
            from signup import signUp
            self.destroy()
            signUp()

        # home_option
        home_option__navbar = Button(
            self, text="Home", font=font_default, fg="#18191F", bg="#FFFFFF", padx=15, bd=0, border=0)
        home_option__navbar.grid(row=0, column=0)

        # signup_option
        signup_option__navbar = Button(
            self, text="Sign up", font=font_default, fg="#18191F", bg="#FFFFFF", padx=15, bd=0, border=0, command=open_signup)
        signup_option__navbar.grid(row=0, column=1)

        # animal_rgister_option
        animal_register_option__navbar = Button(
            self, text="Animal register", font=font_default, fg="#18191F", bg="#FFFFFF", padx=15, bd=0, border=0)
        animal_register_option__navbar.grid(row=0, column=2)

        # services_option
        services_option__navbar = Button(
            self, text="Services", font=font_default, fg="#18191F", bg="#FFFFFF", padx=15, bd=0, border=0)
        services_option__navbar.grid(row=0, column=3)
