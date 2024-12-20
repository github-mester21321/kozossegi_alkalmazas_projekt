from tkinter import *
from tkinter import ttk
from tkinter import PhotoImage
import tkinter.font as tkFont

x = 2
def galeria_p():
    global X
    root = Toplevel()
    root.geometry("750x500")
    root.title("Patrik galéria")
    root.resizable(False, False)
    root.configure(bg='#6a6664')

    font = ("rubik", 14, "bold")

    img1 = PhotoImage(file="./kepek/patrikkep/metallica1.gif")
    img2 = PhotoImage(file="./kepek/patrikkep/metallica2.gif")
    img3 = PhotoImage(file="./kepek/patrikkep/metallica3.gif")
    img4 = PhotoImage(file="./kepek/patrikkep/metallica4.gif")

    def elore():
        global x

        x+=1

        if x == 5:
            x = 1
        if x == 1:
            l.config(image=img1)
            szoveg.config(text="And Justice For All")
        elif x == 2:
            l.config(image=img2)
            szoveg.config(text="Metallica")
        elif x == 3:
            l.config(image=img3)
            szoveg.config(text="Kill 'em All")
        elif x == 4:
            l.config(image=img4)
            szoveg.config(text="Master Of Puppets")
        

    def hatra():
        global x

        x-=1

        if x == 0:
            x = 3
        if x == 1:
            l.config(image=img1)
            szoveg.config(text="And Justice For All")
        elif x == 2:
            l.config(image=img2)
            szoveg.config(text="Metallica")
        elif x == 3:
            l.config(image=img3)
            szoveg.config(text="Kill 'em All")
        elif x == 4:
            l.config(image=img4)
            szoveg.config(text="Master Of Puppets")

    l = Label(root, image=img1)
    l.place(relx=0.3075, rely=0.1)
    szoveg = Label(root, text="And Justice For All", font=font)
    szoveg.place(relx=0.4, rely=0.8)

    gomb1 = Button(root, text=">", command=elore)
    gomb1.place(relx=0.75, rely=0.5)
    gomb2 = Button(root, text="<", command=hatra)
    gomb2.place(relx=0.25, rely=0.5)

    root.mainloop()
    
# galeria_p()