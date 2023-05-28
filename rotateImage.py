import cv2
from tkinter import *
from tkinter import filedialog
import tkinter.messagebox as MessageBox
import mysql.connector as mysql
from PIL import Image, ImageTk

root = Tk()

root.title("Petshop Dog's")
root.config(background='#FFFFFF')
root.resizable(False, False)
root.maxsize(width=500, height=300)
root.minsize(width=500, height=300)

photo = PhotoImage(file="assets\\window_icon.png")
root.iconphoto(False, photo)


def rotate(rotacao_image, angulo):

    altura, largura = rotacao_image.shape[0], rotacao_image.shape[1]

    y, x = altura / 2, largura/2

    rotacao_matriz = cv2.getRotationMatrix2D((x, y), angulo, 1.0)

    rotacionando_imagem = cv2.warpAffine(
        rotacao_image, rotacao_matriz, (largura, altura))

    return rotacionando_imagem


def open_image():
    file_path = filedialog.askopenfilename(
        filetypes=[("Imagens", "*.png;*.jpg;*.jpeg")])

    if file_path:
        image = cv2.imread(file_path, 1)
        angle = int(entry_angle.get())

        if angle:
            normal = rotate(image, angle)
            cv2.imshow("Image", normal)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


lbl_angle = Label(root, text="Ângulo: ", font="Arial 12", bg="#FFFFFF")
lbl_angle.place(x=10, y=80)

entry_angle = Entry(root, font="Arial 12", width=10)
entry_angle.place(x=80, y=80)


btnAskFile = Button(root, text="Selecione um ângulo e escolha a imagem",
                    font="Inter 10 bold", fg="white", bg="#8C30F5", border=5, background="#8C30F5", bd=0, width=40, height=2, command=open_image)
btnAskFile.place(x=10, y=150)


root.mainloop()
