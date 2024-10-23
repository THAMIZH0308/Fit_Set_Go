# Import the required libraries
from tkinter import *
from PIL import ImageTk, Image
import customtkinter as ck
from app import application
from demo_window import demo

def ex_list():
    # Create an instance of Tkinter Frame
    win1 = Toplevel()

    # Set the geometry of Tkinter Frame
    win1.geometry("1000x600")
    win1.title("WORKOUT LIST")

    # Open the Image File
    bg = ImageTk.PhotoImage(file="workout.png")
    
    # Create a Canvas
    canvas = Canvas(win1, width=700, height=3500)
    canvas.pack(fill=BOTH, expand=True)

    # Add Image inside the Canvas
    canvas.create_image(0, 0, image=bg, anchor='nw')

    # Function to resize the window
    def resize_image(e):
        global image, resized, image2
   # open image to resize it
        image = Image.open("workout.png")
   # resize the image with width and height of root
        resized = image.resize((e.width, e.height), Image.LANCZOS)

        image2 = ImageTk.PhotoImage(resized)
        canvas.create_image(0, 0, image=image2, anchor='nw')

    # Bind the function to configure the parent window
    #win.bind("<Configure>", resize_image)
    
    welcomeLabel = ck.CTkButton(win1,fg_color=("orange"),width=200,border_width=5,corner_radius=0,height=50,text="Dead Lift",font=('Times New Roman',20),text_color='black',command=demo)
    #welcomeLabel = ck.CTkLabel(win, height=40, width=120,corner_radius=10,  font=("Roboto",24), text_color="white", fg_color="black",command=application)
    welcomeLabel.place(x=750, y=50)
    #welcomeLabel.configure(text="Let's Lift")

    welcomeLabel = ck.CTkButton(win1,fg_color=("orange"),width=200,border_width=5,corner_radius=0,height=50,text="Biceps Arm Curl",font=('Times New Roman',20),text_color='black')
    #welcomeLabel = ck.CTkLabel(win, height=40, width=120,corner_radius=10,  font=("Roboto",24), text_color="white", fg_color="black",command=application)
    welcomeLabel.place(x=750, y=150)

    welcomeLabel = ck.CTkButton(win1,fg_color=("orange"),width=200,border_width=5,corner_radius=0,height=50,text="Overhead Press",font=('Times New Roman',20),text_color='black')
    #welcomeLabel = ck.CTkLabel(win, height=40, width=120,corner_radius=10,  font=("Roboto",24), text_color="white", fg_color="black",command=application)
    welcomeLabel.place(x=750, y=250)

    welcomeLabel = ck.CTkButton(win1,fg_color=("orange"),width=200,border_width=5,corner_radius=0,height=50,text="Leg Press",font=('Times New Roman',20),text_color='black')
    #welcomeLabel = ck.CTkLabel(win, height=40, width=120,corner_radius=10,  font=("Roboto",24), text_color="white", fg_color="black",command=application)
    welcomeLabel.place(x=750, y=350) 

    welcomeLabel = ck.CTkButton(win1,fg_color=("orange"),width=200,border_width=5,corner_radius=0,height=50,text="Squat",font=('Times New Roman',20),text_color='black',command=application)
    #welcomeLabel = ck.CTkLabel(win, height=40, width=120,corner_radius=10,  font=("Roboto",24), text_color="white", fg_color="black",command=application)
    welcomeLabel.place(x=750, y=450) 

    #button = Button(text='Fit Set Go', command=application)
    #button.place(relx=0.5, rely=0.5, anchor=CENTER)
    #button.pack()

    win1.bind("<Configure>", resize_image)
    win1.mainloop()

if __name__=='__main__':
    ex_list()
