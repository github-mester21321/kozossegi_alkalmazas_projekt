#modulok beimportalasa
from tkinter import *
import tkinter as tk 
from tkinter import ttk 
from tkinter import scrolledtext 


#az ablak letrehozasa es konfiguralasa
root = Tk()
root.title("Dávid oldali chat")
root.geometry("550x500")
root.resizable(width=False, height=False)
root.configure(bg="#257180")


#a chat uzeneteit megjelenito text widget letrehozasa es a gorgethetoseg megoldasa
scroll = tk.Scrollbar(root) 
text = tk.Text(root, height=15, width=65) 
text.configure(yscrollcommand=scroll.set, padx=5) 
text.place(relx=0.5, rely=0.26, anchor=CENTER)


#az elkuldendo uzeneteket befogado text widget letrehozasa es elhelyezese
textbox = tk.Text(root, height=4, width=30)
scroll = tk.Scrollbar(root) 
textbox.configure(yscrollcommand=scroll.set, borderwidth=2, relief="solid", padx=5) 
textbox.place(relx=0.3, rely=0.7, anchor=CENTER)


#az uzeneteket feldolgozo fo fuggveny
def fofuggveny():
    #a text widget torlese
    text.delete("1.0", END)


    #a beolvasott szoveg fajlba iratasa
    asd = textbox.get(1.0, "end-1c")
    if asd != "":    
        with open('./messages.txt', 'a', encoding='utf-8') as irogatas:
            print(80, asd, sep=";", file=irogatas)


    #a fajl tartalmanak bejarasa es az uzenetek kiiratasa
    with open('./messages.txt', 'r', encoding='utf-8') as uzenetek:
        for i in uzenetek:  #a beolvasott fajl bejarasa
            i = i.split(';')    #a beolvasott sorok szetvalasztasa a ';' menten
            x = i[1].replace("\n", "")  #a .strip() nem mukodott, igy ezt hasznaltam helyette       
            i = [int(i[0]), str(x)]     #az i egy lista volt de mivel az i[1] az uzenet reszekent tartalmazta a sortorest (\n), igy az elozo sorban szetbontottam es kivettem belole a sortorest, majd az igy kapott x valtozo esteket a megmaradt i[0] ertekkel visszatoltottem az i valtozoban mint egy lista, amelynek van egy szam (felhasznalo) es egy szoveg (uzenet) eleme.
            # print(i)  #az adatstruktura ellenorzesehet hasznalt kiiratas
            if i[0] == 80:  #a felhasznalo vizsgalata
                text.insert(tk.END, i[1] + "\n", "david")   #az uzenet beillesztese a szovegmezobe
                text.tag_config("david", foreground="white", background="darkgreen", font="rubik 12 bold", justify="right", borderwidth=1, relief="solid")  #a kiiratas kinezetenek beallitasai
            elif i[0] == 420:  #a felhasznalo vizsgalata
                text.insert(tk.END, i[1] + "\n", "patrik")  #az uzenet beillesztese a szovegmezobe
                text.tag_config("patrik", foreground="white", background="red", font="rubik 12 bold", justify="left", borderwidth=1, relief="solid")    #a kiiratas kinezetenek beallitasai
            
    
    #a fofuggvenyt lefuttato gomb letrehozasa
    bekero_gomb = Button(root, text="Küldés", font="Rubik 10 bold", command=fofuggveny).place(relx=0.75, rely=0.7, anchor=CENTER)
    

    #az ablak nyitvamaradasazoz szukseges beepitett fuggveny
    root.mainloop()
    

#a fuggveny meghivasa, ami csak a fejlesztes es a teszteles alatt kell
fofuggveny()