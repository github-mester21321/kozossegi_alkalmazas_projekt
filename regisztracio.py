#kiegeszitok beimportalasa
from tkinter import *
from tkinter import ttk

def belepesAblak():
    root = Tk()
    root.title("Media")
    root.geometry("300x350")



    elso_szoveg = Label(root, text="Felhasználónév: ", font="rubik 10 bold").place(relx=0.25, rely=0.06, anchor=CENTER)
    felhasznalonev = Entry(root, borderwidth=2)
    felhasznalonev.place(relx=0.75, rely=0.06, anchor=CENTER)

    masodik_szoveg = Label(root, text="Jelszó: ", font="rubik 10 bold").place(relx=0.25, rely=0.15, anchor=CENTER)
    jelszo = Entry(root, borderwidth=2)
    jelszo.place(relx=0.75, rely=0.15, anchor=CENTER)


    def bekeres():
        felhasznalo_neve = felhasznalonev.get()
        felhasznalo_jelszava = jelszo.get()
        with open('./felhasznalo_jelszo_kombinacio.txt', 'a', encoding="utf-8") as fajl:
            for adat in fajl:
                data = adat.split(';')
                if data[0] != felhasznalo_neve or data[1] != felhasznalo_jelszava:
                    print(felhasznalo_neve, felhasznalo_jelszava, sep=";", file=fajl)


    bekeres_gomb = Button(root, text="Enter", command=bekeres).place(relx=0.5, rely=0.6, anchor=CENTER)


    root.mainloop()

belepesAblak()