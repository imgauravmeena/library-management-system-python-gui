import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "tsunade106",
    database= "LibraryDb")

cursor = mydb.cursor()

cursor.execute("Create database if not exists LibraryDb")

cursor.execute("Create table if not exists Bookt(BookId int primary key,Title varchar(45),Author varchar(45),Edition int,price int)")

cursor.execute('''Create table if not exists Student(StudentId int primary key,Name varchar(45),Course varchar(45),
Contact int,School varchar(45),Bookid int,Issue_Date date,Return_Date date Null)''')

