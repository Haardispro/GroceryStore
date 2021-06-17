from tkinter import * 

w = Tk()

w.title("List box variations")
w.configure(bg="white")

def okeh():
    listbox.delete(2)

font_tuple = ("Cascadia Code", 20, "bold")
listbox = Listbox(w, height=10,
                  width=20,
                  bg="#1e1e11",
                  font=font_tuple,
                  fg = "white"
                  )


heading = Label(w, text="Food Items", fg="#1e1e11", bg="white", font=font_tuple)
btn = Button(w, text="Delete 2", font=font_tuple, command=okeh)

listbox.insert(1, "Pizza")
listbox.insert(2, "Burger")
listbox.insert(3, "Sandwich")
listbox.insert(4, "Milk Shake")
listbox.insert(5, "Coke")



btn.grid(row=2, column=0)
listbox.grid(row=1, column=0)
heading.grid(row=0, column=0)


w.mainloop()