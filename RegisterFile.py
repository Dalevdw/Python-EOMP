from tkinter import *
from tkinter import messagebox
import mysql.connector

mydb = mysql.connector.connect(user='lifechoices', password='@Lifechoices1234',
                               host='127.0.0.1', database='lifechoicesonline',
                               auth_plugin='mysql_native_password')
mycursor = mydb.cursor()


root = Tk()
root.geometry("350x200")
root.title("Register")
root.configure(background="teal")

unlb = Label(root, text="Name:")
unlb.configure(background="teal")
unlb.grid(row=2, column=0)
ussrlb = Label(root, text="Username:")
ussrlb.configure(background="teal")
ussrlb.grid(row=3, column=0)
psslb = Label(root, text="Password")
psslb.configure(background="teal")
psslb.grid(row=4, column=0)
un = Entry(root)
un.grid(row=2, column=2)
usEnt = Entry(root)
usEnt.grid(row=3, column=2)
pssEnt = Entry(root)
pssEnt.grid(row=4, column=2)


def register():
    infoU = un.get(), usEnt.get(), pssEnt.get()
    uCom = "INSERT INTO users(full_name, username, password) VALUES(%s,%s,%s)"

    mycursor.execute(uCom, infoU)
    mydb.commit()
    messagebox.showinfo("Message", "there you go")


    root.destroy()

    unlb.pack()
    un.pack()
    ussrlb.pack()
    usEnt.pack()
    psslb.pack()
    pssEnt.pack()

regBtn = Button(root, text="register", command=register)
regBtn.grid(row=8, column=2)
root.mainloop()
