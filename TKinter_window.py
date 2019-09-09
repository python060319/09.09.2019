from tkinter import *

root = Tk()
canvas1 = Canvas(root, width=400, height=300)
canvas1.pack()
entry1 = Entry(root)
canvas1.create_window(200, 140, window=entry1)
def getSquareRoot():
    x1 = entry1.get()
    label1 = Label(root, text=float(x1) ** 0.5)
    canvas1.create_window(200, 230, window=label1)
button1 = Button(text='Get the Square Root', command=getSquareRoot)
canvas1.create_window(200, 180, window=button1)
root.mainloop()
