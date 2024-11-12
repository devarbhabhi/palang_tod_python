from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("User Information Form")

foo1 = Label(root, text="GUI Programming", font='times', fg='red')
foo1.pack()

foo2 = Message(root, text="This program shows the use of different Tkinter GUI components")
foo2.pack()

Label(root, text="Name:", font='times').pack(anchor=W)
svalue = StringVar()
foo3 = Entry(root, textvariable=svalue)
foo3.pack(anchor=W)

Label(root, text="Hobbies:", font='times').pack(anchor=W)
CheckVar1 = IntVar()
CheckVar2 = IntVar()
CheckVar3 = IntVar()
C1 = Checkbutton(root, text="Music", variable=CheckVar1, onvalue=1, offvalue=0)
C1.pack(anchor=W)
C2 = Checkbutton(root, text="Games", variable=CheckVar2, onvalue=1, offvalue=0)
C2.pack(anchor=W)
C3 = Checkbutton(root, text="Dance", variable=CheckVar3, onvalue=1, offvalue=0)
C3.pack(anchor=W)

Label(root, text="Gender:", font='times').pack(anchor=W)
Radiovar = StringVar()
R1 = Radiobutton(root, text="Male", variable=Radiovar, value="Male")
R1.pack(anchor=W)
R2 = Radiobutton(root, text="Female", variable=Radiovar, value="Female")
R2.pack(anchor=W)

Label(root, text="Age:", font='times').pack(anchor=W)
scalevar = IntVar()
scale = Scale(root, variable=scalevar, orient=HORIZONTAL, from_=0, to=100)
scale.pack(anchor=W)

def function_when_pressed():
    choice = ""
    if CheckVar1.get() == 1:
        choice += " Music "
    if CheckVar2.get() == 1:
        choice += " Games "
    if CheckVar3.get() == 1:
        choice += " Dance "

    messagebox.showinfo("Hello User",
                         "My name is " + svalue.get() + 
                         "\nI am " + Radiovar.get() + 
                         "\nAge is " + str(scalevar.get()) + 
                         "\nMy hobbies are: " + choice)

foo5 = Button(root, text="Print", command=function_when_pressed)
foo5.pack()

root.mainloop()
