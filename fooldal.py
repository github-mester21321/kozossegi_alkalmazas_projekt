from tkinter import *
import belepes
import regisztracio

root = Tk()
root.geometry("300x350")
# root.attributes('-fullscreen', True)


def belepesFg():
    belepes.belepesAblak()
    
def regisztracioFg():
    regisztracio.regisztaciosAblak()


# elso_szoveg = Label(root, text="Felhasználónév: ", font="rubik 10 bold").place(relx=0.25, rely=0.06, anchor=CENTER)
belepes_gomb = Button(root, text="Belépés", command=belepesFg)
belepes_gomb.place(relx=0.25, rely=0.4, anchor=CENTER)

# masodik_szoveg = Label(root, text="Jelszó: ", font="rubik 10 bold").place(relx=0.25, rely=0.15, anchor=CENTER)
regisztracio_gomb = Button(root, text="Regisztáció", command=regisztracioFg)
regisztracio_gomb.place(relx=0.75, rely=0.4, anchor=CENTER)

root.mainloop()