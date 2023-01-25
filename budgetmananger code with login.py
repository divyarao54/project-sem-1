from tkinter import *
from tkinter import messagebox, ttk
import mysql.connector
from PIL import Image, ImageTk
import customtkinter
customtkinter.set_default_color_theme("dark-blue") 
import os

def main():
    win=Tk()
    app=login_window(win)
    win.mainloop()
#===============================================================================================================
class login_window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")
        
        self.bg=ImageTk.PhotoImage(file=r"C:\Users\divya\Desktop\supermassive-black-hole-explosion-astronomy.jpg")
        lbl_bg=Label(self.root, image=self.bg)
        lbl_bg.place(x=0, y=0, relwidth=1, relheight=1)

        frame=Frame(self.root, bg="black")
        frame.place(x=610, y=170, width=340, height=450)

        img1=Image.open(r"C:\Users\divya\Desktop\848006.jpg")
        img1=img1.resize((90,90), Image.ANTIALIAS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        lbling1=Label(image=self.photoimage1, bg="black", borderwidth=0)
        lbling1.place(x=730, y=175, width=100, height=100)

        get_started=Label(frame, text="Get Started", font=("Helvetica", 20, "bold"), fg="white", bg="black")
        get_started.place(x=95, y=100)

        username=lb1=Label(frame, text="Username", font=("Helvetica", 15, "bold"), fg="white", bg="black")
        username.place(x=70, y=155)

        self.txtuser=ttk.Entry(frame, font=("Helvetica", 15, "bold"))
        self.txtuser.place(x=40, y=180, width=270)

        password=lb1=Label(frame, text="Password", font=("Helvetica", 15, "bold"), fg="white", bg="black")
        password.place(x=70, y=225)

        self.txtpass=ttk.Entry(frame, font=("Helvetica", 15, "bold"))
        self.txtpass.place(x=40, y=250, width=270)

        login_button=Button(frame, command=self.login, text="Login", font=("Helvetica", 15, "bold"), bd=3, relief=RIDGE, fg="white", bg="red", activeforeground="white", activebackground="red")
        login_button.place(x=110, y=300, width=120, height=35)

        register_button=Button(frame, text="New User? Create Account", command=self.register_window, font=("Helvetica", 10,"bold"), borderwidth=0, fg="white", bg="black", activeforeground="white", activebackground="black")
        register_button.place(x=25, y=350, width=160)

        #forgot_button=Button(frame, text="Forgot Password?", font=("Helvetica", 10,"bold"), borderwidth=0, fg="white", bg="black", activeforeground="white", activebackground="black")
        #forgot_button.place(x=0, y=370, width=160)
#================================================================================================================================
    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)
    
    def login(self):
        if self.txtuser.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("Error", "all field are required")
        elif self.txtuser.get()=="DEFAULT_USER" and self.txtpass.get()=="DEFAULTPASSWORD":
            messagebox.showinfo("Success", "Welcome back!")
        else:
            conn=mysql.connector.connect(user="root", password="mysqlpassword", host='127.0.0.1', database="project")
            my_cursor=conn.cursor()
            my_cursor.execute("select * from project.register_table where email=%s and password=%s", (self.txtuser.get(), self.txtpass.get()))
            row=my_cursor.fetchone()
            if row!=None:
                messagebox.showerror("Invalid", "Invalid Username or Password")
            else:
                openmain=messagebox.askyesno("YesNo", "Proceed?")
                if openmain>0:
                    c=os.system("python bm1.py")
                    #self.new_window=Toplevel(self.root)
                    #self.app= ex_program(self.new_window)
                else:
                    if not openmain:
                        return
                conn.commit()
                conn.close()             

