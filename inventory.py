from tkinter import *  
from tkinter import messagebox

#___Layout___#
w = Tk()
w.title("Grocery Store")
w.configure(bg="black")
w.geometry("1300x700")
w.resizable(height=False, width=False)
w.title("Inventory")

#___Functions___#

#Adding Functions
def btn():
    if item_name.get() == "":
        messagebox.showwarning("Warning", "Empty value not accepted!")
    else:
        listbox.insert(END, item_name.get())
def btn1():
    if amount.get() == "":
        messagebox.showwarning("Warning", "Empty value not accepted!")
    else:
        listbox1.insert(END, amount.get())
def btn2():
    if value.get() == "":
        messagebox.showwarning("Warning", "Empty value not accepted!")
    else:
        listbox2.insert(END, value.get())

#Add everthing at once
def add_all():
    if item_name.get() == "" or amount.get() == "" or value.get() == "":
        messagebox.showwarning("Warning", "Empty va|lue not accepted")
    else:
        listbox.insert(END, item_name.get())
        listbox1.insert(END, amount.get())
        listbox2.insert(END, value.get())

#Clear all
def clear_all():
    listbox.delete(0,'end')
    listbox1.delete(0,'end')
    listbox2.delete(0,'end')

#Deleting functions
def delete_item(): 
    listbox.delete(ANCHOR)
def delete_item1(): 
    listbox1.delete(ANCHOR) 
def delete_item2(): 
    listbox2.delete(ANCHOR)

#___Fonts___#
f1 = ("JetBrains Mono", 20, "bold")
list_f1 = ("JetBrains Mono", 15, "bold")

#___Column Name___#
a = Label(w, text="Item Name", font=f1, fg='White', bg="black")
b = Label(w, text="Number of items", font=f1, fg='White', bg="black")
c = Label(w, text="Value(for 1 item)", font=f1, fg='White', bg="black")


#___Listbox___#
listbox = Listbox(w, width=20,
                  height=15,
                  bg="white",
                  fg="black",
                  font=list_f1
                 )
listbox1 = Listbox(w, width=20,
                  height=15,
                  bg="white",
                  fg="black",
                  font=list_f1

                 )

listbox2 = Listbox(w, width=20,
                  height=15,
                  bg="white",
                  fg="black",
                  font=list_f1

                 )


#___Entries___#
global item_name, amount, value
item_name = Entry(w, width=15, font=f1)
amount = Entry(w, width=15, font=f1)
value = Entry(w, width=15, font=f1)

#___Buttons___#

#Add all
ad = Button(w, text="Add all", font=list_f1, width=20, command=add_all)
#Clear all
cl = Button(w, text="Clear all", font=list_f1, width=20, command=clear_all)
#Add
add = Button(w, text="Add", font=list_f1, command=btn, width=20)
add1 = Button(w, text="Add", font=list_f1, command=btn1, width=20)
add2 = Button(w, text="Add", font=list_f1, command=btn2, width=20)
#Delete
delt = Button(w, text="Delete", font=list_f1, command=delete_item, width=20)
delt1 = Button(w, text="Delete", font=list_f1, command=delete_item1, width=20)
delt2 = Button(w, text="Delete", font=list_f1, command=delete_item2, width=20)

#____Grid positions____#

#Entry Positions
item_name.grid(row=3, column=0, padx=100, pady=10)
amount.grid(row=3, column=1, padx=100, pady=10)
value.grid(row=3, column=2, padx=100, pady=10)
#Listbox positions
listbox.grid(row=2, column=0)
listbox1.grid(row=2, column=1)
listbox2.grid(row=2, column=2)
#Add Button positions
add.grid(row=4, column=0, pady=5)
add1.grid(row=4, column=1, pady=5)
add2.grid(row=4, column=2, pady=5)
#Delete positions
delt.grid(row=5, column=0, pady=5)
delt1.grid(row=5, column=1, pady=5)
delt2.grid(row=5, column=2, pady=5)
#Column Names positions
a.grid(row=1, column=0, padx=60, pady=10)
b.grid(row=1, column=1, padx=60, pady=10)
c.grid(row=1, column=2, padx=60, pady=10)
#Add all position
ad.place(x=765, y=650)
#Clear all position
cl.place(x=320, y=650)


w.mainloop() 