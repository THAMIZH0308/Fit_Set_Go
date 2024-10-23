# Import the required libraries
from tkinter import *
from PIL import ImageTk, Image
import customtkinter as ck
from tkinter import messagebox
counter=5

def preset():
    global counter
    pre = Tk()

    pre.geometry("500x250")
    pre.title("PRESET")
    pre.configure(bg='orange')
    
    label = ck.CTkLabel(pre,text="Enter the target REP",width=200,height=25,corner_radius=10,bg_color='white',text_color='black')
    label.place(x=50,y=100)

    ent_get=IntVar()
    ent = ck.CTkEntry(pre,width=50,height=25,corner_radius=10,bg_color='orange',textvariable=ent_get)
    ent.place(x=300,y=100)
    set_count = ent_get.get()    
      
    def preset_submit():
        global counter
        if int(counter)==int(set_count):
            # playsound('./sound.mp3')
            label = ck.CTkLabel(pre,text="Got value",width=200,height=25,corner_radius=10,bg_color='white',text_color='black')
            label.place(x=100,y=180)
        else:
            messagebox.showerror('Print valid count !!')
    
    def close():
        pre.destroy()
    
    button1 = ck.CTkButton(pre, text='submit',corner_radius=10, command=preset_submit, height=25, width=50,  text_color="black")
    button1.place(x=300, y=180)
    
    button1 = ck.CTkButton(pre, text='close',corner_radius=10, command=close, height=25, width=50,  text_color="black")
    button1.place(x=300, y=220)
    pre.mainloop()



    pre.mainloop()

if __name__=='__main__':
    preset()
