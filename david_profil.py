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
    kep5 = PhotoImage(file="./szabo_peti.gif") 
    megjelenites = Label(d_profil_main, image=kep5)
    megjelenites.place(relx=0.15, rely=0.24, anchor=CENTER)
    
    
    #a megjeleniteskor hasznalt formazasokat tartalmazo valtozok felvetele
    stilus = ("rubik", 14, "bold")
    stilus2 = ("rubik", 10, "bold") 
    
    
    #a tulajdonsagok megjelenitese es formazasa (1. oszlop)
    nev = Label(d_profil_main, text="Név: Szabó Péter", font=stilus).place(relx=0.15, rely=0.52, anchor=CENTER)
    kor = Label(d_profil_main, text="Életkor: 30 esztendő", font=stilus2).place(relx=0.15, rely=0.62, anchor=CENTER)
    lakhely = Label(d_profil_main, text="Lakóhely: Szeged, Magyarország", font=stilus2).place(relx=0.155, rely=0.72, anchor=CENTER)
    elerhetosegek = Label(d_profil_main, text="Elérhetőségek:\n E-mail: peter.szabo@email.com\n Telefont szám: +36 30 123 4567", font=stilus2).place(relx=0.15, rely=0.86, anchor=CENTER)
    
    #a tulajdonsagok megjelenitese es formazasa (2. oszlop)
    rovid_bemutat = Label(d_profil_main, text="Rövid bemutatkozas: „Számítógéprajongó és szenvedélyes utazó vagyok.\n Mindig keresem az új lehetőségeket, hogy felfedezzem a világot!”", font=stilus2).place(relx=0.64, rely=0.1, anchor=CENTER)
    tanulmany = Label(d_profil_main, text="Tanulmányok: „Informatikai diplomát szereztem a Szegedi Tudományegyetemen,\n ahol a mesterséges intelligenciára specializálódtam.”", font=stilus2).place(relx=0.64, rely=0.22, anchor=CENTER)
    szakmai = Label(d_profil_main, text="Szakmai háttér: „Több mint 7 éve dolgozom szoftverfejlesztőként,\n és jelenleg egy innovatív startup csapat tagja vagyok.”", font=stilus2).place(relx=0.64, rely=0.34, anchor=CENTER)
    celok = Label(d_profil_main, text="Célok: „Szeretném a következő öt évben saját technológiai vállalkozást alapítani,\n amely fenntartható megoldásokat kínál.”", font=stilus2).place(relx=0.64, rely=0.46, anchor=CENTER)
    k_konyv = Label(d_profil_main, text="Kedvenc könyveim: „Isaac Asimov: Alapítvány, Frank Herbert: Dűne”", font=stilus2).place(relx=0.64, rely=0.56, anchor=CENTER)
    k_zene = Label(d_profil_main, text="Kedvenc zene: „Rock és elektronikus zene, különösen a Coldplay és a Daft Punk.”", font=stilus2).place(relx=0.64, rely=0.64, anchor=CENTER)
    hobbi = Label(d_profil_main, text="Hobbi:\nFutás, Zeneírás\nHegymászás, Festészet\nGasztronómiai kísérletezés", font=stilus2, width=24, height=4).place(relx=0.48, rely=0.78, anchor=CENTER)


    def galeria_megnyito(): #a galeriat megnyito fuggveny letrehozasa
        import davidgaleria
        davidgaleria.galeria_d()
    
    #a galeriat megnyito gomb letrehozasa
    galeria = Button(d_profil_main, text="Képek", command=galeria_megnyito, font=stilus, background="green", width=8, height=2).place(relx=0.71, rely=0.78, anchor=CENTER)
    
    
    def chat_megnyito():    #a chat-et megnyito fuggveny letrehozasa
        import david_oldala
        david_oldala.fofuggveny()
    
    #a chat-et megnyito gomb letrehozasa
    chat = Button(d_profil_main, text="Chat", command=chat_megnyito, font=stilus, background="green", width=8, height=2).place(relx=0.88, rely=0.78, anchor=CENTER)
    
    
    d_profil_main.mainloop()    #a program folyamatos futasat vegzo fuggveny meghivas


# #egy masik programbol torteno meghivashoz sukseges fuggveny meghivasa
# profil_d()