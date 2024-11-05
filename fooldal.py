from tkinter import *
import belepes
import regisztracio
import tkinter.font as tkFont
from tkinter import PhotoImage

root = Tk()
root.geometry("800x500")
root.configure(bg='#257180')
root.title("Casual & Cozy Cringe Club")

def belepesFg():
    belepes.belepesAblak()
    
def regisztracioFg():
    regisztracio.regisztaciosAblak()

cim = Label(root, text="Casual & Cozy Cringe Club", fg='black', bg='#FD8B51', font='Times 30 bold')
cim.place(relx=0.2, rely=0.1)

logo = PhotoImage(file="./patrikkep/aaxct5d7k.gif")
logocim = Label(root, image=logo)
logocim.place(relx=0.35, rely=0.3)

# elso_szoveg = Label(root, text="Felhasználónév: ", font="rubik 10 bold").place(relx=0.25, rely=0.06, anchor=CENTER)
belepes_gomb = Button(root, text="Belépés", command=belepesFg, fg='black', bg='#FD8B51', font='Times 20 bold', bd=2)
belepes_gomb.place(relx=0.25, rely=0.9, anchor=CENTER)

# masodik_szoveg = Label(root, text="Jelszó: ", font="rubik 10 bold").place(relx=0.25, rely=0.15, anchor=CENTER)
regisztracio_gomb = Button(root, text="Regisztáció", command=regisztracioFg, fg='black', bg='#FD8B51', font='Times 20 bold', bd=2)
regisztracio_gomb.place(relx=0.75, rely=0.9, anchor=CENTER)

root.mainloop()