from tkinter import * 
import customtkinter as ck
from app import dead_lift

window = Tk()
window.geometry("480x700")
window.title("ML_APP") 
b1=Button(text='test',command=dead_lift)
b1.pack()

window.mainloop()

'''

classLabel = ck.CTkLabel(window, height=40, width=120,  font=("Roboto",24), text_color="black", padx=10)
classLabel.place(x=10, y=1)
classLabel.configure(text='STAGE') 
counterLabel = ck.CTkLabel(window, height=40, width=120,  font=("Roboto",24), text_color="black", padx=10)
counterLabel.place(x=160, y=1)
counterLabel.configure(text='REPS') 
probLabel  = ck.CTkLabel(window, height=40, width=120, font=("Roboto",24), text_color="black", padx=10)
probLabel.place(x=300, y=1)
probLabel.configure(text='PROB') 
classBox = ck.CTkLabel(window, height=40, width=120,  font=("Roboto",24), text_color="white", fg_color="blue")
classBox.place(x=10, y=41)
classBox.configure(text='0') 
counterBox = ck.CTkLabel(window, height=40, width=120,  font=("Roboto",24), text_color="white", fg_color="blue")
counterBox.place(x=160, y=41)
counterBox.configure(text='0') 
probBox = ck.CTkLabel(window, height=40, width=120,  font=("Roboto",24), text_color="white", fg_color="blue")
probBox.place(x=300, y=41)
probBox.configure(text='0') 
'''