#kiegeszitok beimportalasa
from tkinter import *
from tkinter import ttk
import valasztas
import time

def belepesAblak():
    root = Tk()
    root.title("Media")
    root.geometry("300x350")
    root.configure(bg='#6a6664')

    elso_szoveg = Label(root, text="Felhasználónév: ", font="rubik 10 bold").place(relx=0.25, rely=0.06, anchor=CENTER)
    felhasznalonev = Entry(root, borderwidth=2)
    felhasznalonev.place(relx=0.75, rely=0.06, anchor=CENTER)

    masodik_szoveg = Label(root, text="Jelszó: ", font="rubik 10 bold").place(relx=0.25, rely=0.15, anchor=CENTER)
    jelszo = Entry(root, borderwidth=2)
    jelszo.place(relx=0.75, rely=0.15, anchor=CENTER)


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
                    # time.sleep(0.1)
                    felhasznalonev.delete(0, END)
                    jelszo.delete(0, END)
                    valasztas.foChat()
                    nincs = False
                
            if nincs == True:
                hiba = Label(root, text="Nem jól adtad meg felhasználóneved vagy \n jelszavad vagy még nem regisztráltál.", font='rubik 8 bold')
                hiba.place(relx=0.5, rely=0.4, anchor=CENTER)
                root.after(2000, lambda:root.destroy())
            


    bekeres_gomb = Button(root, text="Enter", command=bekeres).place(relx=0.5, rely=0.6, anchor=CENTER)


    root.mainloop()


# belepesAblak()