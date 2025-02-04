from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class Help:
    def __init__(self,root):
        self.root=root
        self.width= self.root.winfo_screenwidth()               
        self.height= self.root.winfo_screenheight()               
        self.root.geometry("%dx%d" % (self.width, self.height))
        self.root.title("Face recognition system")

        title_lbl=Label(self.root,text="HELP DESK",font=("times new roman",35,"bold"),bg="white",fg="blue")
        title_lbl.place(x=0,y=0,width=1530,height=45)
        
        # Back Button Functionality
        def go_back():
            self.root.destroy()

        # Back Button
        back_btn_img = Image.open(r"images\R.png")
        back_btn_img = back_btn_img.resize((50, 40), Image.LANCZOS)
        self.back_btn_photo = ImageTk.PhotoImage(back_btn_img)
        back_btn = Button(self.root, image=self.back_btn_photo, command=go_back, bd=0, bg="white")
        back_btn.place(x=10, y=2)
        

        img_top=Image.open(r"images\1_5TRuG7tG0KrZJXKoFtHlSg.jpeg")
        img_top=img_top.resize((1530,800),Image.LANCZOS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=55,width=1530,height=800)

        dep_label=Label(f_lbl,text="bscsaiproject@gmail.com",font=("times new roman",13,"bold"),bg="black",fg="white")
        dep_label.place(x=620,y=220)




if __name__ == "__main__":
    root=Tk()
    obj=Help(root)
    root.mainloop()