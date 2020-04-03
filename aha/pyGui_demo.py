from tkinter import *
import random

'''
First_k = Tk()
First_k.title('这是第一个窗口的标题')
w = Label(First_k, text="hello world")
w.pack()
First_k.mainloop()
'''

'''
Grid布局
class App:

    def __init__(self, master):
        self.master = master
        self.initaha()

    def initaha(self):
        e = Entry(relief=SUNKEN, font=('Courier Nes', 24), width=25)
        e.pack(side=TOP, pady=10)
        p = Frame(self.master)
        p.pack(side=TOP)
        name = ('0', '1', '2', '3', '4', '5', '6', '7', '8'
                , '9', '+', '-', '*', '/', '.', '=')
        for i in range(len(name)):
            b = Button(p, text=name[i], font=('Verdana', 20), width=6)
            b.grid(row=i // 4, column=i % 4)


root = Tk()
root.title('Grid布局')
App(root)
root.mainloop()
'''

'''
class App:

    def __init__(self, master):
        self.master = master
        self.ahaWidgets()
    def ahaWidgets(self):
        books = ('疯狂python讲义', 'java', 'kotlin',
                 'swift', 'ruby')
        for i in range(len(books)):
            ct = [random.randrange(256) for x in range(3)]
            grayness = int(round(0.299*ct[0] + 0.587*ct[1] + 0.114*ct[2]))
            bg_color = '#%02x%02x%02x' % tuple(ct)
            lb = Label(self.master, text=books[i], fg='White' if grayness < 125 else 'Black', bg=bg_color)
            lb.place(x=20, y=36+i*36, width=180, height=30)


root = Tk()
root.title('place布局')
root.geometry('250x250+30+30')
App(root)
root.mainloop()
'''

from tkinter import *


class App:
    def __init__(self, master):
        self.master = master
        self.initWidgets()
        self.expr = None

    def initWidgets(self):
        self.show = Label(relief=SUNKEN, font=('Courier New', 24), width=25,
                          bg='white', pady=10)
        self.show.pack(side=TOP, pady=10)
        p = Frame(self.master)
        p.pack(side=TOP)
        names = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '-', '*', '/', '.', '=')
        for i in range(len(names)):
            b = Button(p, text=names[i], font=('Verdana', 20), width=6)
            b.grid(row=i // 4, column=i % 4)
            b.bind('<Button-1>', self.click)
            if b['text'] == '=': b.bind('<Double-1>', self.clean)

    def click(self, event):
        if (event.widget['text'] in ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.')):
            self.show['text'] = self.show['text'] + event.widget['text']
        elif(event.widget['text'] in ('+', '-', '*', '/')):
            if self.expr is None:
                self.expr = self.show['text'] + event.widget['text']
            else:
                self.expr = self.expr + self.show['text'] + event.widget['text']
            self.show['text'] = ''
        elif(event.widget['text'] == '=' and self.expr is not None):
            self.expr = self.expr + self.show['text']
            print(self.expr)
            self.show['text'] = str(eval(self.expr))
            self.expr = None

    def clean(self, event):
        self.expr = None
        self.show['text'] = ''


if __name__ == '__main__':
    root = Tk()
    root.title('计算器')
    App(root)
    root.mainloop()
