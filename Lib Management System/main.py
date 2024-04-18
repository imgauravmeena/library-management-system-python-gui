from tkinter import *
import customtkinter as ct
from PIL import Image,ImageTk
from tkinter import messagebox
from database import *
import subprocess

# Window widget

main = ct.CTk()
main.title("Library Management System")
main.geometry("800x562+200+80")
main.resizable(False, False)
ct.set_appearance_mode("dark")
ct.set_default_color_theme("green")

# Fonts

FONT = ct.CTkFont(family="couture",size = 35)
Font1 =ct.CTkFont(family="Bebas Neue medium",size = 15)
Font2 =ct.CTkFont(family="Franklin Gothic Medium",size=15)
Font3= ct.CTkFont(family="Roboto Bold",size = 15)

# Lables for Main window

lable1 = ct.CTkLabel(main,fg_color="#3da4ab", text="Library Management system",padx= 104,pady=35, height=30,font=FONT,text_color="white").grid(
    row=0,columnspan = 5)

libimage=ct.CTkImage(dark_image= Image.open("library.jpg"),size=(1000,500))

lable2=ct.CTkLabel(main,image=libimage,text="").place(x=0,y=100)

# Functions

# To Add Book

def addbook():
    main.withdraw()
    window = ct.CTkToplevel(main)
    window.geometry("800x562+200+80")
    window.title("Add Books")
    window.resizable(False,False)

    lable1 = ct.CTkLabel(window,bg_color="#3da4ab",fg_color="#3da4ab", text="Add Books",padx= 300,pady=35, height=30,font=FONT,text_color="white").grid(
    row=0,columnspan = 5)

    ebookid = ct.CTkEntry(master=window,placeholder_text="Book Id",width=200, height=40,corner_radius=70, border_width=2,border_color="Green",
    text_color="Green",font=Font1,placeholder_text_color="Green")
    ebookid.place(x=300, y = 150)

    etitle = ct.CTkEntry(master=window,placeholder_text="Book Title",width=200, height=40,corner_radius=70, border_width=2,border_color="Green",
    text_color="Green",font=Font1,placeholder_text_color="Green")
    etitle.place(x=300, y = 210)

    editionb = ct.CTkEntry(master=window,placeholder_text="Book Edition",width=200, height=40,corner_radius=70, border_width=2,
    border_color="Green", text_color="Green",font=Font1,placeholder_text_color="Green")
    editionb.place(x=300, y = 270)

    eprice = ct.CTkEntry(master=window,placeholder_text="Book price",width=200, height=40,corner_radius=70, border_width=2,
    border_color="Green", text_color="Green",font=Font1,placeholder_text_color="Green")
    eprice.place(x=300, y = 330)

    Author = ct.CTkEntry(master=window,placeholder_text="Book Author",width=200, height=40,corner_radius=70, border_width=2,
    border_color="Green", text_color="Green",font=Font1,placeholder_text_color="Green")
    Author.place(x=300, y = 390)

    def addbook():

        bookidd = ebookid.get()
        title = etitle.get()
        editions= editionb.get()
        pricee = eprice.get()
        authorss = Author.get()

        sql = '''INSERT INTO Bookt
        (BookId,Title,Author,Edition,price) VALUES(%s,%s,%s,%s,%s)'''

        val =(bookidd,title,authorss,editions,pricee)

        cursor.execute(sql,val)

        mydb.commit()

    
    def reset():

        ebookid.delete(0,ct.END)
        etitle.delete(0,ct.END)
        editionb.delete(0,ct.END)
        eprice.delete(0,ct.END)
        Author.delete(0,ct.END)

    def home():
        main.deiconify()
        window.withdraw()

    addbookk = ct.CTkImage(dark_image= Image.open("createacc.png"),size=(30,30))
    homeimage = ct.CTkImage(dark_image= Image.open("home.png"),size=(30,30))

    addbookBt =ct.CTkButton(window,width=115, height=40,corner_radius=70,text="Add Book",border_color="#03A9F4",border_width=2,font=Font3,
    text_color="#03A9F4",hover_color="#272727", fg_color="transparent", command=addbook,image=addbookk)
    addbookBt.place(x=325, y=450)

    homeb = ct.CTkButton(window,image=homeimage ,width=5,bg_color="transparent",hover_color="#272727",text="",command=home,fg_color="transparent")
    homeb.place(x=20,y=120)

    resetBt =ct.CTkButton(window,width=20, height=30,corner_radius=70,  bg_color="transparent",hover_color="#272727", text_color="white",
    fg_color="transparent",  text="Click to Reset",command=reset,font=Font3)
    resetBt.place(x=335, y=500)

