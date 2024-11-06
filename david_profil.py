#szukseges modulok beimportalasa
from tkinter import *
from tkinter import PhotoImage


def profil_d():     #a fofuggveny definialasa
    d_profil_main = Toplevel()  #a toplevel fuggveny azt a celt, szolgalja, hogy az ablak a megnyilasakor tudja, hogy o nem egy main ablak hanem egy masodlagol ablak, amelyet masik ablakbol nyitottak meg
    d_profil_main.title("Dávid profil")     #az ablak neve
    d_profil_main.geometry("800x500")   #az ablak meretei pixelben
    d_profil_main.resizable(False, False)   #az ablak atmeretezesenek letiltasa
    d_profil_main.configure(bg='#6a6664')   #az ablak hatterszinenek beallitasa
         
         
    #a profilkep megjelenitese
    kep5 = PhotoImage(file="./kepek/david_profilkep/david_kep.gif") 
    megjelenites = Label(d_profil_main, image=kep5)
    megjelenites.place(relx=0.15, rely=0.24, anchor=CENTER)
    
    
    #a megjeleniteskor hasznalt formazasokat tartalmazo valtozok felvetele
    stilus = ("rubik", 14, "bold")
    stilus2 = ("rubik", 10, "bold") 
    
    
    #a tulajdonsagok megjelenitese es formazasa (1. oszlop)
    nev = Label(d_profil_main, text="Név: Sveiczer Dávid", font=stilus).place(relx=0.15, rely=0.52, anchor=CENTER)
    kor = Label(d_profil_main, text="Életkor: 17 esztendő", font=stilus2).place(relx=0.15, rely=0.62, anchor=CENTER)
    lakhely = Label(d_profil_main, text="Lakóhely:  8220 Balatonalmádi,\n Magyarország", font=stilus2).place(relx=0.15, rely=0.72, anchor=CENTER)
    elerhetosegek = Label(d_profil_main, text="Elérhetőségek:\n E-mail: 11c-sveiczer@ipari.vein.hu\n Telefont szám: +36 ** *** ****", font=stilus2).place(relx=0.15, rely=0.86, anchor=CENTER)
    
    #a tulajdonsagok megjelenitese es formazasa (2. oszlop)
    rovid_bemutat = Label(d_profil_main, text="Rövid bemutatkozas: „Egy tinédzser vagyok a Balatonpartról,\n szeretek társaságba járni és beszélgetni másokkal.”", font=stilus2, width=64).place(relx=0.64, rely=0.09, anchor=CENTER)
    tanulmany = Label(d_profil_main, text="Tanulmányok: „Szoftverfejlesztést és tesztelést tanulok egy szakiskolában,\n ahol az informatika iránti szenvedélyem napról-napra mélyül.”", font=stilus2, width=64).place(relx=0.64, rely=0.2, anchor=CENTER)
    szakmai = Label(d_profil_main, text="Mi motivál: „Rövid távon főleg az motivál, hogy képes legyek elkészíteni\n saját alkalmazásomat, olyanra amilyenre én szeretném. Hosszú távon pedig\n a kényelmes munka és a jó megélhetés a fő húzóerőim.”", font=stilus2, width=64).place(relx=0.64, rely=0.325, anchor=CENTER)
    celok = Label(d_profil_main, text="Célok: „Szeretném letenni az középfukú angol nyelvvizsgát, leérettségizni,\n és majd ha úgy alakul, akkor lediplomázni is.”", font=stilus2, width=64).place(relx=0.64, rely=0.455, anchor=CENTER)
    k_konyv = Label(d_profil_main, text="Érdeklődésem: „Autók és minden más robbanómotoros jármű, az informatika,\n azon belül is főleg a szoftverfejlesztés és akármilyen robot programozása,\n emellett szívesen utazom és próbálok ki különféle sportokat.”", font=stilus2, width=64).place(relx=0.64, rely=0.58, anchor=CENTER)
    hobbi = Label(d_profil_main, text="Hobbi: Motorozás,\n biciklizés, programozás,\n néha vidójátékozás", font=stilus2, width=24, height=4).place(relx=0.48, rely=0.82, anchor=CENTER)


    def galeria_megnyito(): #a galeriat megnyito fuggveny letrehozasa
        import davidgaleria
        davidgaleria.galeria_d()
    
    #a galeriat megnyito gomb letrehozasa
    galeria = Button(d_profil_main, text="Képek", command=galeria_megnyito, font=stilus, background="green", width=8, height=2)
    galeria.place(relx=0.71, rely=0.75, anchor=CENTER)
    
    
    def chat_megnyito():    #a chat-et megnyito fuggveny letrehozasa
        import david_oldala
        david_oldala.fofuggveny()
    
    #a chat-et megnyito gomb letrehozasa
    chat = Button(d_profil_main, text="Chat", command=chat_megnyito, font=stilus, background="green", width=8, height=2)
    chat.place(relx=0.88, rely=0.75, anchor=CENTER)
    
    #fajlbol beolvassa a jelenfegi felhasznalonevet
    with open('./fajlba_iras/felhasznalonev.txt', 'r', encoding='utf-8') as fajl:
        for i in fajl:
            felhasznalo = i.strip('\n')
    
    #ha a jelenlegi felhasznalo nem david (nem en vagyok), akkor a privat chat-et letiltja a privat chat gombjanak a statuszanak a megvaltoztatasaval 
    if felhasznalo != "david":
        chat.config(state=DISABLED)
    
    
    def vendeg_chat_megnyito():    #a vendeg chat-et megnyito fuggveny letrehozasa
        import vendeg_valasztas
        vendeg_valasztas.valasztasAblak_vendegeknek()
    
    #a vendeg chat-et megnyito gomb letrehozasa
    vendeg_chat = Button(d_profil_main, text="Vendég Chat", command=vendeg_chat_megnyito, font=stilus, background="green", width=16, height=2)
    vendeg_chat.place(relx=0.795, rely=0.9, anchor=CENTER)
    
    
    d_profil_main.mainloop()    #a program folyamatos futasat vegzo fuggveny meghivas


# #egy masik programbol torteno meghivashoz sukseges fuggveny meghivasa
# profil_d()