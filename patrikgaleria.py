from tkinter import *
from tkinter import ttk
from tkinter import PhotoImage

x = 2

root = Tk()
root.geometry("750x500")
root.title("Patrik galéria")

img1 = PhotoImage(file="./patrikkep/laci1.gif")
img2 = PhotoImage(file="./patrikkep/laci2.gif")
img3 = PhotoImage(file="./patrikkep/laci3.gif")
img4 = PhotoImage(file="./patrikkep/laci4.gif")
img5 = PhotoImage(file="./patrikkep/laci5.gif")

def elore():
    global x

    if x == 6:
        x = 1
    if x == 1:
        l.config(image=img1)
        szoveg.config(text="laci1")
    elif x == 2:
        l.config(image=img2)
        szoveg.config(text="laci2")
    elif x == 3:
        l.config(image=img3)
        szoveg.config(text="laci3")
    elif x == 4:
        l.config(image=img4)
        szoveg.config(text="laci4")
    elif x == 5:
        l.config(image=img5)
        szoveg.config(text="laci5")
    x+=1

def hatra():
    global x

    if x == 0:
        x = 3
    if x == 1:
        l.config(image=img1)
    elif x == 2:
        l.config(image=img2)
    elif x == 3:
        l.config(image=img3)
    x-=1

l = Label(image=img1)
l.place(relx=0.3, rely=0.3)
szoveg = Label(root, text="laci1")
szoveg.place(relx=0.4, rely=0.75)

gomb1 = Button(root, text=">", command=elore)
gomb1.place(relx=0.75, rely=0.5)
gomb2 = Button(root, text="<", command=hatra)
gomb2.place(relx=0.25, rely=0.5)

root.mainloop()