from tkinter import *
from tkinter import messagebox
from pymongo import MongoClient
from random import randint

import pymongo

# Connect to MongoDB
try:
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client["student_management"]
    print("Connected to MongoDB")
except Exception as e:
    print("Database connection Error:", e)
    messagebox.showerror("Error", "Database Connection Error")
    sys.exit(1)


def add_student():
    def add_query():
        uid = uid_entry.get()
        name = name_entry.get()
        email = email_entry.get()
        batch = batch_entry.get()
        mobile = mobile_entry.get()

        if not (uid and name and email and batch):
            messagebox.showwarning("Warning", "All fields are compulsory (Except Mobile)")
            return

        student = {
            'UID': uid,
            'NAME': name,
            'EMAIL': email,
            'BATCH': batch,
            'MOBILE': mobile
        }

        if not mobile and db.students.count_documents({'UID': uid}, limit=1) == 0:
            result = db.students.insert_one(student)
        elif mobile and db.students.count_documents({'UID': uid}, limit=1) == 0:
            result = db.students.insert_one(student)
        else:
            messagebox.showwarning("Error", "Student Already Exists")
            return

        new_win.destroy()
        messagebox.showinfo("Add Student", "Student Added")

    new_win = Toplevel(root)
    new_win.geometry('400x400')
    new_win.title("Add Students")

    Label(new_win, text="UID").place(x=10, y=50)
    uid_entry = Entry(new_win, bd=7)
    uid_entry.place(x=100, y=50)

    Label(new_win, text="Name").place(x=10, y=100)
    name_entry = Entry(new_win, bd=7)
    name_entry.place(x=100, y=100)

    Label(new_win, text="Email").place(x=10, y=150)
    email_entry = Entry(new_win, bd=7)
    email_entry.place(x=100, y=150)

    Label(new_win, text="Batch").place(x=10, y=200)
    batch_entry = Entry(new_win, bd=7)
    batch_entry.place(x=100, y=200)

    Label(new_win, text="Mobile").place(x=10, y=250)
    mobile_entry = Entry(new_win, bd=7)
    mobile_entry.place(x=100, y=250)

    submit_button = Button(new_win, text="Submit", command=add_query)
    submit_button.place(x=120, y=350)


def delete_student():
    def delete():
        uid = uid_entry.get()
        if not uid:
            messagebox.showwarning("Warning", "Enter a Valid UID")
            return

        if db.students.count_documents({'UID': uid}, limit=1) == 0:
            messagebox.showwarning("Error", "Student Does Not Exist")
            return
        else:
            db.students.delete_one({'UID': uid})

        new_win.destroy()
        messagebox.showinfo("Delete Student", "Student Deleted")

    new_win = Toplevel(root)
    new_win.geometry('400x350')
    new_win.title("Delete Student")

    Label(new_win, text="UID").place(x=10, y=50)
    uid_entry = Entry(new_win, bd=5)
    uid_entry.place(x=100, y=50)

    delete_button = Button(new_win, text="Delete Entry", command=delete)
    delete_button.place(x=120, y=200)


def update_student():
    def update():
        uid = uid_entry.get()
        name = name_entry.get()
        email = email_entry.get()
        batch = batch_entry.get()
        mobile = mobile_entry.get()

        if not uid:
            messagebox.showwarning("Warning", "Enter a Valid UID")
            return

        if db.students.count_documents({'UID': uid}, limit=1) == 0:
            messagebox.showwarning("Error", "Student Does Not Exist")
            return

        if name:
            db.students.update_one({"UID": uid}, {"$set": {'NAME': name}})
        if email: 
            db.students.update_one({"UID": uid}, {"$set": {'EMAIL': email}})
        if batch:
            db.students.update_one({"UID": uid}, {"$set": {'BATCH': batch}})
        if mobile:
            db.students.update_one({"UID": uid}, {"$set": {'MOBILE': mobile}})

        new_win.destroy()
        messagebox.showinfo("Update Student", "Student Updated")

    new_win = Toplevel(root)
    new_win.geometry('400x400')
    new_win.title("Update Student")

    Label(new_win, text="UID").place(x=10, y=50)
    uid_entry = Entry(new_win, bd=7)
    uid_entry.place(x=100, y=50)

    Label(new_win, text="Name").place(x=10, y=100)
    name_entry = Entry(new_win, bd=7)
    name_entry.place(x=100, y=100)

    Label(new_win, text="Email").place(x=10, y=150)
    email_entry = Entry(new_win, bd=7)
    email_entry.place(x=100, y=150)

    Label(new_win, text="Batch").place(x=10, y=200)
    batch_entry = Entry(new_win, bd=7)
    batch_entry.place(x=100, y=200)

    Label(new_win, text="Mobile").place(x=10, y=250)
    mobile_entry = Entry(new_win, bd=7)
    mobile_entry.place(x=100, y=250)

    submit_button = Button(new_win, text="Submit", command=update)
    submit_button.place(x=120, y=350)


def display_students():
    new_win = Toplevel(root)
    new_win.geometry('400x400')
    new_win.title("Student Details")

    Label(new_win, text="UID").grid(row=0, column=0)
    Label(new_win, text="Name").grid(row=0, column=1)
    Label(new_win, text="Email").grid(row=0, column=2)
    Label(new_win, text="Batch").grid(row=0, column=3)
    Label(new_win, text="Mobile").grid(row=0, column=4)

    i = 1
    for student in db.students.find():
        Label(new_win, text=student.get('UID', 'N/A')).grid(row=i, column=0)
        Label(new_win, text=student.get('NAME', 'N/A')).grid(row=i, column=1)
        Label(new_win, text=student.get('EMAIL', 'N/A')).grid(row=i, column=2)
        Label(new_win, text=student.get('BATCH', 'N/A')).grid(row=i, column=3)
        Label(new_win, text=student.get('MOBILE', 'N/A')).grid(row=i, column=4)
        i += 1



root = Tk()
root.geometry('400x350')
root.title("Student Management System")

add_button = Button(root, text='Add New Student', command=add_student)
delete_button = Button(root, text='Delete Student Entry', command=delete_student)
update_button = Button(root, text='Update Student Info', command=update_student)
show_button = Button(root, text='Show Student Details', command=display_students)

add_button.place(x=100, y=100)
delete_button.place(x=100, y=150)
update_button.place(x=100, y=200)
show_button.place(x=100, y=250)

root.mainloop()
