from tkinter import *
import chat

def foChat():
    root = Tk()
    root.title("Chat")
    root.geometry("1800x1000")
    root.attributes('-fullscreen', True)
    root.configure(bg='#6a6664')
    
    def bezaras():
        root.destroy()
        
    
    def megnyitasChat():
        # proba = Tk()
        # proba.title("Chat")
        # # proba.geometry("1800x1000")
        # proba.attributes('-fullscreen', True)
        # proba.configure(bg='black')
        # proba.mainloop()
        chat.chatFolyamat()
        
        
    def david_oldal():
        print("sdad")
        
    def patrik_oldal():
        print("sdad")
    
    bezaro_gomb = Button(root, text="x", bg="red", command=bezaras).place(relx=0.995, rely=0.01, anchor=CENTER)
    megnyito_chat = Button(root, text="Chat", bg="green", command=megnyitasChat).place(relx=0.2, rely=0.2, anchor=CENTER)
    megnyito_david_profil = Button(root, text="Dávid", bg="green", command=david_oldal).place(relx=0.5, rely=0.2, anchor=CENTER)
    megnyito_patrik_profil = Button(root, text="Patrik", bg="green", command=patrik_oldal).place(relx=0.8, rely=0.2, anchor=CENTER)
    
    root.mainloop()
    
# foChat()