from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import random
from time import strftime 
from datetime import datetime
import time
import datetime 
import mysql.connector
from main import Face_Recognition_System
import os

# Get the path of the current script
script_path = os.path.dirname(os.path.abspath(__file__))

def main():
    win = Tk()
    app = Login_window(win)
    win.mainloop()


class Login_window:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.width= self.root.winfo_screenwidth()               
        self.height= self.root.winfo_screenheight()               
        self.root.geometry("%dx%d" % (self.width, self.height))

        img10 = Image.open(os.path.join(script_path,r"images\Image.jpg"))
        img10 = img10.resize((self.width,self.height), Image.LANCZOS)  
        self.photoimage10 = ImageTk.PhotoImage(img10)
        bg_lbl1 = Label(self.root,image=self.photoimage10)
        bg_lbl1.place(x=0, y=0, width =self.width, height = self.height)  

        title= Label(self.root, text="FACIAL RECOGNITION ATTENDANCE MANAGEMENT SYSTEM", font=("times new roman", 20, "bold"), fg="white", bg="black")
        title.place(x=0, y=0,width=1550,height=45)
        
        frame = Frame(self.root,bg = 'black')
        frame.place(x=570, y=200, width=340, height=430) 
        
        # Exit Button Functionality
        def exit():
            self.root.destroy()

        # Back Button
        exit_btn_img = Image.open(r"images\exit.jpg")
        exit_btn_img = exit_btn_img.resize((50, 40), Image.LANCZOS)
        self.exit_btn_photo = ImageTk.PhotoImage(exit_btn_img)
        exit_btn = Button(self.root, image=self.exit_btn_photo, command=exit, bd=0, bg="black")
        exit_btn.place(x=10, y=2)
        
        register_lbl = Label(frame,text="Register Here",font=("times new roman",20,"bold"),fg = "steel blue",bg='black')
        register_lbl.place(x = 20,y = 20)
        
        img1 = Image.open(os.path.join(script_path,r"images\LoginIconAppl.png"))
        img1 = img1.resize((90,90), Image.LANCZOS)  
        self.photoimage1 = ImageTk.PhotoImage(img1)
        lblimg1 = Label(image=self.photoimage1,bg="black",borderwidth=0)
        lblimg1.place(x=690, y=230, width=90, height=90)

        # Label
        username = Label(frame, text="Id", font=("times new roman", 15, "bold"), fg="white", bg="black")
        username.place(x=70, y=155)

        self.txtuser = ttk.Entry(frame, font=("times new roman", 15, "bold"))
        self.txtuser.place(x=40, y=180, width=270)

        password = Label(frame, text="Password", font=("times new roman", 15, "bold"), fg="white", bg="black")
        password.place(x=70, y=225)

        self.txtpass = ttk.Entry(frame, font=("times new roman", 15, "bold"))
        self.txtpass.place(x=40, y=250, width=270)


        # ------------Icon Images-----------

        img2 = Image.open(os.path.join(script_path,r"images\LoginIconAppl.png"))
        img2 = img2.resize((25, 25), Image.LANCZOS)  
        self.photoimage2 = ImageTk.PhotoImage(img2)
        lblimage1 = Label(image=self.photoimage2, bg="black", borderwidth=0)
        lblimage1.place(x=610, y=348, width=25, height=25)
        
        
        img3 = Image.open(os.path.join(script_path,r"images\lock-512.png"))
        img3 = img3.resize((25, 25), Image.LANCZOS)  
        self.photoimage3 = ImageTk.PhotoImage(img3)
        lblimage1 = Label(image=self.photoimage3, bg="black", borderwidth=0)
        lblimage1.place(x=610, y=420, width=25, height=25)


        # Login Button
        loginbtn = Button(frame, command=self.login,text='Login', font= ("times new roman", 15, "bold"), bd=3, relief=RIDGE,fg='white',bg="Black", activeforeground="white", activebackground='red')
        loginbtn.place(x = 100,y=310,width= 140, height=35)
        

        # Register Button
        registerbtn = Button(frame, text='New User Register',command=self.register_window, font= ("times new roman", 10, "bold"),borderwidth=0,relief=RIDGE,fg='white',bg="black", activeforeground="white", activebackground='red')
        registerbtn.place(x = 35,y=350,width= 110)

        # Forget Button
        forgetbtn = Button(frame, text='Forget Password',command=self.forgot_password_window, font= ("times new roman", 10, "bold"),borderwidth=0,relief=RIDGE,fg='white',bg="black", activeforeground="white", activebackground='red')
        forgetbtn.place(x = 35,y=370,width= 95)


    def register_window(self):
        self.new_window = Toplevel(self.root)
        self.app = Register(self.new_window)
        
        
    def login(self):
        if self.txtuser.get()== "" or self.txtpass.get()=="":
            messagebox.showerror("Error","all fields required")
        
        else:
            conn = mysql.connector.connect(host = "localhost",user = "root",password = "Ar12345#",database = "login_Data")
            my_cursor = conn.cursor()
            my_cursor.execute("select * from register where Id = %s and Password = %s", (
                self.txtuser.get(),self.txtpass.get()
            ))
            
            row = my_cursor.fetchone()
            if row == None:
                messagebox.showerror("Error","Invalid Id and password")
            else:
                open_main = messagebox.askyesno("yesNo","Access only admin")
                if open_main == 1:
                    # messagebox.showinfo(title="WELCOME! TO THE PORTAL.")
                    self.new_window=Toplevel(self.root)
                    self.app=Face_Recognition_System(self.new_window)
                else:
                    if open_main == 0:
                        return
            conn.commit()
            conn.close()
    #---------------------Reset Password-------------------------------
    def reset_pass(self):
        if self.combo_security_Q.get()=="Select":
            messagebox.showerror("Error","Select the Security Question",parent=self.root2)
        elif self.S_Answer_entry.get()=="":
            messagebox.showerror("Error","Please enter the answer",parent=self.root2)
        elif self.S_Answer_new_password.get()=="":
            messagebox.showerror("Error","Please enter the new password",parent=self.root2)
        else:
            conn = mysql.connector.connect(host = "localhost",user = "root",password = "Ar12345#",database = "login_Data")
            my_cursor = conn.cursor()
            query=("select * from register where Id=%s and SecurityQ=%s and SecurityA=%s")
            value=(self.txtuser.get(),self.combo_security_Q.get(),self.S_Answer_entry.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row == None:
                messagebox.showerror("Error","Please enter the correct Answer",parent=self.root2)
            else:
                query=("update register set Password=%s where Id=%s")
                value=(self.S_Answer_new_password.get(),self.txtuser.get())
                my_cursor.execute(query,value)

                query=("update admin set AdminPass=%s where AdminId=%s")
                value=(self.S_Answer_new_password.get(),self.txtuser.get())
                my_cursor.execute(query,value)


                conn.commit()
                conn.close()
                messagebox.showinfo("Info","Your password has been reset, Please login new password",parent=self.root2)

    #---------------------- Forget Password Window-------------------------
    def forgot_password_window(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error","Please enter the Email address to reset password")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="Ar12345#",database="login_Data")
            my_cursor=conn.cursor()
            query=("select * from register where Id=%s")
            value=(self.txtuser.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            #print(row)

            if row==None:
                messagebox.showerror("Error","Please enter the valid Id")
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forget Password")
                self.root2.geometry("340x450+610+170")
            

                l=Label(self.root2,text="Forget Password",font=("times new roman",20,"bold"),fg="red")
                l.place(x=50,y=10)

                S_Question = Label(self.root2,text="Select Security Question",font=("times new roman",15,'bold'))
                S_Question.place(x = 50,y = 80)
                
                self.combo_security_Q = ttk.Combobox(self.root2,font=("times new roman",14,'bold'),state='readonly')
                self.combo_security_Q['values'] = ('Select',"Your Birth Place","Your Mother's Name",'Your Pet Name')
                self.combo_security_Q.place(x = 50,y= 110,width = 250)
                self.combo_security_Q.current(0)
                
                S_Answer = Label(self.root2,text="Security Answer",font=("times new roman",15,'bold'))
                S_Answer.place(x = 50,y = 150)
                
                self.S_Answer_entry = ttk.Entry(self.root2,font=("times new roman",14,'bold'))
                self.S_Answer_entry.place(x = 50, y = 180, width = 250)

                new_password = Label(self.root2,text="New Password",font=("times new roman",15,'bold'))
                new_password.place(x = 50,y = 220)
                
                self.S_Answer_new_password = ttk.Entry(self.root2,font=("times new roman",14,'bold'))
                self.S_Answer_new_password.place(x = 50, y = 250, width = 250)

                btn=Button(self.root2,text="Reset",command=self.reset_pass,font=("times new roman",14,'bold'),fg="white",bg="light steel blue")
                btn.place(x=135,y=290)






class Register:
    def __init__(self,root):
        self.root = root
        self.root.title("Register")
        self.width= self.root.winfo_screenwidth()               
        self.height= self.root.winfo_screenheight()               
        self.root.geometry("%dx%d" % (self.width, self.height))
        
        # Variables
        
        self.var_fname = StringVar()
        self.var_lname = StringVar()
        self.var_contact = StringVar()
        self.var_Id = StringVar()
        self.var_securityQ = StringVar()
        self.var_SecurityA = StringVar()
        self.var_pass = StringVar()
        self.var_confpass = StringVar()
        self.var_Admin_Id = StringVar()
        self.var_Admin_Pass = StringVar()
        
        
        img10 = Image.open(os.path.join(script_path,r"images\Image.jpg"))
        img10 = img10.resize((self.width,self.height), Image.LANCZOS)  
        self.photoimage10 = ImageTk.PhotoImage(img10)
        bg_lbl1 = Label(self.root,image=self.photoimage10)
        bg_lbl1.place(x=0, y=0, width =self.width, height = self.height)  
        
        # Main Frame
        
        frame = Frame(self.root,bg='black')
        frame.place(x=340,y = 120,width=900,height=550)
        
        # Back Button Functionality
        def go_back():
            self.root.destroy()

        # Back Button
        back_btn_img = Image.open(r"images\R.png")
        back_btn_img = back_btn_img.resize((50, 40), Image.LANCZOS)
        self.back_btn_photo = ImageTk.PhotoImage(back_btn_img)
        back_btn = Button(self.root, image=self.back_btn_photo, command=go_back, bd=0, bg="Steel blue")
        back_btn.place(x=10, y=2)
        
        register_lbl = Label(frame,text="Register Here",font=("times new roman",20,"bold"),fg = "steel blue",bg='black')
        register_lbl.place(x = 20,y = 20)


        # label and entry
        
        # 1st row
        fname = Label(frame,text="First Name",font=("times new roman",15,'bold'),fg = 'white',bg = 'black')
        fname.place(x = 50,y = 80)
        
        fname_entry = ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",14,'bold'))
        fname_entry.place(x = 50, y = 110, width = 250)
        
        lname = Label(frame,text="Last Name",font=("times new roman",15,'bold'),fg = 'white',bg = 'black')
        lname.place(x = 500,y = 80)
        
        lname_entry = ttk.Entry(frame,textvariable=self.var_lname,font=("times new roman",14,'bold'))
        lname_entry.place(x = 500, y = 110, width = 250)
        
        
        # 2nd row
        Cnumber = Label(frame,text="Contact No",font=("times new roman",15,'bold'),fg = 'white',bg = 'black')
        Cnumber.place(x = 50,y = 150)
        
        Cnumber_entry = ttk.Entry(frame,textvariable=self.var_contact,font=("times new roman",14,'bold'))
        Cnumber_entry.place(x = 50, y = 180, width = 250)
        
        Id = Label(frame,text="Id",font=("times new roman",15,'bold'),fg = 'white',bg = 'black')
        Id.place(x = 500,y = 150)
        
        Id_entry = ttk.Entry(frame,textvariable=self.var_Id,font=("times new roman",14,'bold'))
        Id_entry.place(x = 500, y = 180, width = 250)
        
        
        # 3rd row
        S_Question = Label(frame,text="Select Security Question",font=("times new roman",15,'bold'),fg = 'white',bg = 'black')
        S_Question.place(x = 50,y = 220)
         
        self.combo_security_Q = ttk.Combobox(frame,textvariable=self.var_securityQ,font=("times new roman",14,'bold'),state='readonly')
        self.combo_security_Q['values'] = ('Select',"Your Birth Place","Your Mother's Name",'Your Pet Name')
        self.combo_security_Q.place(x = 50,y= 250,width = 250)
        self.combo_security_Q.current(0)
        
        S_Answer = Label(frame,text="Security Answer",font=("times new roman",15,'bold'),fg = 'white',bg = 'black')
        S_Answer.place(x = 500,y = 220)
        
        self.S_Answer_entry = ttk.Entry(frame,textvariable=self.var_SecurityA,font=("times new roman",14,'bold'))
        self.S_Answer_entry.place(x = 500, y = 250, width = 250)
        
        
        # 4th row
        Password = Label(frame,text="Password",font=("times new roman",15,'bold'),fg = 'white',bg = 'black')
        Password.place(x = 50,y = 290)
        
        self.Password_entry = ttk.Entry(frame,textvariable=self.var_pass,font=("times new roman",14,'bold'))
        self.Password_entry.place(x = 50, y = 320, width = 250)
        
        Confirm_pass = Label(frame,text="Confirm Password",font=("times new roman",15,'bold'),fg = 'white',bg = 'black')
        Confirm_pass.place(x = 500,y = 290)
        
        Confirm_pass_entry = ttk.Entry(frame,textvariable=self.var_confpass,font=("times new roman",14,'bold'))
        Confirm_pass_entry.place(x = 500, y = 320, width = 250)

        # 5th row
        Admin_Id = Label(frame,text="Admin Id",font=("times new roman",15,'bold'),fg = 'white',bg = 'black')
        Admin_Id.place(x = 50,y = 360)
        
        Admin_entry = ttk.Entry(frame,textvariable=self.var_Admin_Id,font=("times new roman",14,'bold'))
        Admin_entry.place(x = 50, y = 390, width = 250)
        
        Admin_pass = Label(frame,text="Admin Password",font=("times new roman",15,'bold'),fg = 'white',bg = 'black')
        Admin_pass.place(x = 500,y = 360)
        
        Admin_pass_entry = ttk.Entry(frame,textvariable=self.var_Admin_Pass,font=("times new roman",14,'bold'))
        Admin_pass_entry.place(x = 500, y = 390, width = 250)

        
        # Check Botton
        
        #self.var_check = IntVar()
        #checkbtn = Checkbutton(frame,variable=self.var_check,text='I Agree The Terms & Conditions',font=("times new roman",12,'bold'),fg = 'white',bg = 'black',onvalue=1,offvalue=0)
        #checkbtn.place(x = 50, y = 430)
        
        # Buttons
        registerbtn = Button(frame,command=self.register_data,text='Register', font= ("times new roman", 15, "bold"),border=2, relief=RIDGE,fg='black',bg="light steel blue", activeforeground="black", activebackground='aqua')
        registerbtn.place(x = 50,y = 470,width=200)
        
        #loginbtn = Button(frame,text='Login', font= ("times new roman", 15, "bold"),border=2, relief=RIDGE,fg='black',bg="light steel blue", activeforeground="black", activebackground='aqua')
        #loginbtn.place(x = 500,y = 470,width=200)
        

    
    # Function
    def register_data(self):
        if self.var_fname.get() == "" or self.var_Id.get() == "" or self.var_securityQ.get() == "Select" or self.var_Id.get() == "":
            messagebox.showerror("Error","All fields are required",parent = self.root)
        
        elif (self.var_pass.get() != self.var_confpass.get()):
            messagebox.showerror("Error","Password & Confirm Password must be same",parent = self.root)
        
        elif self.var_Admin_Id.get() == "" or self.var_Admin_Pass.get() == "":
            messagebox.showerror("Error","Admin Id & Admin Password is must",parent = self.root)
        
        #elif self.var_check.get() == 0:
           # messagebox.showerror("Error","Please agree our terms and conditions",parent = self.root)
        else:
            # admin_conn = mysql.connector.connect(host = "localhost",user = "root",password = "Narwani12345",database = "Login_Data")
            with mysql.connector.connect(host="localhost", user="root", password="Ar12345#", database="login_Data") as conn:
                    
                admin_cursor = conn.cursor()
                admin_cursor.execute("select * from admin where AdminId = %s and AdminPass = %s", (
                    self.var_Admin_Id.get(),
                    self.var_Admin_Pass.get(),
                ))
                row1 = admin_cursor.fetchone()
                if row1 == None:
                    messagebox.showerror("Error","Invalid Admin Id and password",parent = self.root)
                    return
                else:
                    # conn = mysql.connector.connect(host = "localhost",user = "root",password = "Narwani12345",database = "Login_Data")
                    my_cursor = conn.cursor()
                    query = ("Select * from register where Id = %s")
                    value = (self.var_Id.get(),)
                    my_cursor.execute(query,value)
                    row = my_cursor.fetchone()
                    if row != None:
                        messagebox.showerror("Error","User already exist, please try another Id",parent = self.root)
                        return
                    else:
                        my_cursor.execute("insert into admin values(%s,%s)",(
                            self.var_Id.get(),
                            self.var_pass.get()
                        ))
                        my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",(
                            self.var_Id.get(),
                            self.var_fname.get(),
                            self.var_lname.get(),
                            self.var_contact.get(),
                            self.var_securityQ.get(),
                            self.var_SecurityA.get(),
                            self.var_pass.get()
                        ))
                    
                        conn.commit()
                        conn.close()
                        messagebox.showinfo("Sucess","Register Sucessfull",parent = self.root)
                        self.root.destroy()
                
if __name__ == "__main__":
    main()


