from tkinter import *
from components.navbar import Navbar
from PIL import Image, ImageTk

root = Tk()

root.title("Petshop Dog's")
root.config(background='#FFFFFF')
root.resizable(False, False)
root.maxsize(width=1280, height=720)
root.minsize(width=1280, height=720)


# Menu - Navbar
navbarMenu = Navbar(master=root, width=250)
navbarMenu.grid(row=0, column=0, padx=150)

# Purple - Circle
circle_image = Image.open('assets\\circle_home.png')
circle_convert_tk = ImageTk.PhotoImage(circle_image)
lbl_image = Label(root, image=circle_convert_tk, bg="#FFFFFF")
lbl_image.place(x=800, y=-80)

# Orange - Circle
orange_image = Image.open('assets\\orange_circle.png')
orange_convert_tk = ImageTk.PhotoImage(orange_image)
lbl_image = Label(root, image=orange_convert_tk, bg="#FFFFFF")
lbl_image.place(x=700, y=300)


# Turquoise - Circle
turquoise_image = Image.open('assets\\turquoise_circle.png')
turquoise_convert_tk = ImageTk.PhotoImage(turquoise_image)
lbl_image = Label(root, image=turquoise_convert_tk, bg="#FFFFFF")
lbl_image.place(x=885, y=550)

root.mainloop()
