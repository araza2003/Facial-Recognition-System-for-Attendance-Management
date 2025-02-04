from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog

mydata=[]

class Attendance:
    def __init__(self, root):
        self.root = root
        self.width= self.root.winfo_screenwidth()               
        self.height= self.root.winfo_screenheight()               
        self.root.geometry("%dx%d" % (self.width, self.height))
        self.root.title("Face Recognition System")
        
        #================ Text Variables =================
        
        self.var_atten_id=StringVar()
        self.var_atten_roll=StringVar()
        self.var_atten_name=StringVar()
        self.var_atten_dep=StringVar()
        self.var_atten_time=StringVar()
        self.var_atten_date=StringVar()
        self.var_atten_attendance=StringVar()

        # first image
        img = Image.open(r"images\smart-attendance.jpg")
        img = img.resize((800, 200), Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img)

        f_lbl1 = Label(self.root, image=self.photoimg1)
        f_lbl1.place(x=0, y=0, width=800, height=200)

        # second image
        img1 = Image.open(r"images\iStock-182059956_18390_t12.jpg")
        img1 = img1.resize((800, 200), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img1)

        f_lbl2 = Label(self.root, image=self.photoimg2)
        f_lbl2.place(x=800, y=0, width=800, height=200)

        # bg image
        img2 = Image.open(r"images\wp2551980.jpg")
        img2 = img2.resize((1530, 710), Image.LANCZOS)
        self.photoimg_bg = ImageTk.PhotoImage(img2)

        bg_img = Label(self.root, image=self.photoimg_bg)
        bg_img.place(x=0, y=200, width=1530, height=710)

        title_lbl=Label(bg_img,text="ATTENDANCE MANAGEMENT SYSTEM",font=("times new roman",35,"bold"), bg="white", fg="green")
        title_lbl.place(x=0,y=0,width=1530,height=45)
        
        # Back Button Functionality
        def go_back():
            self.root.destroy()

        # Back Button
        back_btn_img = Image.open(r"images\R.png")
        back_btn_img = back_btn_img.resize((50, 40), Image.LANCZOS)
        self.back_btn_photo = ImageTk.PhotoImage(back_btn_img)
        back_btn = Button(self.root, image=self.back_btn_photo, command=go_back, bd=0, bg="white")
        back_btn.place(x=10, y=203)
        
        
        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=20,y=55,width=1480,height=600)

        # left label frame
        Left_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Attendance Details", font=("times new roman", 12, "bold"))
        Left_frame.place(x=10,y=10,width=730,height=580)

        img_left=Image.open(r"images\AdobeStock_303989091.jpeg")
        img_left=img_left.resize((720,130), Image.LANCZOS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lbl=Label(Left_frame,image=self.photoimg_left)
        f_lbl.place(x=5,y=0,width=720,height=130)

        left_inside_frame=Frame(Left_frame,bd=2,relief=RIDGE,bg="white")
        left_inside_frame.place(x=0,y=135,width=720,height=370)

        # Labels and Entry

        # Attendance ID
        attendanceId_label = Label(left_inside_frame, text = "Attendance Id:", font=("times new roman", 11, "bold"), bg = "white")
        attendanceId_label.grid(row = 0, column = 0, padx = 10, pady=5, sticky = W)

        attendanceId_entry = ttk.Entry(left_inside_frame, width = 20,textvariable=self.var_atten_id, font=("times new roman", 11, "bold"))
        attendanceId_entry.grid(row = 0, column = 1, padx = 10, pady = 5, sticky = W)    

        # Name
        name_label = Label(left_inside_frame, text = "Name:", font=("times new roman", 11, "bold"), bg = "white")
        name_label.grid(row = 1, column = 0, padx = 10, pady=5, sticky = W)

        name_entry = ttk.Entry(left_inside_frame, width = 20,textvariable=self.var_atten_name, font=("times new roman", 11, "bold"))
        name_entry.grid(row = 1, column = 1, padx = 10, pady = 5, sticky = W)    

        # Time
        time_label = Label(left_inside_frame, text = "Time:", font=("times new roman", 11, "bold"), bg = "white")
        time_label.grid(row = 2, column = 0, padx = 10, pady=5, sticky = W)

        time_entry = ttk.Entry(left_inside_frame, width = 20,textvariable=self.var_atten_time , font=("times new roman", 11, "bold"))
        time_entry.grid(row = 2, column = 1, padx = 10, pady = 5, sticky = W)

        # Attendance Status
        attendance_label = Label(left_inside_frame, text = "Attendance Status:", font=("times new roman", 11, "bold"), bg = "white")
        attendance_label.grid(row = 3, column = 0, padx = 10, pady=5, sticky = W)

        self.attendance_entry = ttk.Combobox(left_inside_frame, width = 20,textvariable=self.var_atten_attendance, font=("times new roman", 11, "bold"), state='readonly')
        self.attendance_entry['values'] = ('Present', 'Absent', 'Leave')
        self.attendance_entry.grid(row = 3, column = 1, padx = 10, pady = 5, sticky = W)

        # Roll #
        roll_label = Label(left_inside_frame, text = "Roll #:", font=("times new roman", 11, "bold"), bg = "white")
        roll_label.grid(row = 0, column = 2, padx = 10, pady=5, sticky = W)

        roll_entry = ttk.Entry(left_inside_frame, width = 20,textvariable=self.var_atten_roll, font=("times new roman", 11, "bold"))
        roll_entry.grid(row = 0, column = 3, padx = 10, pady = 5, sticky = W)

        # Department
        department_label = Label(left_inside_frame, text = "Department:", font=("times new roman", 11, "bold"), bg = "white")
        department_label.grid(row = 1, column = 2, padx = 10, pady=5, sticky = W)

        department_entry = ttk.Entry(left_inside_frame, width = 20,textvariable=self.var_atten_dep, font=("times new roman", 11, "bold"))
        department_entry.grid(row = 1, column = 3, padx = 10, pady = 5, sticky = W)

        # Date
        date_label = Label(left_inside_frame, text = "Date:", font=("times new roman", 11, "bold"), bg = "white")
        date_label.grid(row = 2, column = 2, padx = 10, pady=5, sticky = W)

        date_entry = ttk.Entry(left_inside_frame, width = 20,textvariable=self.var_atten_date, font=("times new roman", 11, "bold"))
        date_entry.grid(row = 2, column = 3, padx = 10, pady = 5, sticky = W)

        # Buttons
        btn_frame = Frame(left_inside_frame, bd =2, relief = RIDGE)
        btn_frame.place(x=0, y=300, width = 670, height = 40)

        save_btn = Button (btn_frame, text = "Import csv",command=self.importCsv ,width = 17, font=("times new roman", 11, "bold"), bg = "blue", fg = "white")
        save_btn.grid(row = 0, column = 0) 

        update_btn = Button (btn_frame, text = "Export csv",command=self.exportCsv,width = 17, font=("times new roman", 11, "bold"), bg = "blue", fg = "white")
        update_btn.grid(row = 0, column = 1) 

        delete_btn = Button (btn_frame, text = "Update",command=self.update_data,width = 17, font=("times new roman", 11, "bold"), bg = "blue", fg = "white")
        delete_btn.grid(row = 0, column = 2) 

        reset_btn = Button (btn_frame, text = "Reset",command=self.reset_data,width = 17, font=("times new roman", 11, "bold"), bg = "blue", fg = "white")
        reset_btn.grid(row = 0, column = 3)  

        # right label frame
        Right_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Attendance Details", font=("times new roman", 12, "bold"))
        Right_frame.place(x=750,y=10,width=720,height=580)

        table_frame = Frame(Right_frame, bd =2, relief = RIDGE)
        table_frame.place(x=5, y=5, width = 700, height = 480)

        # ====================== Scroll Bar Table ==================
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.AttendanceReportTable=ttk.Treeview(table_frame,column=("ID","Roll","Name","Department","Time","Date","Attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading("ID",text="Attendance Id")
        self.AttendanceReportTable.heading("Roll",text="Roll#")
        self.AttendanceReportTable.heading("Name",text="Name")
        self.AttendanceReportTable.heading("Department",text="Department")
        self.AttendanceReportTable.heading("Time",text="Time")
        self.AttendanceReportTable.heading("Date",text="Date")
        self.AttendanceReportTable.heading("Attendance",text="Attendance")

        self.AttendanceReportTable["show"]="headings"

        self.AttendanceReportTable.column("ID",width=100)
        self.AttendanceReportTable.column("Roll",width=100)
        self.AttendanceReportTable.column("Name",width=100)
        self.AttendanceReportTable.column("Department",width=100)
        self.AttendanceReportTable.column("Time",width=100)
        self.AttendanceReportTable.column("Date",width=100)
        self.AttendanceReportTable.column("Attendance",width=100)


        self.AttendanceReportTable.pack(fill=BOTH, expand=1)
        
        self.AttendanceReportTable.bind("<ButtonRelease>", self.get_cursor)
        
    #================================ Fetch Data ============================
    
    def fetchData(self, rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("", END, values=i)

    #================================= Import CSV ===========================

    def importCsv(self):
        global mydata
        mydata.clear()
        fln = filedialog.askopenfilename(initialdir=os.getcwd(), title="Open CSV", filetypes=(("CSV file" , "*.csv"), ("ALL File" , "*.*")), parent=self.root)
        with open(fln) as myfile:
            csvread = csv.reader(myfile, delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)

    #================================= Export CSV ===========================

    def exportCsv(self):
        try:
            if len(mydata) < 1:
                messagebox.showerror("No Data", "No Data found to export", parent=self.root)
                return False
            
            fln = filedialog.asksaveasfilename(initialdir=os.getcwd(), title="Open CSV", filetypes=[("CSV file", "*.csv"), ("ALL File", "*.*")], parent=self.root)
            
            with open(fln, mode="w", newline="") as myfile:
                exp_write = csv.writer(myfile, delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                    
            messagebox.showinfo("Data Export", f"Your data exported to {os.path.basename(fln)} successfully")
        except Exception as es:
            messagebox.showerror("Error", f"Due To: {str(es)}", parent=self.root)
    
    #=========================== Cursor ===============================

    def get_cursor(self, event=""):
        cursor_row = self.AttendanceReportTable.focus()
        content = self.AttendanceReportTable.item(cursor_row)
        rows = content['values']
        self.var_atten_id.set(rows[0])
        self.var_atten_roll.set(rows[1])
        self.var_atten_name.set(rows[2])
        self.var_atten_dep.set(rows[3])
        self.var_atten_time.set(rows[4])
        self.var_atten_date.set(rows[5])
        self.var_atten_attendance.set(rows[6])
        
    #================================== Reset ===========================

    def reset_data(self):
        self.var_atten_id.set("")
        self.var_atten_roll.set("")
        self.var_atten_name.set("")
        self.var_atten_dep.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_attendance.set("")
        
    #================================= Update Data ===========================

    def update_data(self):
        try:
            if self.var_atten_id.get() == "":
                messagebox.showerror("Error", "Attendance ID must be required", parent=self.root)
                return False
            
            for index, row in enumerate(mydata):
                if row[0] == self.var_atten_id.get():
                    mydata[index] = [
                        self.var_atten_id.get(),
                        self.var_atten_roll.get(),
                        self.var_atten_name.get(),
                        self.var_atten_dep.get(),
                        self.var_atten_time.get(),
                        self.var_atten_date.get(),
                        self.var_atten_attendance.get()
                    ]
                    break

            self.fetchData(mydata)
            
            messagebox.showinfo("Success", "Attendance details successfully updated", parent=self.root)
        except Exception as es:
            messagebox.showerror("Error", f"Error due to: {str(es)}", parent=self.root)


if __name__ == "__main__":
    root = Tk()
    obj = Attendance(root)
    root.mainloop()
    