#szukseges modulok beimportalasa
from tkinter import *
from tkinter import ttk
from tkinter import PhotoImage


#kep beazonositasahoz szukseges szamlalo
hanyadik = 1


#a kepek valtoztatasahoz szukseges lepteto fuggveny
def galeria_d():    #a fuggveny definialasa
    global hanyadik #a szamlalo valtozojanak localissa tetele
    d_galeria_main = Toplevel() #a toplevel fuggveny azt a celt, szolgalja, hogy az ablak a megnyilasakor tudja, hogy o nem egy main ablak hanem egy masodlagol ablak, amelyet masik ablakbol nyitottak meg
    d_galeria_main.geometry("1000x600") #az ablak meretei pixelben
    d_galeria_main.title("Dávid galéria")   #az ablak neve
    d_galeria_main.configure(bg='#257180')


    kep1 = PhotoImage(file="./davidkep/kisvakond.gif")  #a felhasznalt kepek egy valtozoban lesznek eltarolva
    szoveg1 = "Kisvakond"   #a felhasznalt kepekhez tartozo szovegek is egy masik valtozoban lesznek eltarolva
    kep2 = PhotoImage(file="./davidkep/verdak.gif")
    szoveg2 = "Verdák"
    kep3 = PhotoImage(file="./davidkep/mezgacsalad.gif")
    szoveg3 = "Mézga család"
    kep4 = PhotoImage(file="./davidkep/macskafogo.gif")
    szoveg4 = "Macskafogó"
    kep5 = PhotoImage(file="./davidkep/atlantis.gif")
    szoveg5 = "Atlantisz: az elveszett birodalom"
    
    
    #alapbol megjeleno kep beallitasa
    megjelenites = Label(d_galeria_main, image=kep1)
    megjelenites.place(relx=0.5, rely=0.5, anchor=CENTER)
    szoveg_kiiratas = Label(d_galeria_main, text=szoveg1)
    szoveg_kiiratas.place(relx=0.5, rely=0.9, anchor=CENTER)
    
    
    def elore_menet():  #az elore leptetest vegzo fuggveny definialasa
        global hanyadik     #a szamlalo valtozo localissa tetele
        hanyadik = hanyadik + 1     #a szamlalo ertekenek novelese 1-el
        
        
        #a szamlalo allasa szerint a latott kep beallitasa es a valtozo ertekenek megvaltoztatasa
        if hanyadik == 1:
            megjelenites.config(image=kep1)
            szoveg_kiiratas.config(text=szoveg1)
        elif hanyadik == 2:
            megjelenites.config(image=kep2)
            szoveg_kiiratas.config(text=szoveg2)
        elif hanyadik == 3:
            megjelenites.config(image=kep3)
            szoveg_kiiratas.config(text=szoveg3)
        elif hanyadik == 4:
            megjelenites.config(image=kep4)
            szoveg_kiiratas.config(text=szoveg4)
        elif hanyadik == 5:
            megjelenites.config(image=kep5)
            szoveg_kiiratas.config(text=szoveg5)
        else:
            hanyadik = 1
            megjelenites.config(image=kep1)
            szoveg_kiiratas.config(text=szoveg1)

        return hanyadik     #a szamlalo megvaltozott ertekenek visszajuttatasa a profram fo reszebe
            
        
    def hatra_menet():  #a hatra leptetest vegzo fuggveny definialasa
        global hanyadik     #a szamlalo valtozo localissa tetele
        hanyadik = hanyadik - 1     #a szamlalo ertekenek csokkentese 1-el
        
        
        #a szamlalo allasa szerint a latott kep beallitasa es a valtozo ertekenek megvaltoztatasa
        if hanyadik == 1:
            megjelenites.config(image=kep1)
            szoveg_kiiratas.config(text=szoveg1)
        elif hanyadik == 2:
            megjelenites.config(image=kep2)
            szoveg_kiiratas.config(text=szoveg2)
        elif hanyadik == 3:
            megjelenites.config(image=kep3)
            szoveg_kiiratas.config(text=szoveg3)
        elif hanyadik == 4:
            megjelenites.config(image=kep4)
            szoveg_kiiratas.config(text=szoveg4)
        elif hanyadik == 5:
            megjelenites.config(image=kep5)
            szoveg_kiiratas.config(text=szoveg5)
        else:
            hanyadik = 5
            megjelenites.config(image=kep5)
            szoveg_kiiratas.config(text=szoveg5)

        return hanyadik     #a szamlalo megvaltozott ertekenek visszajuttatasa a profram fo reszebe
        
    
    #a fuggvenyeket futtato gombok letrehozasa es elhelyezese
    elore_gomb = Button(d_galeria_main, text="=>", command=elore_menet).place(relx=0.85, rely=0.6, anchor=CENTER)
    hatra_gomb = Button(d_galeria_main, text="<=", command=hatra_menet).place(relx=0.15, rely=0.6, anchor=CENTER)
    
    
    #a program folyamatos futasat vegzo fuggveny meghivas
    d_galeria_main.mainloop()
    

# #egy masik programbol torteno meghivashoz sukseges fuggveny meghivasa
# galeria_d()