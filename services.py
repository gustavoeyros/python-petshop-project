from tkinter import *
from tkinter import ttk
from components.navbar import Navbar

root = Tk()

root.title("Petshop Dog's")
root.config(background='#FFFFFF')
root.resizable(False, False)
root.maxsize(width=1280, height=720)
root.minsize(width=1280, height=720)


def services():
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
    nameEntry = Entry(root, width=55, bg="white")
    nameEntry.place(x=550, y=320)
    nameLabel = Label(root, text="Name: ", font="Inter 10 bold",)
    nameLabel.place(x=495, y=317)

    # Services
    serviceBox = ttk.Combobox(root, values=["Health", "Education", "Dog Bath"])
    serviceBox.place(x=550, y=350)
    serviceLabel = Label(root, text="Service type: ", font="Inter 10 bold",)
    serviceLabel.place(x=455, y=347)

    # Value
    valueEntry = Entry(root, width=55, bg="white")
    valueEntry.place(x=550, y=380)
    valueLabel = Label(root, text="Value: ", font="Inter 10 bold",)
    valueLabel.place(x=495, y=377)

    # Description
    descriptionEntry = Entry(root, width=55, bg="white")
    descriptionEntry.place(x=550, y=410)
    descriptionLabel = Label(root, text="Description: ", font="Inter 10 bold",)
    descriptionLabel.place(x=460, y=407)

    # Button
    btnSignUp = Button(root, text="Register service",
                       font="Inter 10 bold", fg="white", bg="#8C30F5", border=5, background="#8C30F5", bd=0, width=48)
    btnSignUp.place(x=495, y=445)

    root.mainloop()


services()
