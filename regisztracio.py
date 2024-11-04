#kiegeszitok beimportalasa
from tkinter import *
# from tkinter import ttk

def regisztaciosAblak():
    root = Tk()
    root.title("Media")
    root.geometry("300x350")
    # root.attributes('-fullscreen', True)
    root.configure(bg='#6a6664')


    elso_szoveg = Label(root, text="Új felhasználónév: ", font="rubik 10 bold").place(relx=0.25, rely=0.06, anchor=CENTER)
    felhasznalonev = Entry(root, borderwidth=2)
    felhasznalonev.place(relx=0.75, rely=0.06, anchor=CENTER)

    masodik_szoveg = Label(root, text="Új jelszó: ", font="rubik 10 bold").place(relx=0.25, rely=0.15, anchor=CENTER)
    jelszo = Entry(root, borderwidth=2)
    jelszo.place(relx=0.75, rely=0.15, anchor=CENTER)


    def bekeres():
        f_nevek_es_jelsz = []
        felhasznalo_neve = felhasznalonev.get()
        felhasznalo_jelszava = jelszo.get()
        with open('./felhasznalo_jelszo_kombinacio.txt', 'r', encoding="utf-8") as fajl:
            for i in fajl:
                i.strip()
                i = i.split(";")
                # print(i)
                x = i[1].replace("\n", "")
                adat = [i[0], x]
                # print(adat)
                f_nevek_es_jelsz.append(adat)
                # print(f_nevek_es_jelsz)
            
            megfelel_e = True
            for i in f_nevek_es_jelsz:
                # print(i)
                if i[0] == felhasznalo_neve and i[1] == felhasznalo_jelszava:
                    megfelel_e = False
                    break
                                   
        if felhasznalo_neve == "" or felhasznalo_jelszava == "":
            megfelel_e = False
         
        if megfelel_e == True:
            kombinacio = [felhasznalo_neve, felhasznalo_jelszava]
            f_nevek_es_jelsz.append(kombinacio)  
            with open ('./felhasznalo_jelszo_kombinacio.txt', 'w', encoding="utf-8") as fajl2:            
                for adat_sorok in f_nevek_es_jelsz:
                    print(adat_sorok[0], adat_sorok[1], sep=";", file=fajl2)

            visszajelzes = Label(root, text="Az általad megadott felhasználónév és \n jelszó páros el lettek mentve.")
            visszajelzes.place(relx=0.5, rely=0.4, anchor=CENTER)
        
        elif megfelel_e == False:
            visszajelzes = Label(root, text="Add meg újra!")
            visszajelzes.place(relx=0.5, rely=0.4, anchor=CENTER)


    bekeres_gomb = Button(root, text="Enter", command=bekeres).place(relx=0.5, rely=0.6, anchor=CENTER)


    root.mainloop()

# regisztaciosAblak()