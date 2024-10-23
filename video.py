import tkinter as tk
from tkVideoPlayer import TkinterVideo
def video():
    root = tk.Tk()
    root.geometry('800x500')
    videoplayer = TkinterVideo(master=root, scaled=True)
    videoplayer.load(r"demo.mp4")
    videoplayer.pack(expand=True, fill="both")

    videoplayer.play() # play the video

    root.mainloop()