# To Edit Book

def editbook():
    main.withdraw()
    window = ct.CTkToplevel(main)
    window.geometry("800x562+200+80")
    window.title("Edit Books")
    window.resizable(False,False)

    lable1 = ct.CTkLabel(window,bg_color="#3da4ab",fg_color="#3da4ab", text="Edit Books",padx= 300,pady=35, height=30,font=FONT,
    text_color="white").grid(
    row=0,columnspan = 5)

    ebookid = ct.CTkEntry(master=window,placeholder_text="Book Id",width=200, height=40,corner_radius=70, border_width=2,border_color="Green",
    text_color="Green",font=Font1,placeholder_text_color="Green")
    ebookid.place(x=300, y = 170)

    eupdate = ct.CTkComboBox(window,width=200,height=40,corner_radius=70,values=["Bookid","Author","Title","Edition","Price"],border_width=2,
    border_color="#03A9F4",text_color="#03A9F4",font=Font1,dropdown_font=Font1,dropdown_text_color="#03A9F4")
    eupdate.place(x=300, y = 250)

    enew = ct.CTkEntry(master=window,placeholder_text="Enter New Val",width=200, height=40,corner_radius=70, border_width=2,border_color="Green",
    text_color="Green",font=Font1,placeholder_text_color="Green")
    enew.place(x=300, y = 330)

    def submits():
        entry1= ebookid.get()
        entry2= eupdate.get()
        entry3= enew.get()

        if entry2=="Bookid":
            sql = "update bookt set BookId =%s where bookid=%s"
            val =(entry3,entry1)
            cursor.execute(sql,val)
            mydb.commit()

        elif entry2=="Title":
            sql = "update bookt set Title =%s where bookid=%s"
            val =(entry3,entry1)
            cursor.execute(sql,val)
            mydb.commit()

        elif entry2=="Author":
            sql = "update bookt set Author =%s where bookid=%s"
            val =(entry3,entry1)
            cursor.execute(sql,val)
            mydb.commit()

        elif entry2=="Edition":
            sql = "update bookt set Edition =%s where bookid=%s"
            val =(entry3,entry1)
            cursor.execute(sql,val)
            mydb.commit()

        elif entry2=="price":
            sql = "update bookt set price =%s where bookid=%s"
            val =(entry3,entry1)
            cursor.execute(sql,val)
            mydb.commit()


    def reset():
        ebookid.delete(0,ct.END)
        enew.delete(0,ct.END)

    def home():
        main.deiconify()
        window.withdraw()

    homeimage = ct.CTkImage(dark_image= Image.open("home.png"),size=(30,30))

    homeb = ct.CTkButton(window,image=homeimage ,width=5,bg_color="transparent",hover_color="#272727",text="",command=home, 
    fg_color="transparent")
    homeb.place(x=20,y=120)

    submitb = ct.CTkButton(window,width=115, height=40,corner_radius=70,text="Update",border_color="#03A9F4",border_width=2,font=Font3,
    text_color="#03A9F4",hover_color="#272727", fg_color="transparent", command=submits)
    submitb.place(x=340, y=410)

    resetBt =ct.CTkButton(window,width=20, height=30,corner_radius=70,  bg_color="transparent",hover_color="#272727", text_color="white",
    fg_color="transparent",  text="Click to Reset",command=reset,font=Font3)
    resetBt.place(x=335, y=480)

# To Delete Book

