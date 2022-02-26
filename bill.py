from tkinter import *
import subprocess


#___Skeleton___#
w = Tk()
w.geometry("1100x600")
w.title("Bill")
w.resizable(width=False, height=False)
w.configure(bg="#282828")

#__Functions__#
def printbill():
    s = open("bill.txt", "w+")
    s.write("Name: " + name.get())
    s.write("\n")
    s.write("Amount Paid: " + paid.get())
    s.write("\n")
    s.write("Items Bought: " + item.get())
    s.write("\n")
    
    """
    for i in range(10):
        s.write("Hello\n")
    """
    s.close()
    #subprocess.call('lp "bill.txt"')


#__Font__#
font = ("Cascadia Code", 30, "bold")

#Head
head = Label(w, text="Bill", font=font, bg="#282828", fg="white")
#Name
name_lab = Label(w, text="Name:", font=font, fg="white", bg="#282828")
name = Entry(w, width=20, font=font)


#Total Money Paid
paid_lab = Label(w, text="Amount Paid:", font=font, fg="white", bg="#282828")
paid = Entry(w, width=20, font=font)

#Items Bought
item_total = Label(w, text="Items Bought:", font=font, fg="white", bg="#282828")
item = Entry(w, width=20, font=font)

#__Buttons__#
print_button = Button(w, text="Print", font=font, command=printbill)

#___Positions___#
head.grid(row=0, column=0, padx=10, pady=10)
name_lab.grid(row=1, column=0, padx=10, pady=10)
name.grid(row=1, column=1, padx=10, pady=10)
paid_lab.grid(row=2, column=0, padx=10, pady=10)
paid.grid(row=2, column=1, padx=10, pady=10)
item_total.grid(row=3, column=0, pady=10, padx=10)
item.grid(row=3, column=1, padx=10, pady=10)
print_button.grid(row=4, column=0, padx=10, pady=10)

w.mainloop()
