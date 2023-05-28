from tkinter import *
import subprocess


def login():

    root = Tk()

    root.title("Petshop Dog's")
    root.config(background='#FFFFFF')
    root.resizable(False, False)
    root.maxsize(width=1280, height=720)
    root.minsize(width=1280, height=720)

    from PIL import Image, ImageTk

    # CRUD - Navbar

    def open_create():
        subprocess.run(["python", "crud__create.py"])

    def open_delete():
        subprocess.run(["python", "crud__delete.py"])

    # Menu - Navbar

    photo = PhotoImage(file="assets\\window_icon.png")
    root.iconphoto(False, photo)

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

    def open_crud():
        root.destroy()
        subprocess.run(["python", "crud.py"])

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

    # crud_option
    crud_option__navbar = Button(
        root, text="CMS", font=font_default, fg="#18191F", bg="#FFFFFF", padx=15, bd=0, border=0, command=open_crud)
    crud_option__navbar.grid(row=0, column=5)

    ####

    # Container - Form
    containerForm = Frame(root, width=500, height=500)
    containerForm.place(x=450, y=130)

    # Title
    title_page = Label(root, text="Painel - CMS",
                       font="Inter 25 bold")
    title_page.place(x=605, y=155)

    # Purple - Circle
    circle_image_signup = Image.open('assets\\circle_home.png')
    circle_convert_signup = ImageTk.PhotoImage(circle_image_signup)
    lbl_image_signup = Label(root, image=circle_convert_signup, bg="#FFFFFF")
    lbl_image_signup.place(x=980, y=-80)

    # Orange - Circle
    orange_image = Image.open('assets\\orange_circle.png')
    orange_convert_tk = ImageTk.PhotoImage(orange_image)
    lbl_image = Label(root, image=orange_convert_tk, bg="#FFFFFF")
    lbl_image.place(x=320, y=120)

    # Turquoise - Circle
    turquoise_image = Image.open('assets\\turquoise_circle.png')
    turquoise_convert_tk = ImageTk.PhotoImage(turquoise_image)
    lbl_image = Label(root, image=turquoise_convert_tk, bg="#FFFFFF")
    lbl_image.place(x=1000, y=550)

    # Form
    # Buttons
    btnCreate = Button(root, text="Create",
                       font="Inter 10 bold", fg="white", bg="#8C30F5", border=5, background="#8C30F5", bd=0, width=48, height=2, command=open_create)
    btnCreate.place(x=495, y=300)

    btnRead = Button(root, text="Read",
                     font="Inter 10 bold", fg="white", bg="#8C30F5", border=5, background="#8C30F5", bd=0, width=48, height=2)
    btnRead.place(x=495, y=350)

    btnUpdate = Button(root, text="Update",
                       font="Inter 10 bold", fg="white", bg="#8C30F5", border=5, background="#8C30F5", bd=0, width=48, height=2)
    btnUpdate.place(x=495, y=400)

    btnDelete = Button(root, text="Delete",
                       font="Inter 10 bold", fg="white", bg="#8C30F5", border=5, background="#8C30F5", bd=0, width=48, height=2,  command=open_delete)
    btnDelete.place(x=495, y=450)

    root.mainloop()


login()
