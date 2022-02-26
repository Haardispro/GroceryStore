from tkinter import *

s = Tk()
s.geometry("500x400")
s.resizable(width=False, height=False)
s.configure(bg="#282828")
s.title("Grocery Store")

def inventory():
    import inventory

def bill():
    import bill

font = ("Cascadia Code", 20, "bold")

heading = Label(s, text="Grocery store", font=font, fg="white", bg="#282828")
heading.grid(row=0, column=0, padx=150, pady=30)

inv = Button(s, text="Open Inventory", font=font, command=inventory)
inv.grid(row=1, column=0, padx=50, pady=30)
bill = Button(s, text="Open Billing software",font=font, command=bill)
bill.grid(row=2, column=0, padx=50, pady=30)

#update     
s.mainloop()
