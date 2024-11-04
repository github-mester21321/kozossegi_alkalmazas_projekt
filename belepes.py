#kiegeszitok beimportalasa
from tkinter import *
from tkinter import ttk
# import kozossegi_alkalmazas_projekt.david_valasztas as david_valasztas
import time
import tkinter.font as tkFont
import david_profil
import patrik_valasztas
import vendeg_valasztas

def belepesAblak():
    root = Tk()
    root.title("Media")
    root.geometry("400x300")
    # root.attributes('-fullscreen', True)
    root.configure(bg='#6a6664')

    elso_szoveg = Label(root, text="Felhasználónév: ", font="rubik 10 bold").place(relx=0.25, rely=0.16, anchor=CENTER)
    felhasznalonev = Entry(root, borderwidth=2)
    felhasznalonev.place(relx=0.75, rely=0.16, anchor=CENTER)

    masodik_szoveg = Label(root, text="Jelszó: ", font="rubik 10 bold").place(relx=0.25, rely=0.25, anchor=CENTER)
    jelszo = Entry(root, borderwidth=2, show="*")
    jelszo.place(relx=0.75, rely=0.25, anchor=CENTER)

    def nemcsillag(event):
        jelszo.config(show="*")
    def csillag(event):
        jelszo.config(show="")

    showpasswd = Button(root, text="👁", fg='black', bg='#FD8B51', activebackground='#FD8B51')
    showpasswd.bind('<ButtonPress-1>', csillag)
    showpasswd.bind('<ButtonRelease-1>', nemcsillag)
    showpasswd.place(relx=0.925, rely=0.21)

    def bekeres():
        felhasznalo_neve = felhasznalonev.get()
        felhasznalo_jelszava = jelszo.get()

        # print(felhasznalo_jelszava, felhasznalo_neve)

        nincs = True
        with open('./felhasznalo_jelszo_kombinacio.txt', 'r', encoding="utf-8") as file:
            for i in file:
                i = i.split(';')
                x = i[1].replace("\n", "")
                data = [i[0], x]
                print(data)
                if data[0] == felhasznalo_neve and data[1] == felhasznalo_jelszava:
                    koszontes = Label(root, text="Üdvözöllek", font='rubik 12 bold')
                    koszontes.place(relx=0.5, rely=0.4, anchor=CENTER)
                    if felhasznalo_neve == "david" and felhasznalo_jelszava == "jelszo":
                        david_profil.profil_d()
                    elif felhasznalo_neve == "patrik" and felhasznalo_jelszava == "jelszo":
                        patrik_valasztas.valasztasAblak()
                    else:
                        vendeg_valasztas.valasztasAblak()
                        
                    
                    felhasznalonev.delete(0, END)
                    jelszo.delete(0, END)
                    nincs = False

            
        if nincs == True:
            hiba = Label(root, text="Nem jól adtad meg felhasználóneved vagy \n jelszavad vagy még nem regisztráltál.", font='rubik 8 bold')
            hiba.place(relx=0.5, rely=0.4, anchor=CENTER)
            root.after(2000, lambda:root.destroy())
            


    bekeres_gomb = Button(root, text="Enter", command=bekeres, fg='black', bg='#FD8B51').place(relx=0.5, rely=0.6, anchor=CENTER)


    root.mainloop()


# belepesAblak()