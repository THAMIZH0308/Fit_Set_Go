from tkinter import *
from PIL import ImageTk, Image
import customtkinter as ck
from app import application
import tkinter as tk
from tkVideoPlayer import TkinterVideo


def demo():
    # Create an instance of Tkinter Frame
    win2 = Toplevel()

    # Set the geometry of Tkinter Frame
    win2.geometry("1000x600")
    win2.title("WORKOUT LIST")

    # Open the Image File
    bg = ImageTk.PhotoImage(file="workout.png")

    # Create a Canvas
    canvas = Canvas(win2, width=700, height=3500)
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

    def video():
        root = tk.Toplevel()
        root.geometry('800x500')
        root.title('Demo_video')
        videoplayer = TkinterVideo(master=root, scaled=True)
        videoplayer.load(r"demo.mp4")
        videoplayer.pack(expand=True, fill="both")

        videoplayer.play()  # play the video

        root.mainloop()

    # Bind the function to configure the parent window
    # win.bind("<Configure>", resize_image)
    classLabel = ck.CTkLabel(win2, height=40, width=120,  font=(
        "Times New Roman", 18), text_color="white", padx=10, bg_color='black')
    classLabel.place(x=740, y=30)
    classLabel.configure(
        text='first Time?\n checkout demo video ')
    welcomeLabel = ck.CTkButton(win2, fg_color=("orange"), width=200, border_width=5, corner_radius=0, height=50,
                                text="Click here for demo", font=('Times New Roman', 20), text_color='black', command=video)
    # welcomeLabel = ck.CTkLabel(win, height=40, width=120,corner_radius=10,  font=("Roboto",24), text_color="white", fg_color="black",command=application)
    welcomeLabel.place(x=730, y=100)

    classLabel1 = ck.CTkLabel(win2, height=40, width=120,  font=(
        "Times New Roman", 18), text_color="white", padx=10, bg_color='black')
    classLabel1.place(x=740, y=250)
    classLabel1.configure(
        text='Hit the below button to\n try the workout')
    welcomeLabel1 = ck.CTkButton(win2, fg_color=("orange"), width=200, border_width=5, corner_radius=0, height=50,
                                text="Click here for demo", font=('Times New Roman', 20), text_color='black', command=application)
    # welcomeLabel = ck.CTkLabel(win, height=40, width=120,corner_radius=10,  font=("Roboto",24), text_color="white", fg_color="black",command=application)
    welcomeLabel1.place(x=730, y=320)

    win2.bind("<Configure>", resize_image)
    win2.mainloop()


if __name__ == '__main__':
    demo()
