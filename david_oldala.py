from tkinter import *
import tkinter as tk 
from tkinter import ttk 
from tkinter import scrolledtext 
import time


root = Tk()
root.title("Dávid oldali chat")
root.geometry("550x500")
root.resizable(width=False, height=False)
# root.configure(bg="#257180")

text = tk.Text(root, height=15, width=65) 
scroll = tk.Scrollbar(root) 
text.configure(yscrollcommand=scroll.set, padx=5) 
text.place(relx=0.5, rely=0.26, anchor=CENTER)


# #szovegbeolvasas1 ------------------------------------------------
# textbox = tk.Text(root, height=5, width=10)
# scroll = tk.Scrollbar(root) 
# textbox.configure(yscrollcommand=scroll.set, borderwidth=2, relief="solid", padx=5) 
# textbox.place(relx=0.3, rely=0.8, anchor=CENTER)
# #------------------------------------------------------------------


#szovegbeolvasas2 ------------------------------------------------
szoveg = Entry(root, borderwidth=2, width=40)
szoveg.place(relx=0.3, rely=0.7, anchor=CENTER)
#------------------------------------------------------------------


def fofuggveny():
    # #szovegbeolvasas1 ------------------------------------------------
    # asd = textbox.get(1.0, "end-1c")
    # if asd != "":    
    #     with open('./messages.txt', 'a', encoding='utf-8') as irogatas:
    #         print(80, asd, sep=";", file=irogatas)
    # #------------------------------------------------------------------

    
    #szovegbeolvasas2 ------------------------------------------------
    beolv_soveg = szoveg.get()
    if beolv_soveg != "":    
        with open('./messages.txt', 'a', encoding='utf-8') as irogatas:
            print(80, beolv_soveg, sep=";", file=irogatas)
    #------------------------------------------------------------------

    with open('./messages.txt', 'r', encoding='utf-8') as uzenetek:
        for i in uzenetek:
            i = i.split(';')
            x = i[1].replace("\n", "")          
            i = [int(i[0]), str(x)]
            print(i)
            if i[0] == 80:
                text.insert(tk.END, i[1] + "\n", "david")
                text.tag_config("david", foreground="white", background="darkgreen", font="rubik 12 bold", justify="right", borderwidth=1, relief="solid")
            elif i[0] == 420:
                text.insert(tk.END, i[1] + "\n", "patrik")
                text.tag_config("patrik", foreground="white", background="red", font="rubik 12 bold", justify="left", borderwidth=1, relief="solid")
            
    text.config(state=tk.DISABLED)
    text.delete("1.0", END)
    
    bekero_gomb = Button(root, text="Küldés", font="Rubik 10 bold", command=fofuggveny).place(relx=0.75, rely=0.7, anchor=CENTER)
    
    root.mainloop()
    
fofuggveny()










# import tkinter as tk

# # Function to send a message
# def send_message():
#     message = message_entry.get()
#     if message:
#         message_history.config(state=tk.NORMAL)
#         message_history.insert(tk.END, f"You: {message}\n")
#         message_history.config(state=tk.DISABLED)
#         message_entry.delete(0, tk.END)

# # Create the main window
# parent = tk.Tk()
# parent.title("Chat Application")

# # Create a Text widget for message history
# message_history = tk.Text(parent, wrap=tk.WORD, width=40, height=10)
# message_history.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
# message_history.config(state=tk.DISABLED)

# # Create an Entry widget for entering messages
# message_entry = tk.Entry(parent, width=30)
# message_entry.grid(row=1, column=0, padx=10, pady=10)

# # Create a "Send" button
# send_button = tk.Button(parent, text="Send", command=send_message)
# send_button.grid(row=1, column=1, padx=10, pady=10)

# # Start the Tkinter event loop
# parent.mainloop()


