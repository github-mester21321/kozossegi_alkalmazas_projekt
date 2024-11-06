#kiegeszitok beimportalasa
from tkinter import *
from tkinter import ttk
import tkinter.font as tkFont
import david_profil
import patrik_profil
import vendeg_valasztas


def belepesAblak():
    #at ablak letrehozasa es alap beallitasai
    root = Tk()
    root.title("Belépés")
    root.geometry("400x300")
    root.configure(bg='#6a6664')
    root.resizable(False, False)  #az ablak atmeretezesenek letiltasa


    elso_szoveg = Label(root, text="Felhasználónév: ", font="rubik 10 bold").place(relx=0.25, rely=0.16, anchor=CENTER) #a "felhasznalonev" felirat megjelenitese
    felhasznalonev = Entry(root, borderwidth=2) #a "felhasznalonev" bekerese a felhasznalotol
    felhasznalonev.place(relx=0.75, rely=0.16, anchor=CENTER)

    masodik_szoveg = Label(root, text="Jelszó: ", font="rubik 10 bold").place(relx=0.25, rely=0.25, anchor=CENTER) #a "jelszo" felirat megjelenitese
    jelszo = Entry(root, borderwidth=2, show="*")   #a "jelszo" bekerese a felhasznalotol
    jelszo.place(relx=0.75, rely=0.25, anchor=CENTER)


    def csillag(event):  #a fuggveny lefutasakor elrejti a megadott jelszot
        jelszo.config(show="*")
        
    def nemcsillag(event): #a fuggveny lefutasakor megjeleniti a megadott jelszot
        jelszo.config(show="")


    showpasswd = Button(root, text="👁", fg='black', bg='#FD8B51', activebackground='#FD8B51')  #a jelszo elrejtese gomb letrehozasa
    showpasswd.bind('<ButtonPress-1>', nemcsillag) #a gomb lenyomasakor (lenyomva tartasakor) a nemcsillag fuggveny futtatasa
    showpasswd.bind('<ButtonRelease-1>', csillag)    #a gomb felengedesekor a csillag fuggveny futtatasa 
    showpasswd.place(relx=0.925, rely=0.21) #a jelszo elrejtese gomb megjelenitese

    
    def bekeres():  
        #a felhasznalonev es a jelszo beolvasasa az entry widget-bol
        felhasznalo_neve = felhasznalonev.get()
        felhasznalo_jelszava = jelszo.get()
        # print(felhasznalo_jelszava, felhasznalo_neve)


        nincs = True    #a vane valtozo azert kell, hogy ha a felhasznalo meg nem regisztralt, akkor ezt tudassuk vele
        
        with open('./fajlba_iras/felhasznalo_jelszo_kombinacio.txt', 'r', encoding="utf-8") as file:    #a jelszavak es a felhasznalonevek beolvasasa
            for i in file:
                i = i.split(';')    #feldarabolas
                x = i[1].replace("\n", "")  #\n torlese a sorok vegerol
                data = [i[0], x]
                print(data)
                with open('./fajlba_iras/felhasznalonev.txt', 'w', encoding='utf-8') as fajl:
                    print(felhasznalo_neve, file=fajl)  #az aktualis felhasznalonev fajlba kiiratasa
                if data[0] == felhasznalo_neve and data[1] == felhasznalo_jelszava: #ha a felhasznalonev es a jelszo ellenorzese, hogy mar regisztraltak-e
                    koszontes = Label(root, text="Üdvözöllek", font='rubik 12 bold')    #ha igen akkor koszontes
                    koszontes.place(relx=0.5, rely=0.4, anchor=CENTER)
                    if felhasznalo_neve == "david" and felhasznalo_jelszava == "jelszo":    #a felhasznalo nev es a jelszo ellenorzese --> ha jok, akkor a felhasznalonevnek megfeleloen a program megnyitasa
                        david_profil.profil_d()
                    elif felhasznalo_neve == "patrik" and felhasznalo_jelszava == "jelszo": #a felhasznalo nev es a jelszo ellenorzese --> ha jok, akkor a felhasznalonevnek megfeleloen a program megnyitasa
                        patrik_profil.foOldal()
                    else:   #a felhasznalo nev es a jelszo ellenorzese --> ha jok, akkor a felhasznalonevnek megfeleloen a program megnyitasa
                        vendeg_valasztas.valasztasAblak_vendegeknek()
                        
                    
                    felhasznalonev.delete(0, END)   #a mezo torlese bejelentkezes utan
                    jelszo.delete(0, END)   #a mezo torlese bejelentkezes utan
                    nincs = False   #a felhasznalo regisztralt ezert a vane erteket false-ra csereljuk

            
        if nincs == True:   #csak akkor fut le ha van olyan felhasznalo, aki meg nincsen regisztralva
            hiba = Label(root, text="Nem jól adtad meg felhasználóneved vagy \n jelszavad vagy még nem regisztráltál.", font='rubik 8 bold')    #hibauzenet felvetele
            hiba.place(relx=0.5, rely=0.4, anchor=CENTER)   #hibauzenet elhelyezese
            root.after(2000, lambda:root.destroy())     #2 mp utan a program bezarasa --> a regisztracio lehetove tetele 
            


    bekeres_gomb = Button(root, text="Enter", command=bekeres, fg='black', bg='#FD8B51').place(relx=0.5, rely=0.6, anchor=CENTER) #a bejelentkezest futtato gomb letrehozasa es elhelyezese


    #a program folyamatos futasat biztosito fuggveny
    root.mainloop()

# #egy masik programbol torteno meghivashoz sukseges fuggveny meghivasa
# belepesAblak()