#==========================================================================================================
class Register:
    def __init__(self, root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1600x900+0+0")

        self.var_first_name=StringVar()
        self.var_last_name=StringVar()
        self.var_email=StringVar()
        self.var_contact_number=StringVar()
        self.var_id=StringVar()
        self.var_username_new=StringVar()
        self.var_password_new=StringVar()
        self.var_password_confirm=StringVar()

        self.bg= ImageTk.PhotoImage(file=r"C:\Users\divya\Desktop\sean-pollock-PhYq704ffdA-unsplash.jpg")
        bg_lbl=Label(self.root, image=self.bg)
        bg_lbl.place(x=0, y=0, relwidth=1, relheight=1)

        self.bg1= ImageTk.PhotoImage(file=r"C:\Users\divya\Desktop\Screenshot 2023-01-03 090004.jpg")
        bg1_lbl=Label(self.root, image=self.bg1)
        bg1_lbl.place(x=50, y=100, width=470, height=550)

        frame= Frame(self.root, bg="white")
        frame.place(x=520, y=100, width=800, height=550)

        register_lbl=Label(frame, text="REGISTRATION", font=("Helvetica", 20, "bold"), fg="black", bg="white")
        register_lbl.place(x=20, y=20)


        first_name=Label(frame, text="First Name:", font=("Helvetica", 15, "bold"), bg="white")
        first_name.place(x=50, y=100)
        self.first_name_entry=Entry(frame, textvariable=self.var_first_name, font=("Helvetica", 15, "bold"))
        self.first_name_entry.place(x=50, y=130)

        last_name=Label(frame, text="Last Name:", font=("Helvetica", 15, "bold"), bg="white")
        last_name.place(x=450, y=100)
        self.last_name_entry=Entry(frame, textvariable=self.var_last_name, font=("Helvetica", 15, "bold"))
        self.last_name_entry.place(x=450, y=130)

        email=Label(frame, text="Email:", font=("Helvetica", 15, "bold"), bg="white")
        email.place(x=50, y=200)
        self.email_entry=Entry(frame, textvariable=self.var_email, font=("Helvetica", 15, "bold"))
        self.email_entry.place(x=50, y=230)

        contact_number=Label(frame, text="Contact Number:", font=("Helvetica", 15, "bold"), bg="white")
        contact_number.place(x=450, y=200)
        self.contact_number_entry=Entry(frame, textvariable=self.var_contact_number, font=("Helvetica", 15, "bold"))
        self.contact_number_entry.place(x=450, y=230)

        id=Label(frame, text="Enter last 4 digits of your ID:", font=("Helvetica", 15, "bold"), bg="white")
        id.place(x=50, y=300)
        self.id_entry=Entry(frame, textvariable=self.var_id, font=("Helvetica", 15, "bold"))
        self.id_entry.place(x=50, y=330)

        username_new=Label(frame, text="Username:", font=("Helvetica", 15, "bold"), bg="white")
        username_new.place(x=450, y=300)
        self.username_new_entry=Entry(frame, textvariable=self.var_username_new, font=("Helvetica", 15, "bold"))
        self.username_new_entry.place(x=450, y=330)
        
        password_new=Label(frame, text="Enter Password:", font=("Helvetica", 15, "bold"), bg="white")
        password_new.place(x=50, y=400)
        self.password_new_entry=Entry(frame, textvariable=self.var_password_new, font=("Helvetica", 15, "bold"))
        self.password_new_entry.place(x=50, y=430)

        password_confirm=Label(frame, text="Confirm Password:", font=("Helvetica", 15, "bold"), bg="white")
        password_confirm.place(x=450, y=400)
        self.password_confirm_entry=Entry(frame, textvariable=self.var_password_confirm, font=("Helvetica", 15, "bold"))
        self.password_confirm_entry.place(x=450, y=430)

        submit_button=Button(frame, text="SUBMIT", command=self.register_entries, font=("Helvetica", 15, "bold"), bd=3, relief=RIDGE, fg="white", bg="red", activeforeground="white", activebackground="red")
        submit_button.place(x=300, y=500)

#==================================================================================================================================

    def register_entries(self):
        if self.var_first_name.get()=="" or self.var_last_name.get()=="" or self.var_email.get()=="" or self.var_contact_number.get()=="" or self.var_id.get()=="":
            messagebox.showerror("Error", "Please fill in all the fields")
        elif self.var_password_new.get()!=self.var_password_confirm.get():
            messagebox.showerror("Error", "Please enter the same password for the confirmation")
        else:
            conn=mysql.connector.connect(user="root", password="mysqlpassword", host='127.0.0.1', database="project")
            my_cursor=conn.cursor()
            query=("select * from project.register_table where email=%s")
            value=(self.var_email.get(),)
            my_cursor.execute(query, value)
            row=my_cursor.fetchone()
            if row!=None:
                messagebox.showerror("Error", "User already exists, please choose a unique email id")
            else:
                my_cursor.execute("insert into project.register_table values(%s,%s,%s,%s,%s,%s)",(self.var_id.get(), 
                                                                                                  self.var_first_name.get(), 
                                                                                                  self.var_last_name.get(), 
                                                                                                  self.var_email.get(), 
                                                                                                  self.var_contact_number.get(), 
                                                                                                  self.var_password_new.get() ))

            conn.commit()
            conn.close()
            messagebox.showinfo("Successful", "You have registered successfully!")





#class ex_program:
    #c=os.system("python bm1.py")



if __name__=="__main__":
    main()
