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

def n0():
        global string
        string = string + "0"
        g = e.get() + "0"
        e.delete(0, 1000)
        e.insert(0, g)

def n1():
        global string
        string = string + "1"
        g = e.get() + "1"
        e.delete(0, 1000)
        e.insert(0, g)

def n2():
        global string
        string = string + "2"
        g = e.get() + "2"
        e.delete(0, 1000)
        e.insert(0, g)

def n3():
        global string
        string = string + "3"
        g = e.get() + "3"
        e.delete(0, 1000)
        e.insert(0, g)

def n4():
        global string
        string = string + "4"
        g = e.get() + "4"
        e.delete(0, 1000)
        e.insert(0, g)

def n5():
        global string
        string = string + "5"
        g = e.get() + "5"
        e.delete(0, 1000)
        e.insert(0, g)

def n6():
        global string
        string = string + "6"
        g = e.get() + "6"
        e.delete(0, 1000)
        e.insert(0, g)
def n7():
        global string
        string = string + "7"
        g = e.get() + "7"
        e.delete(0, 1000)
        e.insert(0, g)

def n8():
        global string
        string = string + "8"
        g = e.get() + "8"
        e.delete(0, 1000)
        e.insert(0, g)

def n9():
        global string
        string = string + "9"
        g = e.get() + "9"
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
        e.delete(0, 100000)
        

print(string)

def nequal():
        global string
        string = str(eval(string))
        e.delete(0 ,10000)
        e.insert(0, string)




e = Entry(tk, width = 57)
e.grid(row = 1, column = 0, columnspan = 4)



Button(tk, text="0", command=n0, padx=50, pady=50).grid(row = 6, column = 1)
Button(tk, text="1", command=n1, padx=50, pady=50).grid(row = 5, column = 0)
Button(tk, text="2", command=n2, padx=50, pady=50).grid(row = 5, column = 1)
Button(tk, text="3", command=n3, padx=50, pady=50).grid(row = 5, column = 2)
Button(tk, text="4", command=n4, padx=50, pady=50).grid(row = 4, column = 0)
Button(tk, text="5", command=n5, padx=50, pady=50).grid(row = 4, column = 1)
Button(tk, text="6", command=n6, padx=50, pady=50).grid(row = 4, column = 2)
Button(tk, text="7", command=n7, padx=50, pady=50).grid(row = 3, column = 0)
Button(tk, text="8", command=n8, padx=50, pady=50).grid(row = 3, column = 1)
Button(tk, text="9", command=n9, padx=50, pady=50).grid(row = 3, column = 2)
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


