from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class Student:
    def __init__(self, root):
        self.root = root
        self.width= self.root.winfo_screenwidth()               
        self.height= self.root.winfo_screenheight()               
        self.root.geometry("%dx%d" % (self.width, self.height))
        self.root.title("face Recognition System")
         
        #=====================varibles=================
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar() 
        self.var_semester=StringVar()
        self.var_std_id=StringVar() 
        # self.var_std_id=int() 
        # self.var_std_id="" 
        self.var_std_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()
        self.var_radio1 = StringVar()     
        
        self.Db_pass = 'Ar12345#'

        # -------------------------------------------------------------------------------
        # -------------------------------- IMAGES ---------------------------------------
        # -------------------------------------------------------------------------------
        img = Image.open(r"images\Screenshot 2024-04-18 171755.png")
        img = img.resize((500,130))
        self.photoimg = ImageTk.PhotoImage(img)
        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=500, height=100)

        img1 = Image.open(r"images\smart-attendance.jpg")
        img1 = img1.resize((500,130))
        self.photoimg1 = ImageTk.PhotoImage(img1)
        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=500, y=0, width=500, height=100)

        img2 = Image.open(r"images\iStock-182059956_18390_t12.jpg")
        img2 = img2.resize((580,130))
        self.photoimg2 = ImageTk.PhotoImage(img2)
        f_lbl = Label(self.root, image=self.photoimg2)
        f_lbl.place(x=1000, y=0, width=580, height=100)

        # -------------------------------------------------------------------------------
        # --------------------------BACKGROUND IMAGE-------------------------------------
        # -------------------------------------------------------------------------------
        img3 = Image.open(r"images\wp2551980.jpg")
        img3 = img3.resize((1530,710))
        self.photoimg3 = ImageTk.PhotoImage(img3)
        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=130, width=1530, height=700)

        # -------------------------------------------------------------------------------
        # --------------------------------- TITLE ---------------------------------------
        # -------------------------------------------------------------------------------
        title_lbl = Label(self.root, text="STUDENT MANAGEMENT SYSTEM ", font=("times new roman", 35, "bold"), bg="white", fg="green")
        title_lbl.place(x=0, y=105, width=1530, height=45)
        
        # Back Button Functionality
        def go_back():
            self.root.destroy()

        # Back Button
        back_btn_img = Image.open(r"images\R.png")
        back_btn_img = back_btn_img.resize((50, 40), Image.LANCZOS)
        self.back_btn_photo = ImageTk.PhotoImage(back_btn_img)
        back_btn = Button(self.root, image=self.back_btn_photo, command=go_back, bd=0, bg="white")
        back_btn.place(x=10, y=108)

        main_frame = Frame(bg_img, bd=2, bg="white")
        main_frame.place(x=10, y=55, width=1510, height=580)

        # -------------------------------------------------------------------------------
        # ----------------------------- LEFT LABEL FRAME --------------------------------
        # -------------------------------------------------------------------------------
        Left_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Details", font=("times new roman", 13, "bold"))
        Left_frame.place(x=10, y=0, width=750, height=560)

        img_Left = Image.open(r"images\AdobeStock_303989091.jpeg")
        img_Left = img_Left.resize((730,130)) 
        self.photoimg_left = ImageTk.PhotoImage(img_Left)
        f_lbl = Label(Left_frame, image=self.photoimg_left)
        f_lbl.place(x=5, y=0, width=730, height=120) 

        # ----------------------------- CURRENT COURSE --------------------------------
        # -------------------------------------------------------------------------------
        current_course_frame = LabelFrame(Left_frame, bd=2, bg="white", relief=RIDGE, text="Current Course Informaton",font=("times new roman", 13, "bold"))
        current_course_frame.place(x=5, y=120, width=730, height=90)

        # ----------------------------- DEPARTMENT --------------------------------
        dep_label = Label(current_course_frame, text="Department", font=("times new roman", 11, "bold"), bg = "white")
        dep_label.grid(row = 0, column = 0, padx = 10, sticky = W)

        dep_combo = ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("times new roman", 11, "bold"), state = "readonly", width = 15)
        dep_combo["values"] = ("Select Department", "Computer" ,"Civil", "Mechanical",'Pharmacy','Microbiology','School Of Law')
        dep_combo.current(0)
        dep_combo.grid(row = 0,column = 1, padx = 2, pady = 5, sticky = W)

        # ----------------------------- COURSE --------------------------------
        course_label = Label(current_course_frame, text="Course", font=("times new roman", 11, "bold"), bg = "white")
        course_label.grid(row = 0, column = 2, padx = 10, sticky = W)

        course_combo = ttk.Combobox(current_course_frame,textvariable=self.var_course, font=("times new roman", 11, "bold"), state = "readonly", width = 15)
        course_combo["values"] = ("Select Course", "CS", "SE" ,"AI", "CYBER SECURITY",'NETWORKING')
        course_combo.current(0)
        course_combo.grid(row = 0,column = 3, padx = 2, pady = 5, sticky = W)

        # ----------------------------- YEAR ------------------------------
        year_label = Label(current_course_frame, text="Year", font=("times new roman", 11, "bold"), bg = "white")
        year_label.grid(row = 1, column = 0, padx = 10, sticky = W)

        year_entry = ttk.Entry(current_course_frame,textvariable=self.var_year, width = 20, font=("times new roman", 11, "bold"))
        year_entry.grid(row = 1, column = 1, padx =2, pady =5, sticky = W)

        # ----------------------------- SEMESTER ------------------------------
        semester_label = Label(current_course_frame, text = "Semester", font=("times new roman", 11, "bold"), bg = "white")
        semester_label.grid(row = 1, column = 2, padx = 10, sticky = W)

        semester_combo = ttk.Combobox(current_course_frame,textvariable=self.var_semester,font=("times new roman", 11, "bold"), state = "readonly", width = 15)
        semester_combo["values"] = ("Select Semester", "Semester-1", "Semester-2", "Semester-3", "Semester-4", "Semester-5", "Semester-6", "Semester-7", "Semester-8")
        semester_combo.current(0)
        semester_combo.grid(row = 1,column = 3, padx = 2, pady = 5, sticky = W)

        # ----------------------- CLASS STUDENT INFORMATION -----------------------------
        # -------------------------------------------------------------------------------
        class_student_frame = LabelFrame(Left_frame, bd=2, bg="white", relief=RIDGE, text="Class Student Informaton",font=("times new roman", 13, "bold"))
        class_student_frame.place(x=5, y=220, width=730, height=300)

        # ------------------------------- STUDENT ID ------------------------------------
        studentId_label = Label(class_student_frame, text = "StudentID:", font=("times new roman", 11, "bold"), bg = "white")
        studentId_label.grid(row = 0, column = 0, padx = 5, sticky = W)

        studentID_entry = ttk.Entry(class_student_frame,textvariable=self.var_std_id, width = 20, font=("times new roman", 11, "bold"))
        studentID_entry.grid(row = 0, column = 1, padx =5, pady =5, sticky = W)
        # ------------------------------- STUDENT NAME ----------------------------------
        studentName_label = Label(class_student_frame, text = "Student Name:", font=("times new roman", 11, "bold"), bg = "white")
        studentName_label.grid(row = 0, column = 2, padx = 5, sticky = W)

        studentName_entry = ttk.Entry(class_student_frame,textvariable=self.var_std_name,width = 20, font=("times new roman", 11, "bold"))
        studentName_entry.grid(row = 0, column = 3, padx = 5, pady =5, sticky = W)

        # ------------------------------- CLASS DIVISION --------------------------------
        class_div_label = Label(class_student_frame, text = "Class Division:", font=("times new roman", 11, "bold"), bg = "white")
        class_div_label.grid(row = 1, column = 0, padx = 5, sticky = W)
        
        div_combo = ttk.Combobox(class_student_frame,textvariable=self.var_div, font=("times new roman", 11, "bold"), state = "readonly", width = 13)
        div_combo["values"] = ("A", "B", "C" )
        div_combo.current(0)
        div_combo.grid(row = 1,column = 1, padx = 5, pady = 5, sticky = W)
        
        

         # ---------------------------------- ROLL NO ----------------------------------
        roll_no_label = Label(class_student_frame, text = "Roll No:", font=("times new roman", 11, "bold"), bg = "white")
        roll_no_label.grid(row = 1, column = 2, padx =5, sticky = W)

        roll_no_entry = ttk.Entry(class_student_frame, textvariable=self.var_roll,width = 20, font=("times new roman", 11, "bold"))
        roll_no_entry.grid(row = 1, column = 3, padx = 5, pady = 5, sticky = W)

        # --------------------------------- GENDER --------------------------------------
        gender_label = Label(class_student_frame, text = "Gender:", font=("times new roman", 11, "bold"), bg = "white")
        gender_label.grid(row = 2, column = 0, padx = 5, sticky = W)
        
        gender_combo = ttk.Combobox(class_student_frame,textvariable=self.var_gender, font=("times new roman", 11, "bold"), state = "readonly", width = 13)
        gender_combo["values"] = ("Male", "Female", "Other" )
        gender_combo.current(0)
        gender_combo.grid(row = 2,column = 1, padx = 2, pady = 5, sticky = W)
        

         # ------------------------------------ DOB ------------------------------------
        dob_label = Label(class_student_frame, text = "DOB:", font=("times new roman", 11, "bold"), bg = "white")
        dob_label.grid(row = 2, column = 2, padx = 5, sticky = W)

        dob_entry = ttk.Entry(class_student_frame,textvariable=self.var_dob,width = 20, font=("times new roman", 11, "bold"))
        dob_entry.grid(row = 2, column = 3, padx = 5, pady = 5, sticky = W)

        # ----------------------------------- EMAIL ------------------------------------
        email_label = Label(class_student_frame, text = "Email:", font=("times new roman", 11, "bold"), bg = "white")
        email_label.grid(row = 3, column = 0, padx =5, sticky = W)

        email_entry = ttk.Entry(class_student_frame, textvariable=self.var_email,width = 20, font=("times new roman", 11, "bold"))
        email_entry.grid(row = 3, column = 1, padx = 5, pady = 5, sticky = W)

        # --------------------------------- PHONE NO --------------------------------------
        phone_label = Label(class_student_frame, text = "Phone No:", font=("times new roman", 11, "bold"), bg = "white")
        phone_label.grid(row = 3, column = 2, padx = 5, sticky = W)

        phone_entry = ttk.Entry(class_student_frame, textvariable=self.var_phone,width = 20, font=("times new roman", 11, "bold"))
        phone_entry.grid(row = 3, column = 3, padx = 5, pady = 5, sticky = W)

        # ----------------------------------- ADDRESS ------------------------------------
        address_label = Label(class_student_frame, text = "Address", font=("times new roman", 11, "bold"), bg = "white")
        address_label.grid(row = 4, column = 0, padx =5, sticky = W)

        address_entry = ttk.Entry(class_student_frame,textvariable=self.var_address,width = 20, font=("times new roman", 11, "bold"))
        address_entry.grid(row = 4, column = 1, padx = 5, pady = 5, sticky = W)

        # --------------------------------- Teacher --------------------------------------
        teacher_label = Label(class_student_frame, text = "Teacher:", font=("times new roman", 11, "bold"), bg = "white")
        teacher_label.grid(row = 4, column = 2, padx = 5, sticky = W)

        teacher_entry = ttk.Entry(class_student_frame,textvariable=self.var_teacher,width = 20, font=("times new roman", 11, "bold"))
        teacher_entry.grid(row = 4, column = 3, padx = 5, pady = 5, sticky = W)

        # -------------------------------------------------------------------------------
        # -------------------------------- RADIO BUTTONS --------------------------------
        # -------------------------------------------------------------------------------

        self.var_radio1=StringVar()
        radiobtn1 = ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text = "Take photo sample",  value = "yes")
        radiobtn1.grid(row = 6, column = 0)
       
        radiobtn2 = ttk.Radiobutton(class_student_frame,variable=self.var_radio1, text = "NO photo sample",  value = "no")
        radiobtn2.grid(row = 6, column = 1)

        # ------------------------------ BUTTON FRAME -----------------------------------
        btn_frame = Frame(class_student_frame, bd =2, relief = RIDGE)
        btn_frame.place(x=0, y=200, width = 750, height = 40)

        save_btn = Button (btn_frame, text = "Save",command=self.add_data,width = 17, font=("times new roman", 11, "bold"), bg = "blue", fg = "white")
        save_btn.grid(row = 0, column = 0) 

        update_btn = Button (btn_frame, text = "Update",command=self.update_data,width = 20, font=("times new roman", 11, "bold"), bg = "blue", fg = "white")
        update_btn.grid(row = 0, column = 1) 

        delete_btn = Button (btn_frame, text = "Delete",command=self.delete_data,width = 20, font=("times new roman", 11, "bold"), bg = "blue", fg = "white")
        delete_btn.grid(row = 0, column = 2) 

        reset_btn = Button (btn_frame, text = "Reset",command=self.reset_data,width = 20, font=("times new roman", 11, "bold"), bg = "blue", fg = "white")
        reset_btn.grid(row = 0, column = 3)     

        btn_frame1 = Frame(class_student_frame, bd =2, relief = RIDGE)
        btn_frame1.place(x=0, y=240, width = 750, height = 40)
        
        #take_photo_btn = Button (btn_frame,command=self.generate_dataset,text = "Take Photo Sample",width = 17, font=("times new roman", 11, "bold"), bg = "blue", fg = "white")
        #take_photo_btn.grid(row = 0, column = 4) 
 
        take_photo_btn = Button (btn_frame1,command=self.generate_dataset, text = "Take Photo Sample",width = 40, font=("times new roman", 11, "bold"), bg = "blue", fg = "white")
        take_photo_btn.grid(row = 0, column = 0) 

        # update_photo_btn = Button (btn_frame1, text = "Update Phtoto Sample",width = 40, font=("times new roman", 11, "bold"), bg = "blue", fg = "white")
        # update_photo_btn.grid(row = 0, column = 1)  

        # -------------------------------------------------------------------------------
        # ----------------------------- RIGHT LABEL FRAME --------------------------------
        # -------------------------------------------------------------------------------
        Right_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Details",font=("times new roman", 12, "bold"))
        Right_frame.place(x=750, y=10, width=750, height=580)

        img_Right = Image.open(r"images\student-portal_1.jpg")
        img_Right = img_Right.resize((600,130)) 
        self.photoimg_Right = ImageTk.PhotoImage(img_Right)
        f_lbl = Label(Right_frame, image=self.photoimg_Right)
        f_lbl.place(x=5, y=0, width=730, height=200) 




