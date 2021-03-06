from tkinter import *
import PIL
from PIL import ImageTk, Image
import numpy as np


main=Tk()
main.title("Uprava obrazku")
path = "pizza.jpg" #path to image

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

def edges():
    global act, resized
    if act=="":
        img1 = resized
    else:
        img1= act
    
    data= np.asarray(img1)
    tmp=data
    tmp.setflags(write=1)
    w, h, c = data.shape

    for x in range(1, w - 1):
        for y in range(1, h - 1):
            for z in range(c):
                col = (
                + 9 * data[x, y, z]
                - data[x - 1, y, z]
                - data[x + 1, y, z]
                - data[x, y + 1, z]
                - data[x, y - 1, z]
                - data[x - 1, y + 1, z]
                - data[x - 1, y - 1, z]
                - data[x + 1, y - 1, z]
                - data[x + 1, y + 1, z])

                if col < 0:
                    col = 0

                if col > 255:
                    col = 255

                
                tmp[x, y, z] = col

    data_out=tmp
    data_out=np.asarray(data, dtype=np.uint8)
    img_out = Image.fromarray(data_out)
    act = img_out
    img2 = ImageTk.PhotoImage(img_out)
    panel.configure(image = img2)
    panel.image= img2


    
#buttons
original=Button(main,text="Original", command=original, width=10)
original.grid(row=1, column=0)
black=Button(main,text="Grayscale", command= black_white, width=10)
black.grid(row=2, column=0)
rotate=Button(main,text="Rotate", command= rotate, width=10)
rotate.grid(row=3, column=0)
neg=Button(main,text="Negative", command=invert, width=10)
neg.grid(row=5, column=0)
light=Button(main,text="Lighten", width=10, command=lighter)
light.grid(row=6, column=0)
dark=Button(main,text="Darken", width=10, command=darker)
dark.grid(row=7, column=0)
edges=Button(main,text="Sharpen", command=edges, width=10)
edges.grid(row=8, column=0)
