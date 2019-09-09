from tkinter import *
class MyFirstWindow:
    def __init__(self, master):
        self.master = master
        master.title("Simple GUI")
        self.label = Label(master, text="This is my first GUI")
        self.label.pack()
        self.greet_button = Button(master, text="Greet", command=self.greet)
        self.greet_button.pack()
        self.close_button = Button(master, text="Exit", command=master.quit)
        self.close_button.pack()
    def greet(self):
        print("Greeting from window...")

root = Tk()
my_window = MyFirstWindow(root )
root.mainloop() # blocking

print("Goodbye...")

