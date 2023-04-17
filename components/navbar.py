from tkinter import *
import ttkbootstrap as tt

root = Tk()

root.title("Petshop Dog's")
root.config(background='#FFFFFF')
root.resizable(False, False)
root.maxsize(width=1280, height=720)

root.minsize(width=1280, height=720)

# default colors
font_default = "Inter 13 bold"


# home_option
home_option__navbar = Label(
    root, text="Home", font=font_default, fg="#18191F", bg="#FFFFFF", padx=10)
home_option__navbar.grid(row=0, column=0)

# signup_option
signup_option__navbar = Label(
    root, text="Sign up", font=font_default, fg="#18191F", bg="#FFFFFF", padx=10)
signup_option__navbar.grid(row=0, column=1)

# animal_rgister_option
animal_register_option__navbar = Label(
    root, text="Animal register", font=font_default, fg="#18191F", bg="#FFFFFF", padx=10)
animal_register_option__navbar.grid(row=0, column=2)

# services_option
services_option__navbar = Label(
    root, text="Services", font=font_default, fg="#18191F", bg="#FFFFFF", padx=10)
services_option__navbar.grid(row=0, column=3)

root.mainloop()
