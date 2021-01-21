from tkinter import *

def student():
    import Studfile
    Studfile.mainloop()


def admin():
    import Adminfile
    Adminfile.mainloop()


def staff():
    import StaffFile
    StaffFile.mainloop()


def register():
    import RegisterFile
    RegisterFile.mainloop()


window = Tk()
window.geometry("400x500")
window.title("Register")
window.configure(background="teal")

stud_btn = Button(window, text="Students", command=student)
stud_btn.grid(row=2, column=1)

admin_btn = Button(window, text="Admin", command=admin)
admin_btn.grid(row=3, column=1)

staff_btn = Button(window, text="Staff", command=staff)
staff_btn.grid(row=4, column=1)

reg_btn = Button(window, text="Register", command=register)
reg_btn.grid(row=5, column=1)


window.mainloop()
