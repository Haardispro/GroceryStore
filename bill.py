from tkinter import *

#___Skeleton___#
w = Tk()
w.geometry("1100x600")
w.title("Bill")
w.resizable(width=False, height=False)
w.configure(bg="black")

#__Font__#
font = ("JetBrains Mono", 30, "bold")

#Head
head = Label(w, text="Bill", font=font, bg="black", fg="white")
#Name
name_lab = Label(w, text="Name:", font=font, fg="white", bg="black")
name = Entry(w, width=20, font=font)
#Items bought
#Total Money

#__Buttons__#
print_button = Button(w, text="Print", font=font)

#___Positions___#
head.grid(row=0, column=0)
name_lab.grid(row=1, column=0)
name.grid(row=1, column=1)
#print_button.grid()

w.mainloop()