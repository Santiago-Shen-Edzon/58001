from tkinter import *
class MyWindow:
    def __init__(self, win):

        self.lbl1 = Label(win, text = "My Full Name")
        self.lbl1.place(x = 200, y = 50)
        self.fname = Label(win, text = "Enter Given Name:")
        self.fname.place(x = 100, y = 80)
        self.mname = Label(win, text = "Enter Middle Name:")
        self.mname.place(x = 100, y = 110)
        self.lname = Label(win, text = "Enter Last Name:")
        self.lname.place(x = 100, y = 140)
        self.flname = Label(win, text = "My Full Name is:")
        self.flname.place(x = 100, y = 180)
        self.txt1 = Entry(win, bd=1)
        self.txt1.place(x = 300, y = 80)
        self.txt2 = Entry(win, bd=1)
        self.txt2.place(x = 300, y = 110)
        self.txt3 = Entry(win, bd=1)
        self.txt3.place(x = 300, y = 140)
        self.txt4 = Entry(win, bd=3)
        self.txt4.place(x = 300, y = 180, width = 200)
        self.btnsadd = Button(win, text = "Show Full Name", command=self.show)
        self.btnsadd.place(x = 200, y = 220)

    def show(self):
        self.txt4.delete(0, 'end')
        num1 = str(self.txt1.get())
        num2 = str(self.txt2.get())
        num3 = str(self.txt3.get())
        fullname = num1 + " " + num2 + " " + num3
        self.txt4.insert(END, str(fullname))


window = Tk()
mywin = MyWindow(window)
window.geometry("550x400+10+10")
window.title("Midterm Exam Problem 2")
window.mainloop()