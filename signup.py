from tkinter import *

from components.navbar import Navbar

root = Tk()

root.title("Petshop Dog's")
root.config(background='#FFFFFF')
root.resizable(False, False)
root.maxsize(width=1280, height=720)
root.minsize(width=1280, height=720)


def signUp():
    from PIL import Image, ImageTk
    # Menu - Navbar
    navbarMenu = Navbar(master=root, width=250)
    navbarMenu.grid(row=0, column=0, padx=150, pady=15)

    # Container - Form
    containerForm = Frame(root, width=500, height=500)
    containerForm.place(x=450, y=130)

    # Purple - Circle
    circle_img = Image.open('assets\\circle_home.png')
    circle_convert = ImageTk.PhotoImage(circle_img)
    lbl_image = Label(root, image=circle_convert, bg="#FFFFFF")
    lbl_image.place(x=980, y=-80)

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
