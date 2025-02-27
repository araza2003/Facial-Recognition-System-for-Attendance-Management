from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import os
from student import Student
from train import Train
from developer import Developer
from time import strftime 
from datetime import datetime
from face_recognition import Face_Recognition
from help import Help
from attendance import Attendance

class Face_Recognition_System:
    def __init__(self, root):
        self.root = root
        self.width= self.root.winfo_screenwidth()               
        self.height= self.root.winfo_screenheight()               
        self.root.geometry("%dx%d" % (self.width, self.height))
        self.root.title ("face Recognition System")

        # -------------------------------------------------------------------------------
        # -------------------------------- IMAGES ---------------------------------------
        # -------------------------------------------------------------------------------
        img = Image.open(r"images\face-recognition.png")
        img = img.resize((505,130))
        self.photoimg = ImageTk.PhotoImage(img)
        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=505, height=130)

        img1 = Image.open(r"images\smart-attendance.jpg")
        img1 = img1.resize((530,130))
        self.photoimg1 = ImageTk.PhotoImage(img1)
        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=505, y=0, width=530, height=130)

        img2 = Image.open(r"images\2-AI-invades-automobile-industry-in-2019.jpeg")
        img2 = img2.resize((505,130))
        self.photoimg2 = ImageTk.PhotoImage(img2)
        f_lbl = Label(self.root, image=self.photoimg2)
        f_lbl.place(x=1030, y=0, width=505, height=130)

        # -------------------------------------------------------------------------------
        # --------------------------BACKGROUND IMAGE-------------------------------------
        # -------------------------------------------------------------------------------
        img3 = Image.open(r"images\299208600_3255517044689127_958116927625989093_n (1).jpg")
        img3 = img3.resize((1530,710))
        self.photoimg3 = ImageTk.PhotoImage(img3)
        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=130, width=1530, height=730)

        # -------------------------------------------------------------------------------
        # --------------------------------- TITLE ---------------------------------------
        # -------------------------------------------------------------------------------
        title_lbl = Label (bg_img, text="Face Recognition System Software", font=("times new roman", 35, "bold"), bg="beige", fg="red")
        title_lbl.place(x=0, y=-2, width=1530, height=75)
        
        # --------------------------------- Time ----------------------------------------
        
        def time():
            string = strftime('%H:%M:%S %p')
            lbl.config(text = string)
            lbl.after(1000, time)
            
        lbl = Label(title_lbl, font= ('times new roman', 14, 'bold'), background='beige', foreground='blue')
        lbl.place(x=0,y=10,width=110,height=50)
        time()

        # -------------------------------------------------------------------------------
        # --------------------------BUTTONS (IMAGES) ------------------------------------
        # -------------------------------------------------------------------------------
        
        # STUDENT BUTTON
        img4 = Image.open(r"images\student-portal_1.jpg")
        img4 = img4.resize((220,220))
        self.photoimg4 = ImageTk.PhotoImage(img4)

        b1= Button (bg_img, image=self.photoimg4, cursor="hand2",command=self.student_details)
        b1.place(x=200, y=100, width=220, height=220)

        b1_1= Button (bg_img, text="Students Details", cursor="hand2",command=self.student_details, font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=200, y=300, width=220, height=40)
        
        # DETECT FACE BUTTON
        img5 = Image.open(r"images\face_detector1.jpg")
        img5 = img5.resize((220,220))
        self.photoimg5 = ImageTk.PhotoImage(img5)

        b1= Button (bg_img, image=self.photoimg5, cursor="hand2",command=self.face_recog)
        b1.place(x=500, y=100, width=220, height=220)

        b1_1= Button (bg_img, text="Face Detector", cursor="hand2",command=self.face_recog, font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=500, y=300, width=220, height=40)
        
        # ATTANDANCE BUTTON
        img6 = Image.open(r"images\report.jpg")
        img6 = img6.resize((220,220))
        self.photoimg6 = ImageTk.PhotoImage(img6)

        b1= Button (bg_img, image=self.photoimg6, cursor="hand2",command=self.attendance)
        b1.place(x=800, y=100, width=220, height=220)

        b1_1= Button (bg_img, text="Attandance", cursor="hand2",command=self.attendance, font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=800, y=300, width=220, height=40)

        # HELP BUTTON
        img7 = Image.open(r"images\help-desk-customer-care-team-icon-blue-square-button-isolated-reflected-abstract-illustration-89657179.jpg")
        img7 = img7.resize((220,220))
        self.photoimg7 = ImageTk.PhotoImage(img7)

        b1= Button (bg_img, image=self.photoimg7, cursor="hand2",command=self.help)
        b1.place(x=1100, y=100, width=220, height=220)

        b1_1= Button (bg_img, text="Help Desk", cursor="hand2",command=self.help, font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=1100, y=300, width=220, height=40)
        
        # TRAIN BUTTON
        img8 = Image.open(r"images\Train.jpg")
        img8 = img8.resize((220,220))
        self.photoimg8 = ImageTk.PhotoImage(img8)

        b1= Button (bg_img, image=self.photoimg8, cursor="hand2",command=self.train_data)
        b1.place(x=200, y=380, width=220, height=220)

        b1_1= Button (bg_img, text="Train Data", cursor="hand2",command=self.train_data, font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=200, y=580, width=220, height=40)
        
        # PHOTOS BUTTON
        img9 = Image.open(r"images\IMG_1183_augmented_reality_faces1.jpg")
        img9 = img9.resize((220,220))
        self.photoimg9 = ImageTk.PhotoImage(img9)

        b1= Button (bg_img, image=self.photoimg9, cursor="hand2",command=self.open_img)
        b1.place(x=500, y=380, width=220, height=220)

        b1_1= Button (bg_img, text="Photos", cursor="hand2",command=self.open_img, font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=500, y=580, width=220, height=40)
        
        # DEVELOPER BUTTON
        img10 = Image.open(r"images\Team-Management-Software-Development.jpg")
        img10 = img10.resize((220,220))
        self.photoimg10 = ImageTk.PhotoImage(img10)

        b1= Button (bg_img, image=self.photoimg10, cursor="hand2",command=self.developer)
        b1.place(x=800, y=380, width=220, height=220)

        b1_1= Button (bg_img, text="Developer Info", cursor="hand2",command=self.developer, font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=800, y=580, width=220, height=40)

        # EXIT BUTTON
        img11 = Image.open(r"images\OIP.jpeg")
        img11 = img11.resize((220,220))
        self.photoimg11 = ImageTk.PhotoImage(img11)

        b1= Button (bg_img, image=self.photoimg11, cursor="hand2",command=self.iExit)
        b1.place(x=1100, y=380, width=220, height=220)

        b1_1= Button (bg_img, text="Log out", cursor="hand2",command=self.iExit, font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=1100, y=580, width=220, height=40)

    def open_img(self):
        os.startfile("data")

    def iExit(self):
        self.iExit=messagebox.askyesno("Face Recognition","Do you want Log out?",parent  = self.root)
        if self.iExit > 0:
            self.root.destroy()
        else:
            return
            
            


        # ====================== Function Buttons ============================
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)


    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)
        
    def face_recog(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)
        
    def developer(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window)
        
    def help(self):
        self.new_window=Toplevel(self.root)
        self.app=Help(self.new_window)

    def attendance(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)

        

if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()
    