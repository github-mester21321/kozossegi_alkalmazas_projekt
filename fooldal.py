from tkinter import *
import belepes
import regisztracio
import tkinter.font as tkFont

root = Tk()
root.geometry("450x400")
root.configure(bg='#257180')
gombfont = tkFont.Font(weight=tkFont.BOLD, size=10, family="Times")
cimfont = tkFont.Font(weight=tkFont.BOLD, size=20, family="Times")

# root.attributes('-fullscreen', True)


def belepesFg():
    belepes.belepesAblak()
    
def regisztracioFg():
    regisztracio.regisztaciosAblak()

cim = Label(text="Casual & Cozy Cringe Club", font=cimfont)
cim.place(relx=0.14, rely=0.01)

# elso_szoveg = Label(root, text="Felhasználónév: ", font="rubik 10 bold").place(relx=0.25, rely=0.06, anchor=CENTER)
belepes_gomb = Button(root, text="Belépés", command=belepesFg, fg='black', bg='#FD8B51', font=gombfont, bd=2)
belepes_gomb.place(relx=0.25, rely=0.4, anchor=CENTER)

# masodik_szoveg = Label(root, text="Jelszó: ", font="rubik 10 bold").place(relx=0.25, rely=0.15, anchor=CENTER)
regisztracio_gomb = Button(root, text="Regisztáció", command=regisztracioFg, fg='black', bg='#FD8B51', font=gombfont, bd=2)
regisztracio_gomb.place(relx=0.75, rely=0.4, anchor=CENTER)

root.mainloop()