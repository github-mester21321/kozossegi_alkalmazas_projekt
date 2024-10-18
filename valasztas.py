from tkinter import *
import david_oldala
import galeria
import patrik_oldala

def valasztasAblak():
    root = Tk()
    root.title("Választás")
    root.geometry("300x100")
    # root.attributes('-fullscreen', True)
    root.configure(bg='#6a6664')
        
        
    def david_oldal():
        david_oldala.fofuggveny()

    def galeria_oldal():
        galeria.sad()

    def patrik_oldal():
        patrik_oldala.ablak()
        
    
    megnyito_david_profil = Button(root, text="Dávid", bg="green", height=2, width=8, command=david_oldal).place(relx=0.2, rely=0.5, anchor=CENTER)
    galeria_gomb = Button(root, text="Galéria", bg="green", height=2, width=8, command=david_oldal).place(relx=0.5, rely=0.5, anchor=CENTER)
    megnyito_patrik_profil = Button(root, text="Patrik", bg="green", height=2, width=8, command=patrik_oldal).place(relx=0.8, rely=0.5, anchor=CENTER)
    
    root.mainloop()
    
#valasztasAblak()