def delbook():
    main.withdraw()
    window = ct.CTkToplevel(main)
    window.geometry("800x562+200+80")
    window.title("Delete Books")
    window.resizable(False,False)

    lable1 = ct.CTkLabel(window,bg_color="#3da4ab",fg_color="#3da4ab", text="Delete Books",padx= 300,pady=35, height=30,font=FONT,
    text_color="white").grid(
    row=0,columnspan = 5)

    edelbook = ct.CTkEntry(master=window,placeholder_text="Enter Book Id",width=200, height=40,corner_radius=70, border_width=2,
    border_color="Green",text_color="Green",font=Font1,placeholder_text_color="Green")
    edelbook.place(x=300, y = 150)

    textbox = ct.CTkTextbox(window,width=600,corner_radius=20,font=Font1)
    textbox.place(x=100,y=230)

    def submits():
        entry = edelbook.get()
        sql = "Select * from bookt where BookId=%s"
        cursor.execute(sql,(entry,))

        result=cursor.fetchone()

        mydb.commit()

        def inserted_data(data):
            textbox.insert(ct.END,"BookId \t Title \t\t\t Author \t\t\t Edition \t price \n")
            if data:
                formatted_row = f"\n {data[0]}\t {data[1]}\t\t\t {data[2]}\t\t\t {data[3]}\t {data[4]}"
                textbox.insert(ct.END,formatted_row+"\n")

        inserted_data(result)


    submitb = ct.CTkButton(window,width=115, height=40,corner_radius=70,text="Search",border_color="#03A9F4",border_width=2,font=Font3,
    text_color="#03A9F4",hover_color="#272727", fg_color="transparent", command=submits)
    submitb.place(x=550, y=150)
    
  
    def dellbook():

        A = messagebox.askyesno("Confirmation","Wanna Delete?")

        if A:
            entry = edelbook.get()
    
            sql1 = "Delete from bookt where BookId=%s"
            cursor.execute(sql1,(entry,))

            mydb.commit()

        else:
            messagebox.askokcancel("Confirmation","Cancel the operation")

    def reset():
        edelbook.delete(0,ct.END)
        textbox.delete(1.0,ct.END)

    resetBt = ct.CTkButton(window,width=20, height=30,corner_radius=70,  bg_color="transparent",hover_color="#272727", fg_color="transparent", 
    text="Click to Reset",font=Font3,command=reset)
    resetBt.place(x=345, y=510)

    def home():
        main.deiconify()
        window.withdraw()

    homeimage = ct.CTkImage(dark_image= Image.open("home.png"),size=(30,30))

    homeb = ct.CTkButton(window,image=homeimage ,width=5,bg_color="transparent",hover_color="#272727",text="",command=home,fg_color="transparent")
    homeb.place(x=20,y=120)

    delbookkbt =ct.CTkButton(window,width=115, height=40,corner_radius=70,text="Del book",border_color="#03A9F4",border_width=2,font=Font3,
    text_color="#03A9F4",hover_color="#272727", fg_color="transparent", command=dellbook)
    delbookkbt.place(x=350, y=460)

# To Add Student

def addstud():
    main.withdraw()
    window = ct.CTkToplevel(main)
    window.geometry("800x562+200+80")
    window.title("Add Student")
    window.resizable(False,False)

    lable1 = ct.CTkLabel(window,bg_color="#3da4ab",fg_color="#3da4ab", text="Add Student",padx= 300,pady=35, height=30,font=FONT,
    text_color="white").grid(
    row=0,columnspan = 5)

    estudid = ct.CTkEntry(master=window,placeholder_text="Student Id",width=200, height=40,corner_radius=70, border_width=2,
    border_color="Green",text_color="Green",font=Font1,placeholder_text_color="Green")
    estudid.place(x=300, y = 150)

    ename = ct.CTkEntry(master=window,placeholder_text="Name",width=200, height=40,corner_radius=70, border_width=2,border_color="Green", 
    text_color="Green",font=Font1,placeholder_text_color="Green")
    ename.place(x=300, y = 210)

    ecourse = ct.CTkEntry(master=window,placeholder_text="Course",width=200, height=40,corner_radius=70, border_width=2,border_color="Green", 
    text_color="Green",font=Font1,placeholder_text_color="Green")
    ecourse.place(x=300, y = 270)

    econtact = ct.CTkEntry(master=window,placeholder_text="Contact",width=200, height=40,corner_radius=70, border_width=2,border_color="Green", 
    text_color="Green",font=Font1,placeholder_text_color="Green")
    econtact.place(x=300, y = 330)

    eschool = ct.CTkEntry(master=window,placeholder_text="School Name",width=200, height=40,corner_radius=70, border_width=2,
    border_color="Green", text_color="Green",font=Font1,placeholder_text_color="Green")
    eschool.place(x=300, y = 390)

    def addstuddd():

        studidd = estudid.get()
        namee = ename.get()
        coursess= ecourse.get()
        contactt = econtact.get()
        school = eschool.get()

        sql = '''INSERT INTO Student
        (StudentId,Name,Course,Contact,School) VALUES(%s,%s,%s,%s,%s)'''

        val =(studidd,namee,coursess,contactt,school)

        cursor.execute(sql,val)

        mydb.commit()

    
    def reset():

        estudid.delete(0,ct.END)
        ename.delete(0,ct.END)
        ecourse.delete(0,ct.END)
        econtact.delete(0,ct.END)
        eschool.delete(0,ct.END)

    def home():
        main.deiconify()
        window.withdraw()

    homeimage = ct.CTkImage(dark_image= Image.open("home.png"),size=(30,30))

    addstudd = ct.CTkImage(dark_image= Image.open("createacc.png"),size=(30,30))

    homeb = ct.CTkButton(window,image=homeimage ,width=5,bg_color="transparent",hover_color="#272727",text="",command=home, 
    fg_color="transparent")
    homeb.place(x=20,y=120)

    addstuddBt =ct.CTkButton(window,width=115, height=40,corner_radius=70,text="Add Stud",border_color="#03A9F4",border_width=2,font=Font3,
    text_color="#03A9F4",hover_color="#272727", fg_color="transparent", command=addstuddd,image=addstudd)
    addstuddBt.place(x=325, y=450)

    resetBt =ct.CTkButton(window,width=20, height=30,corner_radius=70,  bg_color="transparent",hover_color="#272727", text_color="white",
    fg_color="transparent",  text="Click to Reset",command=reset,font=Font3)
    resetBt.place(x=335, y=500)

