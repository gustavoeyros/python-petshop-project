from PIL import Image, ImageTk
from tkinter import *
import tkinter.messagebox as MessageBox
import mysql.connector as mysql
import subprocess

root = Tk()

root.title("Petshop Dog's")
root.config(background='#FFFFFF')
root.resizable(False, False)
root.maxsize(width=500, height=300)
root.minsize(width=500, height=300)

photo = PhotoImage(file="assets\\window_icon.png")
root.iconphoto(False, photo)

# Database function


def delete():
    id = entry_id.get()

    if (id == ""):
        MessageBox.showinfo("Error", "Preencha todos os campos")
    else:
        connection = mysql.connect(
            host="localhost", user="root", password="", database="crud_python_tkinter")
        cursor = connection.cursor()
        cursor.execute("DELETE FROM usuario WHERE codigo='"+id+"'")
        cursor.execute("commit")

        MessageBox.showinfo("Success", "Dados excluídos com sucesso!")
        connection.close()


# Content
lbl_id = Label(root, text="Código: ", font="Arial 12", bg="#FFFFFF")
lbl_id.place(x=10, y=50)

entry_id = Entry(root, font="Arial 12", width=10)
entry_id.place(x=80, y=50)


btnSave = Button(root, text="Deletar",
                 font="Inter 10 bold", fg="white", bg="#8C30F5", border=5, background="#8C30F5", bd=0, width=20, height=2, command=delete)
btnSave.place(x=10, y=100)

# Database functions


root.mainloop()
