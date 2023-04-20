from tkinter import *
win = Tk()


lbl = Label(win, text="Gender")
lbl.place(relx=.5, rely=.5)
lbl.pack(anchor="center")
var1 = IntVar()
var2 = IntVar()
r1 = Radiobutton(win, text="Male", variable=var1)
r1.place(x=250, y=20)
r1.pack(anchor="center")
r2 = Radiobutton(win, text="Female", variable=var2)
r2.place(x=250, y=40)
r2.pack(anchor="center")

chk1 = Checkbutton(win, text="100 - 200")
chk1.place(x=250, y=60)
chk1.pack(anchor="center")
chk2 = Checkbutton(win, text="201 - 300")
chk2.place(x=250, y=80)
chk2.pack(anchor="center")
chk3 = Checkbutton(win, text="301 - 400")
chk3.place(x=250, y=100)
chk3.pack(anchor="center")

lbl2 = Label(win, text="Select from list of Fruits")
lbl2.place(x=250, y=150)
lbl2.pack(anchor="center")

lst = Listbox(win, selectmode="Single")
lst.insert(1, "Mango")
lst.insert(2, "Orange")
lst.insert(3, "Apple")
lst.place(x=250, y=200)
lst.pack(anchor="center")


win.geometry("500x400+10+10")
win.maxsize(500, 400)
win.minsize(500, 400)
win.mainloop()