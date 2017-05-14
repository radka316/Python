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
