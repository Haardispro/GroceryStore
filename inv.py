from tkinter import * 
import sqlite3

w = Tk()
w.title("Inventory")
w.resizable(width=False, height=False)
w.config(bg="#282828")

fonts = ("Cascadia Code", 15)

def add():
    uin1 = item_name.get()
    uin2 = int(number.get())
    uin3 = int(mass.get())
    uin4 = int(cost.get())
    item_name.delete(0, END)
    number.delete(0, END)
    con = sqlite3.connect("main.db")
    cur = con.cursor()
    try:
        cur.execute("""CREATE TABLE data(
                item_name text,  
                number real,
                mass real, 
                cost real
                )""")
    except:
        sqlite3.OperationalError()
    cur.execute("INSERT INTO data VALUES (?, ?, ?, ?)", (uin1, uin2, uin3, uin4))
    
    #cur.execute("DELETE FROM data ORDER BY item_name")
    #cur.execute("DELETE FROM data ORDER BY number")
    for row in cur.execute("SELECT * FROM data ORDER BY number"):
        print(row)
    con.commit()
    con.close()

def delete():
    con=sqlite3.connect("main.db")
    cur=con.cursor()
    cur.execute("DELETE FROM data")
    con.commit()
    con.close()
    all_data.delete("1.0", "end")

def view():
    all_data.delete("1.0", "end")
    con=sqlite3.connect("main.db")
    cur=con.cursor()
    for row in cur.execute("SELECT * FROM data ORDER BY item_name"):
        all_data.insert(END, row)
        all_data.insert(END, "\n")
    con.commit()
    con.close()
        
#lb = Listbox(w,)
#        width=20,
#        height=10, 
#        font=fonts
#        )

label1 = Label(w, text="Item Name: \n(should be <5 letters)", font=fonts, bg="#282828", fg="white")
label2 = Label(w, text="Number: ", font=fonts, bg="#282828", fg="white")
label3 = Label(w, text="Mass(kg): ", font=fonts, bg="#282828", fg="white")
label4 = Label(w, text="Cost(Rs.): ", font=fonts, bg="#282828", fg="white")
label5 = Label(w, text="Item: Num: Mass: Cost:                  ", font=fonts, fg="white", bg="#282828")
item_name = Entry(w, width=20, font=fonts)
number = Entry(w, width=20, font=fonts)
mass = Entry(w, width=20, font=fonts)
cost = Entry(w, width=20, font=fonts)

submit = Button(w, text="Add", font=fonts, command=add)
delete_all = Button(w, text="Delete all", font=fonts, command=delete)
view_records = Button(w, text="View all records", command=view, font=fonts)
all_data = Text(w, font=fonts, fg="white", bg="#282828", width=40, height=20)

#Positions

label1.grid(row=0, column=0, padx=10, pady=10)
label2.grid(row=1, column=0, padx=10, pady=10)
label3.grid(row=2, column=0, padx=10, pady=10)
label4.grid(row=3, column=0, padx=10, pady=10)
label5.grid(row=7, column=1, padx=10, pady=10)
item_name.grid(row=0, column=1, padx=10, pady=10)
number.grid(row=1, column=1, padx=10, pady=10)
mass.grid(row=2, column=1, padx=10, pady=10)
cost.grid(row=3, column=1, padx=10, pady=10)
submit.grid(row=4, column=1, padx=10, pady=10)
delete_all.grid(row=5, column=1, padx=10, pady=10)
view_records.grid(row=6, column=1, padx=10, pady=10)
all_data.grid(row=8, column=1, padx=10, pady=10)

w.mainloop()
