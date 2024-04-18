from tkinter import *
import customtkinter as ct
from tkinter import messagebox
from PIL import Image, ImageTk
import subprocess

# Window widget

root = ct.CTk()
root.title("Login")
root.geometry("700x500")
root.resizable(False,False)
ct.set_appearance_mode("dark")
ct.set_default_color_theme("green")

# Fonts

FONT = ct.CTkFont(family="couture",size = 90)
Font1 =ct.CTkFont(family="Bebas Neue medium",size = 15)
Font2 =ct.CTkFont(family="Franklin Gothic Medium",size=15)
Font3= ct.CTkFont(family="Roboto Bold",size = 15)

# Login Database

import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "tsunade106",
    database = "Logindb")

cursor = mydb.cursor()

cursor.execute("Create database if not exists LoginDb")
cursor.execute('''Create table if not exists userdata(username varchar(255) primary key,password varchar(255))''')

# For Sign in

def signin():

    try:
        u = usern.get()
        p = passw.get()

        sql ="SELECT * From userdata where username = %s AND password =%s"
        val =(u,p)
        cursor.execute(sql,val)
        result =cursor.fetchall()

        mydb.commit()

        def callmain(data):
                if data:
                    subprocess.Popen(["python","main.py"])
                    root.destroy()
                else:
                    messagebox.showerror("Error","Password is Incorrect")       
        callmain(result)  
        
    except:
        pass

lable1 = ct.CTkLabel(root, text="Login",padx= 210,pady=50, width=20, height=30,font=FONT).grid(
    row=0,columnspan = 5)

usern = ct.CTkEntry(root,width=200, height=40,corner_radius=70, border_width=2,border_color="Green", 
fg_color="transparent", text_color="Green",placeholder_text="Username",placeholder_text_color="Green",font=Font1)
usern.place(x=250, y=200,)

passw = ct.CTkEntry(root,width=200, height=40,corner_radius=70, border_width=2,border_color="Green", 
fg_color="transparent",text_color="Green",placeholder_text=" Password",placeholder_text_color="Green",show="*",font=Font1)
passw.place(x=250, y=270)

signinimg = ct.CTkImage(dark_image=Image.open("signin.png"),size=(30,30))

LBt = ct.CTkButton(root,width=115, height=40,corner_radius=70,text="Sign In",border_color="#03A9F4",border_width=2,font=Font3,
text_color="#03A9F4",hover_color="#272727", fg_color="transparent", command=signin,image=signinimg,compound="left")
LBt.place(x=290, y=330)

# For sign up

def signup():
    root.withdraw()
    window = ct.CTkToplevel(root)
    window.geometry("700x500")
    window.title("Sign up")
    window.resizable(False,False)

    def Acc():
        user = euser.get()
        passwd = epass.get()
        sql = '''INSERT INTO Userdata
        (username,password) VALUES(%s,%s)'''

        val = (user,passwd)

        cursor.execute(sql,val)

        mydb.commit()

        subprocess.Popen(["python","main.py"])
        window.destroy()
        
    lable = ct.CTkLabel(master=window, text="Sign Up",padx= 160,pady=50, width=20, height=30,font=FONT).grid(
    row=0,columnspan = 5)

    euser = ct.CTkEntry(master=window,placeholder_text="Enter Username",width=200, height=40,corner_radius=70, 
    border_width=2,border_color="Green",fg_color="transparent", text_color="Green",font=Font1,placeholder_text_color="Green")
    euser.place(x=250, y = 200)

    epass = ct.CTkEntry(master=window,placeholder_text="Enter Password",width=200, height=40,corner_radius=70, 
    border_width=2,border_color="Green",fg_color="transparent", text_color="Green",font=Font1,placeholder_text_color="Green")
    epass.place(x=250, y = 270)
    
    createaccimg = ct.CTkImage(dark_image=Image.open("createacc.png"),size=(30,30))

    eBt = ct.CTkButton(master=window,width=115, height=40,corner_radius=70,text="Create",border_color="#03A9F4",
    border_width=2,font=Font3,text_color="#03A9F4",hover_color="#272727", fg_color="transparent",command=Acc,image=createaccimg)
    eBt.place(x=280, y=330)
    
signupBt = ct.CTkButton(root,width=20, height=30,corner_radius=70,  bg_color="transparent",hover_color="#272727", 
fg_color="transparent",  text="Click to Create Account :)",command=signup)
signupBt.place(x=265, y=390)

root.mainloop()