# To Issue Book

def issuebook():
    main.withdraw()
    window = ct.CTkToplevel(main)
    window.geometry("800x562+200+80")
    window.title("Issue Books")
    window.resizable(False,False)
    
    lable1 = ct.CTkLabel(window,bg_color="#3da4ab",fg_color="#3da4ab", text="Issue Books",padx= 300,pady=35, height=30,font=FONT,
    text_color="white").grid(
    row=0,columnspan = 5)

    frame = ct.CTkFrame(window,width=320,height=390,corner_radius=20,fg_color="#272727")
    frame.place(x=440,y=140)

    estudid1= ct.CTkEntry(master=window,placeholder_text="Student Id",width=200, height=40,corner_radius=70, border_width=2,
    border_color="Green",text_color="Green",font=Font1,placeholder_text_color="Green",bg_color="#272727")
    estudid1.place(x=500, y = 170)

    ebookid = ct.CTkEntry(master=window,placeholder_text="BookId",width=200, height=40,corner_radius=70, border_width=2,
    border_color="Green",text_color="Green",font=Font1,placeholder_text_color="Green",bg_color="#272727")
    ebookid.place(x=500, y = 230)

    edate = ct.CTkEntry(master=window,placeholder_text="Date: YYYY-MM-DD",width=200, height=40,corner_radius=70, border_width=2,
    border_color="Green",text_color="Green",font=Font1,placeholder_text_color="Green",bg_color="#272727")
    edate.place(x=500, y = 290)

    def issueeebook():
        sql = "Update Student Set Bookid= %s where Studentid =%s"
        val = (ebookid.get(),estudid1.get(),)

        sql2=  "Update Student Set issue_date= %s where Studentid =%s"
        val2 = (edate.get(),estudid1.get(),)

        cursor.execute(sql,val)
        cursor.execute(sql2,val2)

        mydb.commit()

    def reset():
        ebookid.delete(0,ct.END)
        estudid1.delete(0,ct.END)
        edate.delete(0,ct.END)
        estudid.delete(0,ct.END)
        textbox.delete(1.0,ct.END)

    issueeb = ct.CTkButton(window,width=115, height=40,corner_radius=70,text="Issue Book",border_color="#03A9F4",border_width=2,
    font=Font3,text_color="#03A9F4",hover_color="#272727", fg_color="transparent", command=issueeebook)
    issueeb.place(x=540, y=370)

    resetb = ct.CTkButton(window,width=115, height=40,corner_radius=70,text="Reset",border_color="#03A9F4",border_width=2,font=Font3,
    text_color="#03A9F4",hover_color="#272727", fg_color="transparent", command=reset)
    resetb.place(x=540, y=440)

    estudid = ct.CTkEntry(master=window,placeholder_text="Student Id",width=200, height=40,corner_radius=70, border_width=2,
    border_color="Green",text_color="Green",font=Font1,placeholder_text_color="Green")
    estudid.place(x=150, y = 150)

    textbox = ct.CTkTextbox(window,width=300,height=200,corner_radius=20,font=Font1)
    textbox.place(x=100,y=300)

    def submits():
        sql = "Select * from Student where StudentId = %s"
        studentid= estudid.get()
        cursor.execute(sql,(studentid,))
        result = cursor.fetchall()

        def inserted_data(result):
            if not result:
                textbox.insert(ct.END,"No Student Found!")

            for row in result:
                formatted_row = f"\nStudent Id :{row[0]}\n\n Name :{row[1]}\n\n Course :{row[2]}\n\n Contact :{row[3]}\n\n School :{row[4]}\n\n"
                textbox.insert(ct.END,formatted_row+"\n")
            
        inserted_data(result)

        mydb.commit()

    def home():
        main.deiconify()
        window.withdraw()

    homeimage = ct.CTkImage(dark_image= Image.open("home.png"),size=(30,30))

    homeb = ct.CTkButton(window,image=homeimage ,width=5,bg_color="transparent",hover_color="#272727",text="",command=home,
    fg_color="transparent")
    homeb.place(x=20,y=120)
        
    submitb = ct.CTkButton(window,width=115, height=40,corner_radius=70,text="Search",border_color="#03A9F4",border_width=2,font=Font3,
    text_color="#03A9F4",hover_color="#272727", fg_color="transparent", command=submits)
    submitb.place(x=190, y=220)

