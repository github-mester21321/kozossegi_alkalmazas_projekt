from tkinter import *
from tkinter import PhotoImage

def foOldal():
    root = Toplevel()
    root.title("Patrik profil")
    root.geometry("800x500")
    # root.attributes('-fullscreen', True)
    root.configure(bg='#6a6664')
    font = ("rubik", 14, "bold")
    font2 = ("rubik", 10, "bold") 
    profilkep = PhotoImage(file="./kepek/patrik_profilkep/patrik.gif")
    megjelenites = Label(root, image=profilkep)
    megjelenites.place(relx=0.15, rely=0.24, anchor=CENTER)
    nev = Label(root, text="Név: Pók Patrik", font=font).place(relx=0.15, rely=0.52, anchor=CENTER)
    kor = Label(root, text="Életkor: 17 éves", font=font2).place(relx=0.15, rely=0.62, anchor=CENTER)
    lakhely = Label(root, text="Lakóhely: Pétfürdő, Magyarország", font=font2).place(relx=0.155, rely=0.72, anchor=CENTER)
    rovid_bemutat = Label(root, text="Rövid bemutatkozás: Pók Patrik vagyok, falusi gyerek Pétfürdőről. Nagyon érdekel az \n informatika világa, hiszen szeretek a semmiből építkezni és hálózatokkal foglalkozni.", font=font2).place(relx=0.64, rely=0.1, anchor=CENTER)
    tanulmany = Label(root, text="Tanulmányok: VSZC Ipari Technikum", font=font2).place(relx=0.64, rely=0.22, anchor=CENTER)
    k_zene = Label(root, text="Kedvenc zene: Metallica - Disposable Heroes", font=font2).place(relx=0.64, rely=0.34, anchor=CENTER)
    hobbi = Label(root, text="Hobbi:\nZeneírás, basszusgitározás\nTestépítés", font=font2, width=24, height=4).place(relx=0.6, rely=0.46, anchor=CENTER)
        
    def patrik_oldal():  
        import patrik_oldala 
        patrik_oldala.fofuggveny()
    
    def galeria_oldal():
        import patrikgaleria
        patrikgaleria.galeria_p()

    def vendeg_chat_megnyito():
        import vendeg_valasztas
        vendeg_valasztas.valasztasAblak_vendegeknek()
    
    megnyito_patrik_profil = Button(root, text="Chat", bg="green", height=2, width=8, command=patrik_oldal).place(relx=0.71, rely=0.78, anchor=CENTER)
    galeria_gomb = Button(root, text="Képek", bg="green", height=2, width=8, command=galeria_oldal).place(relx=0.88, rely=0.78, anchor=CENTER)
    vendeg_chat = Button(root, text="Vendég Chat", command=vendeg_chat_megnyito, font=font, background="green", width=16, height=2)
    vendeg_chat.place(relx=0.795, rely=0.9, anchor=CENTER)
    
    root.mainloop()
    
# foOldal()
