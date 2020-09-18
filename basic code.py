from tkinter import *

tk = Tk()

string = ""

def rstring(st):
        sts = list(st)
        stf = ""
        for i in range(len(sts)-1,-1,-1):
                stf = stf + sts[i]
        return stf

def insert():
        label = Label(tk, text="fuck yeah 9")
        label.grid(column = 1)


def n(number):
        global string
        string = string + str(number)
        g = e.get() + str(number)
        e.delete(0, 1000)
        e.insert(0, g)


def nadd():
        global string
        string = string + " + "
        g = e.get() + "+"
        e.delete(0, 1000)
        e.insert(0, g)

def nsubtract():
        global string
        string = string + " - "
        g = e.get() + "-"
        e.delete(0, 1000)
        e.insert(0, g)

def nmultiply():
        global string
        string = string + " * "
        g = e.get() + "x"
        e.delete(0, 1000)
        e.insert(0, g)

def ndivide():
        global string
        string = string + " / "
        g = e.get() + "/"
        e.delete(0, 1000)
        e.insert(0, g)

def npower():
        global string
        string = string + "**"
        g = e.get() + "^"
        e.delete(0, 1000)
        e.insert(0, g)

def npoint():
        global string
        string = string + "."
        g = e.get() + "."
        e.delete(0, 1000)
        e.insert(0, g)

def nobracket():
        global string
        string = string + "("
        g = e.get() + "("
        e.delete(0, 1000)
        e.insert(0, g)

def ncbracket():
        global string
        string = string + ")"
        g = e.get() + ")"
        e.delete(0, 1000)
        e.insert(0, g)

def nclear():
        global string
        string = ""
        e.delete(0, 100000)
        

print(string)

def nequal():
        global string
        string = str(eval(string))
        e.delete(0 ,10000)
        e.insert(0, string)




e = Entry(tk, width = 57)
e.grid(row = 1, column = 0, columnspan = 4)



Button(tk, text="0", command=lambda: n(0), padx=50, pady=50).grid(row = 6, column = 1)
Button(tk, text="1", command=lambda: n(1), padx=50, pady=50).grid(row = 5, column = 0)
Button(tk, text="2", command=lambda: n(2), padx=50, pady=50).grid(row = 5, column = 1)
Button(tk, text="3", command=lambda: n(3), padx=50, pady=50).grid(row = 5, column = 2)
Button(tk, text="4", command=lambda: n(4), padx=50, pady=50).grid(row = 4, column = 0)
Button(tk, text="5", command=lambda: n(5), padx=50, pady=50).grid(row = 4, column = 1)
Button(tk, text="6", command=lambda: n(6), padx=50, pady=50).grid(row = 4, column = 2)
Button(tk, text="7", command=lambda: n(7), padx=50, pady=50).grid(row = 3, column = 0)
Button(tk, text="8", command=lambda: n(8), padx=50, pady=50).grid(row = 3, column = 1)
Button(tk, text="9", command=lambda: n(9), padx=50, pady=50).grid(row = 3, column = 2)
Button(tk, text="+", command=nadd, padx=50, pady=50, fg="#3e944a", activeforeground="#3e944a").grid(row = 5, column = 3)
Button(tk, text="-", command=nsubtract, padx=53, pady=50, fg="#3e944a", activeforeground="#3e944a").grid(row = 4, column = 3)
Button(tk, text="x", command=nmultiply, padx=52, pady=50, fg="#3e944a", activeforeground="#3e944a").grid(row = 3, column = 3)
Button(tk, text="/", command=ndivide, padx=54, pady=50, fg="#3e944a", activeforeground="#3e944a").grid(row = 2, column = 3)
Button(tk, text="^", command=npower, padx=48, pady=50).grid(row = 6, column = 0)
Button(tk, text=".", command=npoint, padx=52, pady=50).grid(row = 6, column = 2)
Button(tk, text="=", command=nequal, padx=50, pady=50, bg="#3e944a", fg="white", activebackground="#3e944a", activeforeground="white").grid(row = 6, column = 3)
Button(tk, text="C", command=nclear, padx=50, pady=50, fg="#ff801f", activeforeground="#ff801f").grid(row = 2, column = 0)
Button(tk, text="(", command=nobracket, padx=52, pady=50, fg="#3e944a", activeforeground="#3e944a").grid(row = 2, column = 1)
Button(tk, text=")", command=ncbracket, padx=52, pady=50, fg="#3e944a", activeforeground="#3e944a").grid(row = 2, column = 2)



tk.mainloop()
