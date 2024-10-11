#kiegeszitok beimportalasa
from tkinter import *
from tkinter import ttk

def regisztaciosAblak():
    root = Tk()
    root.title("Media")
    root.geometry("300x350")



    elso_szoveg = Label(root, text="Új felhasználónév: ", font="rubik 10 bold").place(relx=0.25, rely=0.06, anchor=CENTER)
    felhasznalonev = Entry(root, borderwidth=2)
    felhasznalonev.place(relx=0.75, rely=0.06, anchor=CENTER)

    masodik_szoveg = Label(root, text="Új jelszó: ", font="rubik 10 bold").place(relx=0.25, rely=0.15, anchor=CENTER)
    jelszo = Entry(root, borderwidth=2)
    jelszo.place(relx=0.75, rely=0.15, anchor=CENTER)


    def bekeres():
        vane = False
        felhasznalo_neve = felhasznalonev.get()
        felhasznalo_jelszava = jelszo.get()
        with open('./felhasznalo_jelszo_kombinacio.txt', 'r', encoding="utf-8") as fajl:
            for i in fajl:
                # i.strip()
                i = i.split(";")
                x = i[1].replace("\n", "")
                adat = [i[0], x]
                print(adat)
                if adat[0] != felhasznalo_neve or adat[1] != felhasznalo_jelszava:
                    vane = True
                    continue
        
        if vane == True and felhasznalo_neve != "" and felhasznalo_jelszava != "":
            with open ('./felhasznalo_jelszo_kombinacio.txt', 'a', encoding="utf-8") as fajl2:            
                print(felhasznalo_neve, felhasznalo_jelszava, sep=";", file=fajl2)


    bekeres_gomb = Button(root, text="Enter", command=bekeres).place(relx=0.5, rely=0.6, anchor=CENTER)


    root.mainloop()

# regisztaciosAblak()