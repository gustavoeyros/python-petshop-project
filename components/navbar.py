from tkinter import *


# default colors
font_default = "Inter 13 bold"


class Navbar(Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # home_option
        home_option__navbar = Label(
            self, text="Home", font=font_default, fg="#18191F", bg="#FFFFFF", padx=10)
        home_option__navbar.grid(row=0, column=0)

        # signup_option
        signup_option__navbar = Label(
            self, text="Sign up", font=font_default, fg="#18191F", bg="#FFFFFF", padx=10)
        signup_option__navbar.grid(row=0, column=1)

        # animal_rgister_option
        animal_register_option__navbar = Label(
            self, text="Animal register", font=font_default, fg="#18191F", bg="#FFFFFF", padx=10)
        animal_register_option__navbar.grid(row=0, column=2)

        # services_option
        services_option__navbar = Label(
            self, text="Services", font=font_default, fg="#18191F", bg="#FFFFFF", padx=10)
        services_option__navbar.grid(row=0, column=3)
