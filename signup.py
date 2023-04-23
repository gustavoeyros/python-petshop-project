from tkinter import *
import subprocess


def signUp():

    root = Tk()

    root.title("Petshop Dog's")
    root.config(background='#FFFFFF')
    root.resizable(False, False)
    root.maxsize(width=1280, height=720)
    root.minsize(width=1280, height=720)

    from PIL import Image, ImageTk
    # Menu - Navbar

    def open_animal_register():
        root.destroy()
        subprocess.run(["python", "animalRegister.py"])

    def open_services():
        root.destroy()
        subprocess.run(["python", "services.py"])

    def open_home():
        root.destroy()
        subprocess.run(["python", "main.py"])

    font_default = "Inter 13 bold"
    # home_option
    home_option__navbar = Button(
        root, text="Home", font=font_default, fg="#18191F", bg="#FFFFFF", padx=15, bd=0, border=0, command=open_home)
    home_option__navbar.grid(row=0, column=0)

    # signup_option
    signup_option__navbar = Button(
        root, text="Sign up", font=font_default, fg="#18191F", bg="#FFFFFF", padx=15, bd=0, border=0)
    signup_option__navbar.grid(row=0, column=1)

    # animal_rgister_option
    animal_register_option__navbar = Button(
        root, text="Animal register", font=font_default, fg="#18191F", bg="#FFFFFF", padx=15, bd=0, border=0, command=open_animal_register)
    animal_register_option__navbar.grid(row=0, column=2)

    # services_option
    services_option__navbar = Button(
        root, text="Services", font=font_default, fg="#18191F", bg="#FFFFFF", padx=15, bd=0, border=0, command=open_services)
    services_option__navbar.grid(row=0, column=3)

    ####

    # Container - Form
    containerForm = Frame(root, width=500, height=500)
    containerForm.place(x=450, y=130)

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

    # Name
    userEntry = Entry(root, width=55, bg="white")
    userEntry.place(x=550, y=320)
    userLabel = Label(root, text="Name: ", font="Inter 10 bold",)
    userLabel.place(x=495, y=317)

    # Email
    emailEntry = Entry(root, width=55, bg="white")
    emailEntry.place(x=550, y=350)
    emailLabel = Label(root, text="E-mail: ", font="Inter 10 bold",)
    emailLabel.place(x=495, y=347)

    # Password
    passwordEntry = Entry(root, width=52, bg="white")
    passwordEntry.place(x=570, y=380)
    passwordLabel = Label(root, text="Password: ", font="Inter 10 bold",)
    passwordLabel.place(x=495, y=377)

    # Button
    btnSignUp = Button(root, text="Sign Up",
                       font="Inter 10 bold", fg="white", bg="#8C30F5", border=5, background="#8C30F5", bd=0, width=48)
    btnSignUp.place(x=495, y=435)

    root.mainloop()


signUp()
