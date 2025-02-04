from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class Developer:
    def __init__(self, root):
        self.root = root
        self.width= self.root.winfo_screenwidth()               
        self.height= self.root.winfo_screenheight()               
        self.root.geometry("%dx%d" % (self.width, self.height))
        self.root.title("Facial Recognition System for Attendance Maintenance")
    
        # Title
        title_lbl = Label(self.root, text="DEVELOPER", font=("times new roman", 35, "bold"), bg="white", fg="blue")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        # Background Image
        img_top = Image.open("images/dev.jpg")
        img_top = img_top.resize((1530, 800), Image.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=55, width=1530, height=720)

        # Main Frame
        main_frame = Frame(f_lbl, bd=2, bg="white")
        main_frame.place(x=1000, y=0, width=500, height=720)

        # Back Button Functionality
        def go_back():
            self.root.destroy()

        # Back Button
        back_btn_img = Image.open("images/R.png")
        back_btn_img = back_btn_img.resize((50, 40), Image.LANCZOS)
        self.back_btn_photo = ImageTk.PhotoImage(back_btn_img)
        back_btn = Button(self.root, image=self.back_btn_photo, command=go_back, bd=0, bg="white")
        back_btn.place(x=10, y=2)

        # Developer Image
        img_top1 = Image.open("images/WhatsApp Image 2024-04-21 at 21.31.18_d64e1bb8.jpg")
        img_top1 = img_top1.resize((200, 200), Image.LANCZOS)
        self.photoimg_top1 = ImageTk.PhotoImage(img_top1)

        f_lbl = Label(main_frame, image=self.photoimg_top1)
        f_lbl.place(x=300, y=0, width=200, height=200)

        # Developer Information
        dep_label = Label(main_frame, text="Developed By:", font=("times new roman", 15, "bold","underline"), bg="white")
        dep_label.place(x=10, y=5)

        # List of Developers
        developers = [
            "Ahmed Raza - B21110006009", "Dinesh Kumar - B21110006026",
            "Syed Zohaib Ahmed Qadri - B21110006142"
        ]

        y_offset = 30
        for dev in developers:
            dev_label = Label(main_frame, text=dev, font=("times new roman", 13), bg="white")
            dev_label.place(x=10, y=y_offset)
            y_offset += 22

        # Department Information
        dep_info_label = Label(main_frame, text="Department of Computer Science", font=("times new roman", 15, "bold","underline"), bg="white")
        dep_info_label.place(x=10, y=255)

        uni_label = Label(main_frame, text="University of Karachi", font=("times new roman", 13), bg="white")
        uni_label.place(x=10, y=280)

        location_label = Label(main_frame, text="Karachi, Sindh, Pakistan", font=("times new roman", 13), bg="white")
        location_label.place(x=10, y=305)

        # Image showcasing development process
        img2 = Image.open("images/KPIs-and-Agile-software-development-metrics-for-teams-1.jpg")
        img2 = img2.resize((500, 390), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl = Label(main_frame, image=self.photoimg2)
        f_lbl.place(x=0, y=330, width=500, height=390)

if __name__ == "__main__":
    root = Tk()
    obj = Developer(root)
    root.mainloop()