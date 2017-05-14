from tkinter import *
import PIL
from PIL import ImageTk, Image
import numpy as np

main=Tk()
main.title("Uprava obrazku")
path = "pizza.jpg" #zadaj cestu k obrazku

origo = Image.open(path)
width= (500 / float(origo.size[0]))
height= int((float(origo.size[1]) * float(width)))
resized= origo.resize((500, height), PIL.Image.ANTIALIAS)
imgg=ImageTk.PhotoImage(resized)
panel = Label(main, image = imgg)
panel.grid(row=0, column=0)

#tlacidla

original=Button(main,text="Original", width=10)
original.grid(row=1, column=0)
black=Button(main,text="Odstíny šedi", width=10)
black.grid(row=2, column=0)
rotate_l=Button(main,text="Otočit", width=10)
rotate_l.grid(row=3, column=0)
