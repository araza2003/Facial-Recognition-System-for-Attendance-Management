from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np
from time import strftime
from datetime import datetime

class Face_Recognition:
    def __init__(self, root):
        self.root = root
        self.width= self.root.winfo_screenwidth()               
        self.height= self.root.winfo_screenheight()               
        self.root.geometry("%dx%d" % (self.width, self.height))
        self.root.title("Face Recognition System")
        
        self.db_pass = "Ar12345#"
        
        # Main Title
        title_lbl = Label (self.root, text="FACE RECOGNITION", font=("times new roman", 25, "bold"), bg="orange", fg="black")
        title_lbl.place(x=0, y=0, width=1530, height=45)
        
        # Back Button Functionality
        def go_back():
            self.root.destroy()

        # Back Button
        back_btn_img = Image.open(r"images\R.png")
        back_btn_img = back_btn_img.resize((50, 40), Image.LANCZOS)
        self.back_btn_photo = ImageTk.PhotoImage(back_btn_img)
        back_btn = Button(self.root, image=self.back_btn_photo, command=go_back, bd=0, bg="orange")
        back_btn.place(x=10, y=2)
        

        # -------------------------------- Images -----------------------------------
        # First Image
        img_top=Image.open(r"images\face_detector1.jpg")
        img_top = img_top.resize((650, 750), Image.LANCZOS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0,y=45,width=650,height=750)
        
        # 2nd Image
        img_top1=Image.open(r"images\facial_recognition_system_identification_digital_id_security_scanning_thinkstock_858236252_3x3-100740902-large.jpg")
        img_top1 = img_top1.resize((950, 750), Image.LANCZOS)
        self.photoimg_top1=ImageTk.PhotoImage(img_top1)

        f_lbl=Label(self.root, image=self.photoimg_top1)
        f_lbl.place(x=650, y=45, width=950, height=750)
        
        # ----------------------------- button ----------------------------------------
        b1_1=Button(self.root,text="Face Recognition", cursor="hand2",command=self.face_recog,font=("times new roman", 18,"bold"),bg="darkgreen",fg="white")
        b1_1.place(x=1020, y=710, width=200, height=40)
    
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ATTENDANCE ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    # def mark_attendance(self,i,r,n,d):
    #     now=datetime.now()
    #     current_date=now.strftime("%d/%m/%Y")
    #     path = f"attendance_Data/attendance_{current_date}.csv"
    #     with open(path,"w+",newline="\n") as f:
    #         myDataList=f.readlines()
    #         name_list=[]
    #         for line in myDataList:
    #             entry=line.split((","))
    #             name_list.append(entry[0])
    #         if((i not in name_list) and (r not in name_list) and (n not in name_list) and (d not in name_list)):
    #             now=datetime.now()
    #             d1=now.strftime("%d/%m/%Y")
    #             dtString=now.strftime("%H:%M:%S")
    #             f.writelines(f"\n{i},{r},{n},{d},{dtString},{d1},Present")
        

    def mark_attendance(self, i, r, n, d):
        now = datetime.now()
        current_date = now.strftime("%d-%m-%Y")
        path = f"attendance_Data/attendance_{current_date}.csv"

        # Ensure the directory exists
        os.makedirs(os.path.dirname(path), exist_ok=True)  # Create the directory if it doesn't exist

        # Open the CSV file safely (append mode to add new entries without overwriting existing ones)
        with open(path, "a+", newline="\n") as f:
            # Read existing data
            f.seek(0)  # Go to the beginning of the file
            myDataList = f.readlines()
            name_list = [line.split(",")[0] for line in myDataList]  # Extract the first column (e.g., Student ID)

            # Check if this data is already recorded
            if (i not in name_list) and (r not in name_list) and (n not in name_list) and (d not in name_list):
                dtString = now.strftime("%I:%M:%S %p")
                d1 = now.strftime("%d-%m-%Y")
                f.write(f"{i},{r},{n},{d},{dtString},{d1},Present\n")

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ FACE RECOGNITION ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def face_recog(self):
        def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)    
            features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)
                
            coord = []
                
            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 3)
                id, predict = clf.predict(gray_image[y:y+h, x:x+w])
                confidence = int((100 * (1 - predict/300)))
                    
                if confidence > 83:
                    # Fetching data from database
                    # print(confidence)
                    conn = mysql.connector.connect(host="localhost", username="root", password=self.db_pass, database="face_recognizer")
                    my_cursor = conn.cursor()
                    for student_id in range(1, 1001):  # Assuming student IDs are between 1 and 1000
                        # Construct SQL query
                        if student_id == id:
                            
                            sql_query = "SELECT Student_name, Roll, Student_id, Dep FROM student WHERE Student_id = %s" % (student_id,)

                            # Execute SQL query
                            my_cursor.execute(sql_query)
                            data = my_cursor.fetchone()
                            # print(data)
                            if data:
                                n,r,i,d = data  # Unpack the retrieved data
                                # n = n if n else "Unknown"
                                # r = r if r else "Unknown"
                                # i = i if i else "Unknown"
                                # d = d if d else "Unknown"
                                print("Name:", n)
                                print("Roll:", r)
                                print("Department:", d)
                                print("Student ID:", i)
                                cv2.putText(img, f"Student ID:{i}", (x, y-80), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                                cv2.putText(img, f"Roll:{r}", (x, y-55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                                cv2.putText(img, f"Name:{n}", (x, y-30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                                cv2.putText(img, f"Department:{d}", (x, y-5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                                #cv2.putText(img, f"Attendance Marked!:", (x, y+280), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                                self.mark_attendance(i,r,n,d)
                                break  # Stop iterating if data is found
                        else:
                            print("Student data not found")
                            continue
                else:
                    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 3)
                    cv2.putText(img, "Unknown Person", (x, y-5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
      
                    coord = [x, y, w, y]
                        
            return coord
            
        def recognize(img, clf, faceCascade):
            coord = draw_boundary(img, faceCascade, 1.1, 10, (255, 25, 255), "Face", clf)
            return img
            
        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer.create()
        clf.read("classifier.xml")
            
        # 0 for local camera and 1 for external one
        video_cap = cv2.VideoCapture(0)
            
        while True:
            ret, img = video_cap.read()
            img = recognize(img, clf, faceCascade)
            cv2.imshow("Welcome To Face Recognition", img)
                
            if cv2.waitKey(1) == 13:
                break

        video_cap.release()
        cv2.destroyAllWindows()
    
if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()
