# Import the required libraries
from tkinter import *
from PIL import ImageTk, Image
import customtkinter as ck
from workout_List import ex_list
from demo_window import demo


# Create an instance of Tkinter Frame
win = Tk()

# Set the geometry of Tkinter Frame
win.geometry("700x450")
win.title("FIT_SET_GO")

# Open the Image File
bg = ImageTk.PhotoImage(file="bg_img.jpg")

# Create a Canvas
canvas = Canvas(win, width=700, height=3500)
canvas.pack(fill=BOTH, expand=True)

# Add Image inside the Canvas
canvas.create_image(0, 0, image=bg, anchor='nw')

# Function to resize the window
def resize_image(e):
   global image, resized, image2
   # open image to resize it
   image = Image.open("bg_img.jpg")
   # resize the image with width and height of root
   resized = image.resize((e.width, e.height), Image.LANCZOS)

   image2 = ImageTk.PhotoImage(resized)
   canvas.create_image(0, 0, image=image2, anchor='nw')

   # Bind the function to configure the parent window
   #win.bind("<Configure>", resize_image)

welcomeLabel = ck.CTkButton(win,fg_color=("orange"),width=120,border_width=0,corner_radius=8,height=32,text="Let's Lift",text_color='black',command=ex_list)
   #welcomeLabel = ck.CTkLabel(win, height=40, width=120,corner_radius=10,  font=("Roboto",24), text_color="white", fg_color="black",command=application)
welcomeLabel.place(x=300, y=40)
   #welcomeLabel.configure(text="Let's Lift")

   #button = Button(text='Fit Set Go', command=application)
   #button.place(relx=0.5, rely=0.5, anchor=CENTER)
   #button.pack()

win.bind("<Configure>", resize_image)
win.mainloop()


