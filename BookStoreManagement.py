from tkinter import *
import mysql.connector as m


def connect():
    try:
        bookdata = m.connect(host="localhost", user='root', password='manager', database="BookStore")
        cursor = bookdata.cursor()
        cursor.execute("create table if not exists BookInfo(id int primary key Auto_increment , Title varchar(100) , Auther varchar(100) , year int , ISBN int)")
        bookdata.commit()
        bookdata.close()
    except m.Error as e:
        print("Error connecting to the database:", e)


def Insert():
    try:
        Side_Frame.delete(0, END)
        bookdata = m.connect(host="localhost", user='root', password='manager', database="BookStore")
        cursor = bookdata.cursor()
        cursor.execute("insert into BookInfo values(NULL,%s,%s,%s,%s)", (Title.get(), Auther.get(), Year.get(), ISBN.get()))
        bookdata.commit()
        bookdata.close()
        Side_Frame.insert(END, Title.get(), Auther.get(), Year.get(), ISBN.get())
        l["text"] = Title.get() + " Book is added successfully."
    except m.Error as e:
        print("Error inserting data into the database:", e)


def delete():
    try:
        Side_Frame.delete(0, END)
        bookdata = m.connect(host="localhost", user="root", password="manager", database="BookStore")
        cursor = bookdata.cursor()
        cursor.execute("delete from BookInfo where title=%s or isbn=%s", (Title.get(), ISBN.get()))
        if cursor.rowcount > 0:
            bookdata.commit()
            Side_Frame.insert(END, Title.get(), ISBN.get())
            l["text"] = Title.get() + " Book is deleted successfully."
        else:
            l["text"] = "Book not found."
        bookdata.close()
    except m.Error as e:
        print("Error deleting data from the database:", e)


def update():
    try:
        Side_Frame.delete(0, END)
        bookdata = m.connect(host="localhost", user="root", password="manager", database="BookStore")
        cursor = bookdata.cursor()
        cursor.execute("update BookInfo set year=%s where ISBN=%s", (Year.get(), ISBN.get()))
        if cursor.rowcount > 0:
            bookdata.commit()
            Side_Frame.insert(END, Title.get(), Auther.get(), Year.get(), ISBN.get())
            l["text"] = Title.get() + " Book is successfully updated."
        else:
            l["text"] = "Book not found."
        bookdata.close()
    except m.Error as e:
        l["text"]="Error retrieving data from the database:"

def Showall():
    try:
        bookdata = m.connect(host="localhost", user="root", password="manager", database="BookStore")
        cursor = bookdata.cursor()
        cursor.execute("SELECT * FROM BookInfo")
        rows = cursor.fetchall()
        Side_Frame.delete(0, END)  # Clear the existing items from the listbox
        if len(rows) > 0:
            for row in rows:
                Side_Frame.insert(END, f"Title: {row[1]}, Author: {row[2]}, Year: {row[3]}, ISBN: {row[4]}")
        else:
            l["text"] = "No books found in the database."
    except m.Error as e:
        l["text"]="Error retrieving data from the database:"

connect()

window=Tk(className='Book Store Managment')
#window.title("Book Store")
window.geometry("1550x800+0+0")

labletitle = Label(window,text="BOOK STORE MANAGEMENT",bd=20,relief=RIDGE,bg='lightblue',fg='black',font=("times new roman",40,"bold"),padx=2,pady=4)
labletitle.pack(side=TOP , fill=X)

# Dataframe ########
DataFrame=Frame(window,bd=15,relief=RIDGE,padx=30,bg="lightgreen")
DataFrame.place(x=0,y=120,width=1360,height=550)

DataFrame1=LabelFrame(DataFrame,bd=10,relief=RIDGE,padx=20,text="Book Information",bg="pink",fg="red",font=("times new roman",15,"bold"))
DataFrame1.place(x=0,y=5,width=650,height=500)

DataFrame2=LabelFrame(DataFrame,bd=10,relief=RIDGE,padx=20,text="Display",fg="red",font=("times new roman",15,"bold"))
DataFrame2.place(x=660,y=5,width=620,height=500)

# Button 
b1= Button(DataFrame1,text="Add",font=("arial",12,"bold"),fg="black",bg="orange",command=Insert)
b1.place(x=0,y=370,width=90,height=50)

b2= Button(DataFrame1,text="Delete",font=("arial",12,"bold"),fg="black",bg="orange",command=delete)
b2.place(x=110,y=370,width=90,height=50)

b3= Button(DataFrame1,text="Update",font=("arial",12,"bold"),fg="black",bg="orange", command=update)
b3.place(x=220,y=370,width=90,height=50)

b4= Button(DataFrame1,text="show all",font=("arial",12,"bold"),fg="black",bg="orange",command=Showall)
b4.place(x=340,y=370,width=90,height=50)

b5= Button(DataFrame1,text="Close",font=("arial",12,"bold"),fg="black",bg="red",command=window.destroy)
b5.place(x=470,y=370,width=90,height=50)

# Label
l1= Label(DataFrame1,text="Title :: ",font=("times new roman",15,"bold"),fg="black",padx=2)
l1.grid(row=0,column=0)

l2= Label(DataFrame1,text="Auther :: ",font=("times new roman",15,"bold"),fg="black",padx=1)
l2.grid(row=10,column=0)

l3= Label(DataFrame1,text="Year :: ",font=("times new roman",15,"bold"),fg="black",padx=2)
l3.grid(row=20,column=0)

l4= Label(DataFrame1,text="ISBN :: ",font=("times new roman",15,"bold"),fg="black",padx=2)
l4.grid(row=30,column=0)

# Entry
Title=StringVar()
e1= Entry(DataFrame1,textvariable=Title,font=("times new roman",12,"bold"),bd=3,bg="white",relief=RIDGE,width=50)
e1.grid(row=5,column=0)

Auther=StringVar()
e2= Entry(DataFrame1,textvariable=Auther,font=("times new roman",12,"bold"),bd=3,bg="white",relief=RIDGE,width=50)
e2.grid(row=15,column=0)

Year=StringVar()
e3= Entry(DataFrame1,textvariable=Year,font=("times new roman",12,"bold"),bd=3,bg="white",relief=RIDGE,width=50)
e3.grid(row=25,column=0)

ISBN=StringVar()
e4= Entry(DataFrame1,textvariable=ISBN,font=("times new roman",12,"bold"),bd=3,bg="white",relief=RIDGE,width=50)
e4.grid(row=35,column=0)

Side_Frame=Listbox(DataFrame2,bd=4,relief=RIDGE,bg="white")
Side_Frame.place(x=0,y=0,width=560,height=300)

sb=Scrollbar(Side_Frame,orient=VERTICAL)
sb.pack(side=RIGHT,fill=Y)

l= Label(DataFrame2,padx=2,width=70,bg="red",fg="white",font=("times new roman",10,"bold"))
l.place(x=0,y=340)


window.mainloop()