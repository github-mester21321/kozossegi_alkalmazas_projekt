#kiegeszitok beimportalasa
from tkinter import *

def regisztaciosAblak():
    root = Tk()
    root.title("Regisztráció")
    root.geometry("300x350")
    root.configure(bg='#6a6664')
    root.resizable(False, False)  #az ablak atmeretezesenek letiltasa


    #az 'uj felhasznalonev' megjelenito szoveg megjelenitese
    elso_szoveg = Label(root, text="Új felhasználónév: ", font="rubik 10 bold").place(relx=0.25, rely=0.06, anchor=CENTER)
    #az uj felhasznalonevet bekero mezo letrehozasa es megjelenitese
    felhasznalonev = Entry(root, borderwidth=2)
    felhasznalonev.place(relx=0.75, rely=0.06, anchor=CENTER)


    #az 'uj jelszo' megjelenito szoveg megjelenitese
    masodik_szoveg = Label(root, text="Új jelszó: ", font="rubik 10 bold").place(relx=0.25, rely=0.15, anchor=CENTER)
    #az uj jelszavat bekero mezo letrehozasa es megjelenitese
    jelszo = Entry(root, borderwidth=2)
    jelszo.place(relx=0.75, rely=0.15, anchor=CENTER)


    def bekeres():  #az uj felhasznalonevet es jelszavat bekero, ellenorzo es mento fuggveny letrehozasa
        f_nevek_es_jelsz = []   #a felhasznalonevet es jelszot eltarolo lista letrehozasa
        felhasznalo_neve = felhasznalonev.get() #a felhasznalonev mezo ertekenek beolvasasa es valtozoba mentese
        felhasznalo_jelszava = jelszo.get() #a jelszo mezo ertekenek beolvasasa es valtozoba mentese
        with open('./fajlba_iras/felhasznalo_jelszo_kombinacio.txt', 'r', encoding="utf-8") as fajl:    #a mar meglevo felhasznaloneveket es jelszavakat tartalmazo jegyzet megnyitasa es bejarasa
            for i in fajl:
                i.strip()
                i = i.split(";") #a beolsasott adatok szetvalasztasa a megadott karakter menten
                # print(i)
                x = i[1].replace("\n", "")  #a .strip valamiert nem tunteti el a sor vegi \n sor veget jelzo karaktert igy azt men torli a program, hanem kicseréli a semmire (ez is torlesnek felel meg)
                adat = [i[0], x]    #a felhasznalonev es jelszo listaba torteno visszatoltese
                # print(adat)
                f_nevek_es_jelsz.append(adat)   #a felhasznalonev es jelszo lista hozzaadasa a f_nevek_es_jelsz listahoz
                # print(f_nevek_es_jelsz)
            
            megfelel_e = True #a kereses miatt kell
            for i in f_nevek_es_jelsz:  #f_nevek_es_jelsz lista bejarasa
                # print(i)
                if i[0] == felhasznalo_neve and i[1] == felhasznalo_jelszava:   #ha a f_nevek_es_jelsz lista elemei meg nem szerepelnek a mar regisztraltak kozott akkor nem allitja at a megfelel_e erteket
                    megfelel_e = False
                    break
                                   
        if felhasznalo_neve == "" or felhasznalo_jelszava == "":    #ha a felhasznalonev es a jelszo is valami, akkor nem valtoztatja meg a megfelel_e erteket 
            megfelel_e = False
         
        if megfelel_e == True:  #ha a felhasznalonev es a jelszo is megfeleltek a kovetelmenyeknek akkor itt elmentesre kerulnek 
            kombinacio = [felhasznalo_neve, felhasznalo_jelszava]
            f_nevek_es_jelsz.append(kombinacio)  
            with open ('./fajlba_iras/felhasznalo_jelszo_kombinacio.txt', 'w', encoding="utf-8") as fajl2:            
                for adat_sorok in f_nevek_es_jelsz:
                    print(adat_sorok[0], adat_sorok[1], sep=";", file=fajl2)

            visszajelzes = Label(root, text="Az általad megadott felhasználónév és \n jelszó páros el lettek mentve.")
            visszajelzes.place(relx=0.5, rely=0.4, anchor=CENTER)   #visszajelzes a felhasznalonev es jelszo menteserol
        
        elif megfelel_e == False:
            visszajelzes = Label(root, text="Add meg újra!")    #visszajelzes a felhasznalonev es jelszo meg nem tortent menteserol
            visszajelzes.place(relx=0.5, rely=0.4, anchor=CENTER)


    #az uj felhasznalonevet es jelszavat bekero fuggvenyt futtato gomb letrehozasa es elhelyezese
    bekeres_gomb = Button(root, text="Enter", command=bekeres).place(relx=0.5, rely=0.6, anchor=CENTER)


    #a program folyamatos futasat biztosito fuggveny
    root.mainloop()


# #egy masik programbol torteno meghivashoz sukseges fuggveny meghivasa
# regisztaciosAblak()