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
act=""

def black_white () :
    global act, resized
    if act=="":
        img1 = resized
    else:
        img1= act
    
    data= np.asarray(img1)
    try:
        data_out = [0.299, 0.587, 0.114] * data
        data_out= data_out.sum(axis=2)
        data_out=np.asarray(data_out, dtype=np.uint8)
        img_out = Image.fromarray(data_out, 'L')
    except:
        return 0
    act = img_out
    img_new = ImageTk.PhotoImage(img_out)
    panel.configure(image = img_new)
    panel.image= img_new

def original():
    global act, resized
    img = ImageTk.PhotoImage(resized)
    panel.configure(image = img)
    panel.image= img
    act= resized

def rotate():
    global act, resized
    if act=="":
        img2 = resized
    else:
        img2= act
    data= np.asarray(img2)
    data_out=np.rot90(data)
    data_out=np.asarray(data_out, dtype=np.uint8)
    img_out=Image.fromarray(data_out)
    act= img_out
    img_new = ImageTk.PhotoImage(img_out)
    panel.configure(image = img_new)
    panel.image= img_new

def invert():
    global act, resized
    if act=="":
        img3 = resized
    else:
        img3= act
    data= np.asarray(img3)
    try:
        data_out = 255 - data
        img_out = Image.fromarray(data_out)
        img_new = ImageTk.PhotoImage(img_out)
    except:
        return 0
    act=img_out
    panel.configure(image = img_new)
    panel.image= img_new

def lighter():
    global act, resized
    if act=="":
        img1 = resized
    else:
        img1= act
    
    data= np.asarray(img1)
    mask = (255 - data) < 25
    data_out = np.where((255-data) < 25,255,data+25)
    data_out=np.asarray(data_out, dtype=np.uint8)
    img_out = Image.fromarray(data_out)

    act = img_out
    img2 = ImageTk.PhotoImage(img_out)
    panel.configure(image = img2)
    panel.image= img2

def darker():
    global act, resized
    if act=="":
        img1 = resized
    else:
        img1= act
    
    data= np.asarray(img1)
    try:
        data_out = 0.8 * data
        
        data_out=np.asarray(data_out, dtype=np.uint8)
        img_out = Image.fromarray(data_out)
    except:
        return 0
    act = img_out
    img2 = ImageTk.PhotoImage(img_out)
    panel.configure(image = img2)
    panel.image= img2

#tlacidla
original=Button(main,text="Original", command=original, width=10)
original.grid(row=1, column=0)
black=Button(main,text="Odstíny šedi", command= black_white, width=10)
black.grid(row=2, column=0)
rotate_l=Button(main,text="Otočit", command= rotate, width=10)
rotate_l.grid(row=3, column=0)
neg=Button(main,text="Inverzní obraz", command=invert, width=10)
neg.grid(row=5, column=0)
zes=Button(main,text="Zesvětlení", width=10, command=lighter)
zes.grid(row=6, column=0)
ztma=Button(main,text="Ztmavení", width=10, command=darker)
ztma.grid(row=7, column=0)
hrany=Button(main,text="Zvýraznění hran", width=10)
hrany.grid(row=8, column=0)
