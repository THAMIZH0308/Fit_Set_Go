import tkinter as tk 
import customtkinter as ck 
from tkinter import *
import pandas as pd 
import numpy as np 
import pickle 
import os
from playsound import playsound
import mediapipe as mp
import cv2
from PIL import Image, ImageTk 
from landmarks import landmarks
from tkinter import messagebox
from preset import preset
import time
import multiprocessing
def application():
    window = tk.Tk()
    window.geometry("480x700")
    window.title("DeadLift_Tracker") 
    ck.set_appearance_mode("Light")

    classLabel = ck.CTkLabel(window, height=40, width=120,  font=("Roboto",24), text_color="black", padx=10)
    classLabel.place(x=10, y=1)
    classLabel.configure(text='STAGE') 
    counterLabel = ck.CTkLabel(window, height=40, width=120,  font=("Roboto",24), text_color="black", padx=10)
    counterLabel.place(x=160, y=1)
    counterLabel.configure(text='REPS') 
    probLabel  = ck.CTkLabel(window, height=40, width=120, font=("Roboto",24), text_color="black", padx=10)
    probLabel.place(x=300, y=1)
    probLabel.configure(text='PROB') 
    classBox = ck.CTkLabel(window, height=40, width=120, corner_radius=10, font=("Roboto",24), text_color="white", fg_color="grey")
    classBox.place(x=10, y=41)
    classBox.configure(text='0') 
    counterBox = ck.CTkLabel(window, height=40, width=120,corner_radius=10,  font=("Roboto",24), text_color="white", fg_color="grey")
    counterBox.place(x=160, y=41)
    counterBox.configure(text='0') 
    probBox = ck.CTkLabel(window, height=40, width=120,corner_radius=10,  font=("Roboto",24), text_color="white", fg_color="grey")
    probBox.place(x=300, y=41)
    probBox.configure(text='0') 


    def reset_counter(): 
        global counter
        counter = 0 

    button = ck.CTkButton(window, text='RESET', command=reset_counter, height=40, width=120, font=("Arial", 20), text_color="white", fg_color="green")
    button.place(x=10, y=600)

    def preset_rep():
        #global counter
        pre = Toplevel()

        # Set the geometry of Tkinter Frame
        pre.geometry("500x250")
        pre.title("PRESET")
        pre.configure(bg='orange')
        
        label = ck.CTkLabel(pre,text="Enter the target REP",width=200,height=25,corner_radius=10,bg_color='white',text_color='black')
        label.place(x=50,y=100)

        global ent_get
        ent_get=IntVar()
        ent = ck.CTkEntry(pre,width=50,height=25,corner_radius=10,bg_color='orange',textvariable=ent_get)
        ent.place(x=300,y=100)
            
        def preset_submit():
            #global counter
            global set_count
            set_count = ent_get.get()
            pre.destroy()

            if counter==set_count:
                playsound('./sound.mp3')
            else:
                messagebox.showerror('Error','Print valid count !!')

            
        
        button1 = ck.CTkButton(pre, text='submit',corner_radius=10, command=preset_submit, height=25, width=50,  text_color="black")
        button1.place(x=300, y=180)
        pre.mainloop()


    button = ck.CTkButton(window, text='PRESET_REP', command=preset_rep, height=40, width=120, font=("Arial", 20), text_color="white", fg_color="blue")
    button.place(x=300, y=600)


    frame = tk.Frame(height=480, width=480)
    frame.place(x=10, y=90) 
    lmain = tk.Label(frame) 
    lmain.place(x=0, y=0) 

    mp_drawing = mp.solutions.drawing_utils
    mp_pose = mp.solutions.pose
    pose = mp_pose.Pose(min_tracking_confidence=0.5, min_detection_confidence=0.5) 
    

    with open(r'C:\Users\thami\Desktop\thamizh_backup\Study_Materials\Project\Project\deadlift.pkl', 'rb') as f: 
        model = pickle.load(f) 

    cap = cv2.VideoCapture(0)
    global current_stage
    global counter
    global bodylang_class
    global bodylang_prob
    current_stage = ''
    counter = 0 
    bodylang_prob = np.array([0,0]) 
    bodylang_class = '' 
    
    def detect(): 
        global current_stage
        global counter
        global bodylang_class
        global bodylang_prob 

        ret, frame = cap.read()
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) 
        results = pose.process(image)
        mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS, 
            mp_drawing.DrawingSpec(color=(106,13,173), thickness=4, circle_radius = 5), 
            mp_drawing.DrawingSpec(color=(255,102,0), thickness=5, circle_radius = 10)) 

        try: 
            row = np.array([[res.x, res.y, res.z, res.visibility] for res in results.pose_landmarks.landmark]).flatten().tolist()
            X = pd.DataFrame([row], columns = landmarks) 
            bodylang_prob = model.predict_proba(X)[0]
            bodylang_class = model.predict(X)[0] 

            if bodylang_class =="down" and bodylang_prob[bodylang_prob.argmax()] > 0.7: 
                current_stage = "down" 
            elif current_stage == "down" and bodylang_class == "up" and bodylang_prob[bodylang_prob.argmax()] > 0.7:
                current_stage = "up" 
                counter += 1 
            #global set_count    
            if counter==set_count:
                playsound('./sound.mp3')
            

        except Exception as e: 
            print(e) 

        img = image[:, :460, :] 
        imgarr = Image.fromarray(img) 
        imgtk = ImageTk.PhotoImage(imgarr) 
        lmain.imgtk = imgtk 
        lmain.configure(image=imgtk)
        lmain.after(10, detect)  

        counterBox.configure(text=counter) 
        probBox.configure(text=bodylang_prob[bodylang_prob.argmax()]) 
        classBox.configure(text=current_stage) 

    detect() 
    
    window.mainloop()
if __name__=='__main__':
    application()