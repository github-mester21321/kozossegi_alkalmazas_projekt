from tkinter import *
import david_profil
import patrikgaleria


def valasztasAblak():
    root = Toplevel()
    root.title("Választás")
    root.geometry("300x140")
    # root.attributes('-fullscreen', True)
    root.configure(bg='#6a6664')
         
    
    def david_p_megnyito():
        david_profil.profil_d()
    
    def partik_p_megnyito():
        pass  
    
    # def galeria_david():
    #     davidgaleria.galeria_d()

    def galeria_patrik():
        patrikgaleria.galeria_p()
      
    
    megnyito_david_profil = Button(root, text="Dávid profil", bg="green", height=2, width=10, command=david_p_megnyito).place(relx=0.30, rely=0.25, anchor=CENTER)
    megnyito_patrik_profil = Button(root, text="Patrik profil", bg="green", height=2, width=10, command=partik_p_megnyito).place(relx=0.70, rely=0.25, anchor=CENTER)
    # megnyito_david_galeria = Button(root, text="Dávid galéria", bg="green", height=2, width=10, command=david_p_megnyito).place(relx=0.30, rely=0.75, anchor=CENTER)
    megnyito_patrik_galeria = Button(root, text="Patrik galéria", bg="green", height=2, width=10, command=partik_p_megnyito).place(relx=0.70, rely=0.75, anchor=CENTER)
    

    root.mainloop()
    
# valasztasAblak()