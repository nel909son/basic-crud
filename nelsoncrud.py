import sys
import time
from tkinter import *
from PIL import ImageTk,Image
import sqlite3


root = Tk()

root.title("tester")

root.geometry("300x300")

path = "/Users/nelson/Desktop/python/"

root.iconbitmap(path+"icons/Boss.ico")

def clearFields():
    fNameEn.delete(0,END)
    lNameEn.delete(0,END)
    addressEn.delete(0,END)
    dobEn.delete(0,END)
    imageEn.delete(0,END)

#add functions to add record and display records

def addRecord():
    #connect to database
    #use placeholder variables and a dictionary
    conn=sqlite3.connect(path+"address_book.db")
    try:
        c=conn.cursor()
        c.execute("insert into contacts values (?,?,?,?,?,?)",
                  (fNameEn.get(),lNameEn.get(),addressEn.get(),cityEn.get(),selected.get(),int(zipCodeEn.get()) ))
        conn.commit()
        print ("one record added successfully")

    except:
         print("error in operation")
         conn.rollback()
    conn.close()
    clearFields()
def show_selected_record(event):
    clearFields()
    for selection in tvStudent.selection():
        item =tvStudent.item(selection)
        global id
        fName,lName,address,city,state,zipCode= item["values"][0:6]
        fNameEn.insert(0,fName)
        lNameEn.insert(0,lName)
        addressEn.insert(0,address)
        cityEn.insert(0, city)
        stateOp.setvar(state)
        zipCodeEn.insert(0, zipCode)
    return id

selected = StringVar()

fNameLb=Label(root,text="First Name")
lNameLb=Label(root,text="Last Name")
addressLb=Label(root,text="Address")
dobLb=Label(root,text="DOB")
imageLb=Label(root,text="Profile Picture")

fNameEn = Entry(root)
lNameEn = Entry(root)
addressEn = Entry(root)
dobEn = Entry(root)
imageEn = Entry()


saveBtn = Button(root,text="save", command=addRecord)
clearBtn = Button(root,text="clear",command=clearFields)

fNameLb.grid(row=0, column=0)
lNameLb.grid(row=1, column=0)
addressLb.grid(row=2, column=0)
dobLb.grid(row=3, column=0)
imageLb.grid(row=4, column=0)

fNameEn.grid(row=0, column=1)
lNameEn.grid(row=1, column=1)
addressEn.grid(row=2, column=1)
dobEn.grid(row=3, column=1)
imageEn.grid(row=4, column=1)


saveBtn.grid(row=7, column=0)
clearBtn.grid(row=7,column=1)

root.mainloop()
