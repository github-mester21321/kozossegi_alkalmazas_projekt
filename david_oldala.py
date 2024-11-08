#szukseges modulok beimportalasa
from tkinter import *
import tkinter as tk 
from tkinter import ttk 
from tkinter import scrolledtext 


#az ablak letrehozasa es konfiguralasa
d_chat_main = Toplevel()    #a toplevel fuggveny azt a celt, szolgalja, hogy az ablak a megnyilasakor tudja, hogy o nem egy main ablak hanem egy masodlagol ablak, amelyet masik ablakbol nyitottak meg
d_chat_main.title("Dávid oldali chat")
d_chat_main.geometry("550x500")
d_chat_main.resizable(width=False, height=False)    #az ablak atmeretezesenek letiltasa
d_chat_main.configure(bg="#257180")


#a chat uzeneteit megjelenito text widget letrehozasa es a gorgethetoseg megoldasa
scroll = tk.Scrollbar(d_chat_main) 
text = tk.Text(d_chat_main, height=15, width=65)
text.configure(yscrollcommand=scroll.set, padx=5) 
text.place(relx=0.5, rely=0.26, anchor=CENTER)
text.configure(state=DISABLED)  #a text widget atirasanak blokkolasa, hogy ne lehessen kitotolni az uzeneteket


#az elkuldendo uzeneteket befogado text widget letrehozasa es elhelyezese
textbox = tk.Text(d_chat_main, height=4, width=30)
scroll = tk.Scrollbar(d_chat_main) 
textbox.configure(yscrollcommand=scroll.set, borderwidth=2, relief="solid", padx=5) 
textbox.place(relx=0.3, rely=0.7, anchor=CENTER)


#az uzeneteket feldolgozo fo fuggveny
def fofuggveny():
    #a text widget atirasanak lehetove telele az uzenetek kiiratasanak idejere
    text.configure(state=NORMAL)
    
    
    #a text widget torlese
    text.delete("1.0", END)


    #a beolvasott szoveg fajlba iratasa
    asd = textbox.get(1.0, "end-1c")
    if asd != "":    
        with open('./fajlba_iras/messages.txt', 'a', encoding='utf-8') as irogatas:
            print("david", asd, sep=";", file=irogatas)


    #a fajl tartalmanak bejarasa es az uzenetek kiiratasa
    with open('./fajlba_iras/messages.txt', 'r', encoding='utf-8') as uzenetek:
        for i in uzenetek:  #a beolvasott fajl bejarasa
            i = i.split(';')    #a beolvasott sorok szetvalasztasa a ';' menten
            x = i[1].replace("\n", "")  #a .strip() nem mukodott, igy ezt hasznaltam helyette       
            i = [str(i[0]), str(x)]     #az i egy lista volt de mivel az i[1] az uzenet reszekent tartalmazta a sortorest (\n), igy az elozo sorban szetbontottam es kivettem belole a sortorest, majd az igy kapott x valtozo esteket a megmaradt i[0] ertekkel visszatoltottem az i valtozoban mint egy lista, amelynek van egy szam (felhasznalo) es egy szoveg (uzenet) eleme.
            # print(i)  #az adatstruktura ellenorzesehet hasznalt kiiratas
            if i[0] == "david":  #a felhasznalo vizsgalata
                text.insert(tk.END, i[1] + "\n", "david")   #az uzenet beillesztese a szovegmezobe
                text.tag_config("david", foreground="white", background="darkgreen", font="rubik 12 bold", justify="right", borderwidth=1, relief="solid")  #a kiiratas kinezetenek beallitasai
                text.yview(END)     #az uzenetek kiiratasakor a nezopont ne ugorjon fel a lap tetejere, hanem maradjon a lap aljan az aktualis (utolso) kiiratasnal
            else:  #a felhasznalo vizsgalata
                text.insert(tk.END, f"{i[0]}: {i[1]}" + "\n", "mas")  #az uzenet beillesztese a szovegmezobe
                text.tag_config("mas", foreground="white", background="red", font="rubik 12 bold", justify="left", borderwidth=1, relief="solid")    #a kiiratas kinezetenek beallitasai
                text.yview(END)     #az uzenetek kiiratasakor a nezopont ne ugorjon fel a lap tetejere, hanem maradjon a lap aljan az aktualis (utolso) kiiratasnal


        #az uzenetek kiiratasa utan a text widget atirasanak ujra blokkolasa
        text.configure(state=DISABLED)
        
        
    #a fofuggvenyt lefuttato gomb letrehozasa
    bekero_gomb = Button(d_chat_main, text="Küldés", font="Rubik 10 bold", command=fofuggveny).place(relx=0.75, rely=0.7, anchor=CENTER)
    

    #az ablak nyitvamaradasazoz szukseges beepitett fuggveny
    d_chat_main.mainloop()
    

#a fuggveny meghivasa, ami csak a fejlesztes es a teszteles alatt kell
fofuggveny()