# ======================= Search System =======================


        #Search_frame = LabelFrame(Right_frame, bd=2, bg="white", relief=RIDGE, text="Search System",font=("times new roman", 13, "bold"))
        #Search_frame.place(x=5, y=125, width=730, height=60)

        # search_label = Label(Search_frame, text = "Search By:", font=("times new roman", 13, "bold"), bg = "red",fg="white")
        # search_label.grid(row = 0, column = 0, padx = 5, pady=3,sticky = W)


        # search_combo = ttk.Combobox(Search_frame, font=("times new roman", 11, "bold"), state = "readonly", width = 10)
        # search_combo["values"] = ("Select", "Roll_No", "Phone_No")
        # search_combo.current(0)
        # search_combo.grid(row = 0,column = 1, padx = 2, pady = 5, sticky = W)    


        # search_entry = ttk.Entry(Search_frame, width = 15, font=("times new roman", 11, "bold"))
        # search_entry.grid(row = 0, column = 2, padx = 5, pady = 5, sticky = W)


        # search_btn = Button(Search_frame, text="Search", width=12, font=("times new roman", 9, "bold"), bg="blue", fg="white")

        # search_btn.grid(row = 0, column = 3,padx = 4) 


        # showAll_btn = Button (Search_frame, text = "Show All",width = 12, font=("times new roman", 9, "bold"), bg = "blue", fg = "white")
        # showAll_btn.grid(row = 0, column = 4,padx = 4)

