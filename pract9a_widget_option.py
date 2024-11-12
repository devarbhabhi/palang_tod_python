from tkinter import *
from tkinter.font import Font
root=Tk()
n=Label(root,text="hello World",font='times',fg='black',bg='white')
n.pack()
O=Canvas(root,bg="red",width=500,height=500)
O.pack()
root.mainloop()
