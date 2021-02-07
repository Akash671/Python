
""" 
@author.    : AKASH KUMAR
@institute. : MIT Institute Moradabad India
@branch.    : Computer Science & Information Technology
@work as.   : Software Devlope & Machine Learning Engineer
@website.   : https://medium.com/@akashsaininasa
@github.    : https://github.com/Akash671
""" 




import tkinter as tk
from tkinter import*
import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='dbms_mini_project',
                                         user='root',
                                         password='')
    root=tk.Tk()
    root.geometry("400x420")
    root.configure(bg="skyblue")
    root.title(".......Student Login......")
    Label(root,text="Enter username and password",width=25,bg="powderblue").pack()
    Label(root,text="Application Version 2.7.1",width=25,bg="pink").pack(side=BOTTOM)
    Label(root,text="username", width=15,bg="powderblue").place(x=90,y=80)
    Label(root,text="password", width=15,bg="powderblue").place(x=90,y=120)
    def clear():
     user_name.set("")
     password.set("")
    user_name = StringVar()  # User name variable
    password = StringVar()  # Password variable
    Entry(root, textvariable=user_name).place(x=220,y=80)
    Entry(root, textvariable=password, show='*').place(x=220,y=120)
    def login():
     username=user_name.get()
     Password=password.get()
    
     username_list=["st_1810101","st_1810102","st_1810103","st_1810104","st_1810105","st_1810106","st_1810107","st_1810108",
                   "st_1810109","st_18101010"] 
     user_password_list=["a@123","ab@123","abc@123","abcd@123","abcde@123","aa@123","Akash@1996",
                        "Hitman@123","9@123","102123"]
    #c1=0
    #c2=0
     us=0
     pas=0
     for i in username_list:
        if username==i:
            us=i
           # c1=1
            break
     for j in user_password_list:
           if Password==j:
               pas=j
            #   c2=1
               break
            #print("ok")
     if us==username and pas==Password:
        import tkinter as tk
        wind1=tk.Tk()
        wind1.geometry("400x500")
        wind1.configure(bg="violet")
        wind1.title(".......student info......")
        Label(wind1,text="MIT Moradabad",width=25,bg="powderblue").pack()
       # Label(wind1,text="Application Version 2.7.1",width=25,bg="pink").pack(side=BOTTOM)
        Label(wind1,text="Student No.", width=15,bg="powderblue").place(x=80,y=60)
        Label(wind1,text="Student Name", width=15,bg="powderblue").place(x=80,y=100)
        Label(wind1,text="Course Name", width=15,bg="powderblue").place(x=80,y=140)
        Label(wind1,text="Stream Name", width=15,bg="powderblue").place(x=80,y=180)
        Label(wind1,text="Section", width=15,bg="powderblue").place(x=80,y=220)
        Label(wind1,text="Year", width=15,bg="powderblue").place(x=80,y=260)
        Label(wind1,text="Duration", width=15,bg="powderblue").place(x=80,y=300)
        Label(wind1,text="Session", width=15,bg="powderblue").place(x=80,y=340)
        Label(wind1,text="Age", width=15,bg="powderblue").place(x=80,y=380)
        Label(wind1,text="Gender", width=15,bg="powderblue").place(x=80,y=420)

        #database.................
        sql_select_Query = "select * from "+us
        cursor = connection.cursor()
        cursor.execute(sql_select_Query)
        records = cursor.fetchall()
        data=[]
        k=0
        for row in records:
           #if k==0:
           #     k=1
           #     continue
           #if k==1:
            Label(wind1,text=row[0], width=15,bg="powderblue").place(x=220,y=60)
            Label(wind1,text=row[1], width=15,bg="powderblue").place(x=220,y=100)
            Label(wind1,text=row[2], width=15,bg="powderblue").place(x=220,y=140)
            Label(wind1,text=row[3], width=15,bg="powderblue").place(x=220,y=180)
            Label(wind1,text=row[4], width=15,bg="powderblue").place(x=220,y=220)
            Label(wind1,text=row[5], width=15,bg="powderblue").place(x=220,y=260)
            Label(wind1,text=row[6], width=15,bg="powderblue").place(x=220,y=300)
            Label(wind1,text=row[7], width=15,bg="powderblue").place(x=220,y=340)
            Label(wind1,text=row[8], width=15,bg="powderblue").place(x=220,y=380)
            Label(wind1,text=row[9], width=15,bg="powderblue").place(x=220,y=420)
            break




        wind1.mainloop()
         


     else:
        import tkinter as tk
        error_window=tk.Tk()
        error_window.geometry("250x220")
        error_window.configure(bg="skyblue")


        error_window.title(".......Error......")

       # Label(error_window,text="invalid username or password", width=15,bg="powderblue").place(x=20,y=100)
       
        Button(error_window,text="invalid username or password",width=25,bg="powderblue",bd=4).place(x=30,y=60)
        
        def destroy():
         #conn.close()
           error_window.destroy()


        Button(error_window,text="Ok",width=5,bg="powderblue",bd=4,command=destroy).place(x=100,y=100)
        error_window.resizable(0,0)
        error_window.mainloop()
    def clear():
     user_name.set("")
     password.set("")

    Button(root, text='Clear',width=6,bg="powderblue",bd=4, command=clear).place(x=220,y=160)
    Button(root,text="Login",width=6,bg="powderblue",bd=4,command=login).place(x=150,y=160)
    root.resizable(0,0)
    root.mainloop()


except Error as e:
    print("Error reading data from MySQL table", e)
