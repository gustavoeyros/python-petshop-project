from tkinter import *
import tkinter.messagebox as MessageBox
import mysql.connector as mysql

root = Tk()

root.title("Petshop Dog's")
root.config(background='#FFFFFF')
root.resizable(False, False)
root.maxsize(width=500, height=300)
root.minsize(width=500, height=300)

photo = PhotoImage(file="assets\\window_icon.png")
root.iconphoto(False, photo)

# Database function


def read():
    id = entry_id.get()

    if (id == ""):
        MessageBox.showinfo("Error", "Preencha todos os campos")
    else:
        connection = mysql.connect(
            host="localhost", user="root", password="", database="crud_python_tkinter")
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM usuario WHERE codigo='"+id+"'")
        rows = cursor.fetchall()

        for row in rows:
            entry_name.insert(0, row[1])
            entry_phone.insert(0, row[2])
        connection.close()


# Content
lbl_id = Label(root, text="Código: ", font="Arial 12", bg="#FFFFFF")
lbl_id.place(x=10, y=50)

entry_id = Entry(root, font="Arial 12", width=10)
entry_id.place(x=80, y=50)

lbl_name = Label(root, text="Nome: ", font="Arial 12", bg="#FFFFFF")
lbl_name.place(x=10, y=80)

entry_name = Entry(root, font="Arial 12", width=10)
entry_name.place(x=80, y=80)


lbl_phone = Label(root, text="Telefone: ", font="Arial 12", bg="#FFFFFF")
lbl_phone.place(x=10, y=110)

entry_phone = Entry(root, font="Arial 12", width=10)
entry_phone.place(x=80, y=110)


btnSave = Button(root, text="Consultar",
                 font="Inter 10 bold", fg="white", bg="#8C30F5", border=5, background="#8C30F5", bd=0, width=20, height=2, command=read)
btnSave.place(x=10, y=150)

# Database functions


root.mainloop()