# To Return Book

def returnbook():
    main.withdraw()
    window = ct.CTkToplevel(main)
    window.geometry("800x562+200+80")
    window.title("Return Books")
    window.resizable(False,False)

    lable1 = ct.CTkLabel(window,bg_color="#3da4ab",fg_color="#3da4ab", text="Return Books",padx= 300,pady=35, height=30,font=FONT,
    text_color="white").grid(
    row=0,columnspan = 5)

    estudid = ct.CTkEntry(master=window,placeholder_text="StudentId",width=200, height=40,corner_radius=70, border_width=2,
    border_color="Green",text_color="Green",font=Font1,placeholder_text_color="Green")
    estudid.place(x=150, y = 150)

    textbox = ct.CTkTextbox(window,width=300,height=200,corner_radius=20,font=Font1)
    textbox.place(x=100,y=300)

    frame = ct.CTkFrame(window,width=320,height=390,corner_radius=20,fg_color="#272727")
    frame.place(x=440,y=140)

    ereturn = ct.CTkEntry(master=window,placeholder_text="Return Date :YYYY-MM-DD",width=200, height=40,corner_radius=70, 
    border_width=2,border_color="Green",text_color="Green",font=Font1,placeholder_text_color="Green",bg_color="#272727")
    ereturn.place(x=500, y = 200)

    def returnnbook():
        sql = "Update Student Set Return_date = %s where studentid=%s"
        val= (ereturn.get(),estudid.get(),)
        cursor.execute(sql,val)
        mydb.commit()

    returnb = ct.CTkButton(window,width=115, height=40,corner_radius=70,text="Return Book",border_color="#03A9F4",border_width=2,
    font=Font3,text_color="#03A9F4",hover_color="#272727", fg_color="transparent", command=returnnbook)
    returnb.place(x=540, y=300)

    def reset():

        estudid.delete(0,ct.END)
        textbox.delete(1.0,ct.END)
        ereturn.delete(0,ct.END)

    resetb = ct.CTkButton(window,width=115, height=40,corner_radius=70,text="Reset",border_color="#03A9F4",border_width=2,font=Font3,
    text_color="#03A9F4",hover_color="#272727", fg_color="transparent", command=reset)
    resetb.place(x=545, y=400)

    def submits():
        sql = "Select * from Student where Studentid =%s"
        val =(estudid.get(),)
        cursor.execute(sql,val)
        result = cursor.fetchall()
        mydb.commit()

        def inserted_data(result):
            for row in result:
                formatted_row = f"\nName :{row[1]}\n\n Book Id :{row[5]}\n\n Issue Date :{row[6]}\n\n"
                textbox.insert(ct.END,formatted_row+"\n")

        inserted_data(result)

    submitb = ct.CTkButton(window,width=115, height=40,corner_radius=70,text="Search",border_color="#03A9F4",border_width=2,font=Font3,
    text_color="#03A9F4",hover_color="#272727", fg_color="transparent", command=submits)
    submitb.place(x=190, y=220)

    def home():
        main.deiconify()
        window.withdraw()

    homeimage = ct.CTkImage(dark_image= Image.open("home.png"),size=(30,30))

    homeb = ct.CTkButton(window,image=homeimage ,width=5,bg_color="transparent",hover_color="#272727",text="",command=home, 
    fg_color="transparent")
    homeb.place(x=20,y=120)

