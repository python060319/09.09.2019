from tkinter import *
class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")

        self.total = 0
        self.entered_number = 0
        # IntVar, StrVar
        self.total_label_text = IntVar()
        self.total_label_text.set(self.total)
        self.total_label = Label(master,
            textvariable = self.total_label_text)

        self.label = Label(master, text="Total:")

        self.entry = Entry(master)
        self.add_button = Button(master,
            text="+",command=self.add)
        self.sub_button = Button(master,
            text="-",command=self.add)
        self.reset_button = Button(master,
            text="C",command=self.add)

        # layuot
        self.label.grid(row=0, column=0, sticky=W)
        self.total_label.grid(row=0, column = 1, columnspan=2, sticky=E)
        self.entry.grid(row=1, column=0, columnspan=3)
        self.add_button.grid(row=2, column=0)
        self.sub_button.grid(row=2, column=1)
        self.reset_button.grid(row=2, column=2)

    def add(self):
        self.total += float(self.entry.get())
        self.total_label_text.set(self.total)
root = Tk()
my_window = Calculator(root )
root.mainloop() # blocking

print("Goodbye...")