#======================table frame===================
        table_frame =Frame(Right_frame, bd=2, bg="white", relief=RIDGE)
        table_frame.place(x=5, y=200, width=730, height=340)
        
        scroll_x = ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame,orient=VERTICAL)
        self.student_table=ttk.Treeview(table_frame,column=("dep", "course", "year", "sem", "id", "name","div", "roll", "gender", "dob", "email", "phone","address", "teacher", "photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X) 
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep",text="Department" )
        self.student_table.heading("course", text="Course")
        self.student_table.heading("year", text="Year")
        self.student_table.heading("sem", text="Semester")
        self.student_table.heading("id", text="StudentId")
        self.student_table.heading("name", text="Name")
        self.student_table.heading("roll",text="Roll")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("div", text="Division")
        self.student_table.heading("dob", text="DOB")
        self.student_table.heading("email", text="Email")
        self.student_table.heading("phone", text="Phone")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("teacher", text="Teacher")
        self.student_table.heading("photo", text="PhotoSampleStatus")
        self.student_table["show"]="headings"
 
        self.student_table.column("dep", width=100)
        self.student_table.column("course", width=100)
        self.student_table.column("year", width=100)
        self.student_table.column("sem", width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("name", width=100)
        self.student_table.column("roll",width=100)
        self.student_table.column("gender", width=100)
        self.student_table.column("div",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("email", width=100)
        self.student_table.column("phone", width=100)
        self.student_table.column("address", width=100)
        self.student_table.column("teacher", width=100)
        self.student_table.column("photo", width=100)

        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease>", self.get_curser)
        self.fetch_data()    



    # ======================= Search System =======================
    def add_data(self):
        if self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" or self.var_std_id.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
           try:
            conn = mysql.connector.connect(host="localhost", username="root", password=self.Db_pass, database="face_recognizer")
            my_cursor = conn.cursor()
            my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                self.var_dep.get(),
                self.var_course.get(),
                self.var_year.get(),
                self.var_semester.get(),
                self.var_std_id.get(),
                self.var_std_name.get(),
                self.var_div.get(),
                self.var_roll.get(),
                self.var_gender.get(),
                self.var_dob.get(),
                self.var_email.get(),
                self.var_phone.get(),
                self.var_address.get(),
                self.var_teacher.get(),
                self.var_radio1.get()
                ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Success", "Student details has been added successfully", parent=self.root)
           except Exception as es:
            messagebox.showerror("Error", f"Due to : {str(es)}", parent=self.root)
  

    # ============================fetch data===========================          
    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password=self.Db_pass, database="face_recognizer")
        my_cursor = conn.cursor()
        my_cursor.execute("Select * from student")
        data = my_cursor.fetchall()

        if len(data) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("", "end", values=i)

        conn.commit()
        conn.close()

    # ====================== get cursor======================     
    def get_curser(self,event=""):
        cursor_focus = self.student_table.focus()         
        content = self.student_table.item(cursor_focus)      
        data = content["values"]
        self.var_dep.set(data[0])
        self.var_course.set(data[1])
        self.var_semester.set(data[3])
        self.var_year.set(data[2])
        self.var_std_id.set(data[4])
        self.var_std_name.set(data[5])
        self.var_div.set(data[6])
        self.var_roll.set(data[7])
        self.var_gender.set(data[8])
        self.var_dob.set(data[9])
        self.var_email.set(data[10])
        self.var_phone.set(data[11])
        self.var_address.set(data[12])
        self.var_teacher.set(data[13])
        self.var_radio1.set(data[14])
        
            

    #================================Update Function============================
    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                Update= messagebox.askyesno("Update","Do you want to update this student details",parent=self.root)
                if Update>0:
                   conn=mysql.connector.connect(host="localhost",username="root",password=self.Db_pass,database="face_recognizer")
                   my_cursor=conn.cursor()
                   my_cursor.execute("update student set Dep=%s, course=%s, Yr=%s, Semester=%s, Division=%s, Roll=%s, Gender=%s, Dob=%s,Email=%s, Phone=%s, Address=%s, Teacher=%s, PhotoSample=%s where Student_id=%s", (
                       
                        self.var_dep.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_semester.get(),
                        self.var_div.get(),
                        self.var_roll.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_email.get(),
                        self.var_phone.get(),
                        self.var_address.get(),
                        self.var_teacher.get(),
                        self.var_radio1.get(),
                        self.var_std_id.get() 
                   ))
                                   
                else:
                   if not Update:
                       return
                messagebox.showinfo("Success","Student details succesfully update completed",parent=self.root)
                conn.commit()   
                self.fetch_data()
                conn.close()       
                                        
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)         
                
#===============Delete Function====================
    def delete_data(self):
        if self.var_std_id.get()=="":
            messagebox.showerror("Error,Student id must be required",parent=self.root)                      
        else:
            try:
                delete = messagebox.askyesno("Student Delete Page","Do you want to delete this student",parent=self.root)
                if delete > 0:
                    conn = mysql.connector.connect(host="localhost",user="root", password = self.Db_pass,database="face_recognizer")
                    my_cursor = conn.cursor()
                    # sql = "delete from student where Student_id = %s"
                    # val = (self.var_std_id.get(),)
                    my_cursor.execute("delete from student where Student_id = %s"%self.var_std_id.get())
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Successfully deleted student details",parent = self.root)
            except Exception as es:
                    messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)    

    #==========================reset data===============
    def reset_data(self):
        self.var_dep.set("SELECT department"),
        self.var_course.set("SELECT course"),
        self.var_year.set(""),
        self.var_semester.set("SELECT semester"),
        self.var_std_id.set(""),
        self.var_std_name.set(""),
        self.var_div.set("SELECT divison"),
        self.var_roll.set(""),
        self.var_gender.set("Male"),
        self.var_dob.set(""),
        self.var_email.set(""),
        self.var_phone.set(""),
        self.var_address.set(""),
        self.var_teacher.set(""),
        self.var_radio1.set(""),
                               

        # ========================== GENERATE DATA SAMPLES OR TAKE PHOTO SAMPLES ===========================
            
    def generate_dataset(self):
        print("Inside generate_dataset function")
        
        if self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" or self.var_std_id.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                print("Trying to connect to the database")
                conn = mysql.connector.connect(host="localhost", username="root", password=self.Db_pass, database="face_recognizer")
                print("Database connected successfully")
                
                my_cursor = conn.cursor()
                my_cursor.execute("Select * from student")
                myresult= my_cursor.fetchall()
                # id=0
                id=self.var_std_id.get()
                print(id)
                # id = (id[-3] +id[-2] +id[-1] ) 
                i = 1
                for x in myresult:
                    if i == id:
                    # id+=1
                        my_cursor.execute("update student set Dep=%s, course=%s, Yr=%s, Semester=%s, Division=%s, Roll=%s, Gender=%s, Dob=%s,Email=%s, Phone=%s, Address=%s, Teacher=%s, PhotoSample=%s where Student_id=%s", (
                            self.var_dep.get(),
                            self.var_course.get(),
                            self.var_year.get(),
                            self.var_semester.get(),
                            self.var_div.get(),
                            self.var_roll.get(),
                            self.var_gender.get(),
                            self.var_dob.get(),
                            self.var_email.get(),
                            self.var_phone.get(),
                            self.var_address.get(),
                            self.var_teacher.get(),
                            self.var_radio1.get(),
                            self.var_std_id.get()==id
                        ))
                    print("Database update successful")
                    
                conn.commit()
                self.reset_data()
                conn.close()

                print("Starting webcam capture")

                # Load predefined data on face frontals from OpenCV
                face_classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

                def face_cropped(img):
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray, 1.3, 5)
                    for (x, y, w, h) in faces:
                        face_cropped = img[y:y+h, x:x+w]
                        return face_cropped

                cap = cv2.VideoCapture(0)
                img_id = 0
                # std_id = self.var_std_id
                # print(std_id)
                while True:
                    ret, my_frame = cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id += 1
                        face = cv2.resize(face_cropped(my_frame), (450, 450))
                        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                        # file_name_path = "data/user." + str(id) + "." + str(img_id) + ".jpg"
                        file_name_path = "data/user." + id + "." + str(img_id) + ".jpg"
                        cv2.imwrite(file_name_path, face)
                        cv2.putText(face, str(img_id), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)
                        cv2.imshow("Cropped Face", face)

                    if cv2.waitKey(1) == 13 or int(img_id) == 100:
                        break

                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result", "Generating data sets completed!!!")

            except Exception as es:
                messagebox.showerror("Error", f"Due To: {str(es)}", parent=self.root)

                                
                            
if __name__ == "__main__":
    root = Tk() 
    obj = Student(root)
    root.mainloop()