# To Show Books

def showbook():
    main.withdraw()
    window = ct.CTkToplevel(main)
    window.geometry("800x562+200+80")
    window.title("Show Books")
    window.resizable(False,False)
    
    lable1 = ct.CTkLabel(window,bg_color="#3da4ab",fg_color="#3da4ab", text="Show Books",padx= 300,pady=35, height=30,font=FONT,
    text_color="white").grid(
    row=0,columnspan = 5)

    textbox = ct.CTkTextbox(window,width=600,height=370,corner_radius=20,font=Font1)
    textbox.place(x=100,y=150)


    sql ="Select * from bookt"
    cursor.execute(sql)
    result = cursor.fetchall()

    def inserted_data(data):
        textbox.insert(ct.END,"BookId \t Title \t\t\t Author \t\t\t Edition \t price \t")
        for row in data:
            formatted_row = f"\n{row[0]}\t {row[1]}\t\t\t {row[2]}\t\t\t {row[3]}\t {row[4]}"
            textbox.insert(ct.END,formatted_row+"\n")

    inserted_data(result)
    
    def home():
        main.deiconify()
        window.withdraw()

    homeimage = ct.CTkImage(dark_image= Image.open("home.png"),size=(30,30))

    homeb = ct.CTkButton(window,image=homeimage ,width=5,bg_color="transparent",hover_color="#272727",text="",command=home, 
    fg_color="transparent")
    homeb.place(x=20,y=120)

# To Logout

def Logout():
    D = main.destroy()
    subprocess.Popen(["python","login.py"])
    

# Images for Main Window Buttons


addbookimage=ct.CTkImage(dark_image= Image.open("add book.png"),size=(30,30))

editbookimage=ct.CTkImage(dark_image= Image.open("edit book.png"),size=(30,30))

delbookimage=ct.CTkImage(dark_image= Image.open("Delete book .png"),size=(30,30))

addstudimage=ct.CTkImage(dark_image= Image.open("student.png"),size=(30,30))

issueimage=ct.CTkImage(dark_image= Image.open("issue.png"),size=(30,30))

returnimage=ct.CTkImage(dark_image= Image.open("return.png"),size=(30,30))

bookimage=ct.CTkImage(dark_image= Image.open("book.png"),size=(30,30))

logoutimage=ct.CTkImage(dark_image= Image.open("logout.png"),size=(30,30))


# Main Window Buttons

addbut = ct.CTkButton(main,width=115, height=40,text="Add Books",fg_color="green",bg_color="green",font=Font3,image=addbookimage,command=addbook)
addbut.place(x=180, y=150)

editbut = ct.CTkButton(main,width=115, height=40,text="Edit Books",fg_color="green",bg_color="green",font=Font3,image=editbookimage,command=editbook)
editbut.place(x=180, y=250)

delbut = ct.CTkButton(main,width=115, height=40,text="Delete Books",fg_color="green",bg_color="green",font=Font3,image=delbookimage,command=delbook)
delbut.place(x=180, y=350)

addstubut = ct.CTkButton(main,width=115, height=40,text="Add Students",fg_color="green",bg_color="green",font=Font3,image=addstudimage,command=addstud)
addstubut.place(x=180, y=450)

issuebut = ct.CTkButton(main,width=115, height=40,text="Issue Books",fg_color="green",bg_color="green",font=Font3,image=issueimage,command=issuebook)
issuebut.place(x=500, y=150)

returnbut = ct.CTkButton(main,width=115, height=40,text="Return Books",fg_color="green",bg_color="green",font=Font3,image=returnimage,command=returnbook)
returnbut.place(x=500, y=250)

showbut = ct.CTkButton(main,width=115, height=40,text="Show Books",fg_color="green",bg_color="green",font=Font3,image=bookimage,command=showbook)
showbut.place(x=500, y=350)

logoutbut = ct.CTkButton(main,width=115, height=40,text="Logout",fg_color="green",bg_color="green",font=Font3,image=logoutimage,command=Logout)
logoutbut.place(x=500, y=450)


main.mainloop()