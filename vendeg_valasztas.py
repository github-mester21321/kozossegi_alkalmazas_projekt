#szukseges modulok beimportalasa
from tkinter import *
import david_profil
import tkinter as tk 
from tkinter import ttk 
from tkinter import scrolledtext
import patrik_profil


def valasztasAblak_vendegeknek():   #a megnyitas miatt szukkseges fuggveny letrehozasa
    root = Toplevel() #az ablak letrehozaas
    root.title("Vendég felhasználói felület") #az ablakcim beallitasa
    root.geometry("820x700")    #az ablak felbontasanak beallitasa
    # root.attributes('-fullscreen', True) #teljes kepernyos nezet beallitasa
    root.configure(bg='#6a6664')    #a hatterszin beallitasa
    root.resizable(False, False)  #az ablak atmeretezesenek letiltasa
         
    
    scroll = tk.Scrollbar(root) #a mezo gorgethetosegenek engedelyezese
    text = tk.Text(root, height=30, width=100)  #a szovegmezo letrehozasa 
    text.configure(yscrollcommand=scroll.set, padx=5) #a gorgo beallitasa
    text.place(relx=0.5, rely=0.35, anchor=CENTER)  #a szovegmezo elhelyezese
    text.configure(state=DISABLED)  #a szoveg atirhatatlansagat bizositva a mezo szerkeszthetosegenek letiltasa

    textbox = tk.Text(root, height=2, width=50) #a szovegmezo letrehozasa
    scroll = tk.Scrollbar(root) #a mezo gorgethetosegenek engedelyezese
    textbox.configure(yscrollcommand=scroll.set, borderwidth=2, relief="solid", padx=5) 
    textbox.place(relx=0.3, rely=0.75, anchor=CENTER)   #a szovegmezo elhelyezese
    
    
    def fofuggveny():   #az uzenetek kuldeseert es fogadasaert felelos fuggveny letrehozasa
        with open('./fajlba_iras/felhasznalonev.txt', 'r', encoding='utf-8') as fajl:  #az aktualis felhasznalonev beolvasasa
            for i in fajl:
                # print("das", i.strip('\n'))
                felhasznalo = i.strip('\n')
        uzenet = textbox.get(1.0, "end-1c") #a kuldendo uzenet beolvasasa es valtozoba mentese
        # print(uzenet, "sad")
        uzenet.strip('\n')
        if uzenet != "":    #ha az uzenet nem "" (semmi), akkor az uzenet hozzaadasa az uzeneteket tartalmazo allomanhoz (kiiratas, mentes) 
            with open('./fajlba_iras/vendegmessages.txt', 'a', encoding='utf-8') as irogatas:
                print(felhasznalo, uzenet, sep=";", file=irogatas)

        with open('./fajlba_iras/vendegmessages.txt', 'r', encoding='utf-8') as uzenetek:   #a beerkezo es az elkuldott uzenetek beolvasasa a felhasznalonevekkel egyutt
            text.configure(state=NORMAL)  #a szoveg atirhatosagat bizositva a mezo szerkeszthetosegenek engedelyezese
            text.delete("1.0", END) #a szovegmezo tartalmanak torlese
            for i in uzenetek:
                i = i.split(';')
                x = i[1].replace("\n", "")          
                if str(i[0]) == felhasznalo:    #ha az uzenetet a jelenlegi felhasznalo irta, akkor az uzenet a jobb oldalon jelenik meg zold szinnel korbeveve
                    text.insert(tk.END, x + "\n", "sajat")  #az uzenet hozzaadasa az uzenetek aljahoz
                    text.tag_config("sajat", foreground="white", background="darkgreen", font="rubik 12 bold", justify="right", borderwidth=1, relief="solid")  #a kiiratas kinezetenek beallitasai
                    text.yview(END) #ez azert szukseges, hogy egy uj bekuldott uzenetkor a kep ne ugorjon a text box tetejere 
                else:   #ha az uzenetet a nem jelenlegi felhasznalo irta, akkor az uzenet a bal oldalon jelenik meg piros szinnel korbeveve
                    text.insert(tk.END, f"{i[0]}: {x}\n", "idegen") #az uzenet hozzaadasa az uzenetek aljahoz
                    text.tag_config("idegen", foreground="white", background="red", font="rubik 12 bold", justify="left", borderwidth=1, relief="solid")    #a kiiratas kinezetenek beallitasai
                    text.yview(END) #ez azert szukseges, hogy egy uj bekuldott uzenetkor a kep ne ugorjon a text box tetejere 
        
        text.configure(state=DISABLED)  #a szoveg atirhatatlansagat bizositva a mezo szerkeszthetosegenek letiltasa
        
        
        #az uzenetek kuldeseert es fogadasaert felelos fuggvenyt lefuttato gomb letrehozasa es elhelyezese
        bekero_gomb = Button(root, text="Küldés", font="Rubik 10 bold", command=fofuggveny, height=2, width=10, bg="green").place(relx=0.75, rely=0.75, anchor=CENTER)
            
            
        def david_p_megnyito():     #a david profilt megnyito fuggveny
            david_profil.profil_d() #maga a megnyitas
            
        def partik_p_megnyito():    #a patrik profilt megnyito fuggveny
            patrik_profil.foOldal() #maga a megnyitas
            
            
        #a david profilt megnyito gomb letrehozasa es elhelyezese
        megnyito_david_profil = Button(root, text="Dávid profil", font="Rubik 10 bold", bg="green", height=2, width=10, command=david_p_megnyito).place(relx=0.30, rely=0.85, anchor=CENTER)
        
        #a patrik profilt megnyito gomb letrehozasa es elhelyezese
        megnyito_patrik_profil = Button(root, text="Patrik profil", font="Rubik 10 bold", bg="green", height=2, width=10, command=partik_p_megnyito).place(relx=0.70, rely=0.85, anchor=CENTER)
            
            
        #a program folyamatos futasat biztosito fuggveny
        root.mainloop()
    
    
    #az uzenetek megnyitaskor torteno kiiratasat biztosito fuggveny meghivasa
    fofuggveny()
    
    
# #egy masik programbol torteno meghivashoz sukseges fuggveny meghivasa
# valasztasAblak_vendegeknek()