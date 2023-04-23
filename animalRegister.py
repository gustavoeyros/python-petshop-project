from tkinter import *
from PIL import Image, ImageTk
import subprocess


def animalRegister():
    root = Tk()

    root.title("Petshop Dog's")
    root.config(background='#FFFFFF')
    root.resizable(False, False)
    root.maxsize(width=1280, height=720)
    root.minsize(width=1280, height=720)

    photo = PhotoImage(file="assets\\window_icon.png")
    root.iconphoto(False, photo)

    # Menu - Navbar

    def open_home():
        root.destroy()
        subprocess.run(["python", "main.py"])

    def open_signup():
        root.destroy()
        subprocess.run(["python", "signup.py"])

    def open_animal_register():
        root.destroy()
        subprocess.run(["python", "animalRegister.py"])

    def open_services():
        root.destroy()
        subprocess.run(["python", "services.py"])

    def open_login():
        root.destroy()
        subprocess.run(["python", "login.py"])

    font_default = "Inter 13 bold"
    # home_option
    home_option__navbar = Button(
        root, text="Home", font=font_default, fg="#18191F", bg="#FFFFFF", padx=15, bd=0, border=0, command=open_home)
    home_option__navbar.grid(row=0, column=0)

    # signup_option
    signup_option__navbar = Button(
        root, text="Client Register", font=font_default, fg="#18191F", bg="#FFFFFF", padx=15, bd=0, border=0, command=open_signup)
    signup_option__navbar.grid(row=0, column=1)

    # animal_rgister_option
    animal_register_option__navbar = Button(
        root, text="Animal register", font=font_default, fg="#18191F", bg="#FFFFFF", padx=15, bd=0, border=0, command=open_animal_register)
    animal_register_option__navbar.grid(row=0, column=2)

    # services_option
    services_option__navbar = Button(
        root, text="Services", font=font_default, fg="#18191F", bg="#FFFFFF", padx=15, bd=0, border=0, command=open_services)
    services_option__navbar.grid(row=0, column=3)

    # login_option
    login_option__navbar = Button(
        root, text="Login", font=font_default, fg="#18191F", bg="#FFFFFF", padx=15, bd=0, border=0, command=open_login)
    login_option__navbar.grid(row=0, column=4)

    # Container - Form
    containerForm = Frame(root, width=500, height=500)
    containerForm.place(x=450, y=130)

    # Title
    title_page = Label(root, text="Animal Register",
                       font="Inter 25 bold")
    title_page.place(x=570, y=155)

    # Purple - Circle
    circle_img_animal_register = Image.open('assets\\circle_home.png')
    circle_convert_animal = ImageTk.PhotoImage(circle_img_animal_register)
    lbl_image_animal = Label(root, image=circle_convert_animal, bg="#FFFFFF")
    lbl_image_animal.place(x=980, y=-80)

    # Orange - Circle
    orange_image_animal = Image.open('assets\\orange_circle.png')
    orange_convert_tk_animal = ImageTk.PhotoImage(orange_image_animal)
    lbl_image_animal = Label(
        root, image=orange_convert_tk_animal, bg="#FFFFFF")
    lbl_image_animal.place(x=320, y=120)

    # Turquoise - Circle
    turquoise_image_animal = Image.open('assets\\turquoise_circle.png')
    turquoise_convert_tk_animal = ImageTk.PhotoImage(turquoise_image_animal)
    lbl_image_animal = Label(
        root, image=turquoise_convert_tk_animal, bg="#FFFFFF")
    lbl_image_animal.place(x=1000, y=550)

    # Form

    # Name
    userEntry = Entry(root, width=55, bg="white")
    userEntry.place(x=550, y=320)
    userLabel = Label(root, text="Name: ", font="Inter 10 bold",)
    userLabel.place(x=495, y=317)

    # Weight
    emailEntry = Entry(root, width=55, bg="white")
    emailEntry.place(x=550, y=350)
    emailLabel = Label(root, text="Weight: ", font="Inter 10 bold",)
    emailLabel.place(x=485, y=347)

    # Age
    passwordEntry = Entry(root, width=55, bg="white")
    passwordEntry.place(x=550, y=380)
    passwordLabel = Label(root, text="Age: ", font="Inter 10 bold",)
    passwordLabel.place(x=495, y=377)

    # Raca
    raceEntry = Entry(root, width=55, bg="white")
    raceEntry.place(x=550, y=410)
    raceLabel = Label(root, text="Race: ", font="Inter 10 bold",)
    raceLabel.place(x=495, y=407)

    # Button
    btnSignUp = Button(root, text="Register Animal",
                       font="Inter 10 bold", fg="white", bg="#8C30F5", border=5, background="#8C30F5", bd=0, width=48)
    btnSignUp.place(x=495, y=445)

    root.mainloop()


animalRegister()
