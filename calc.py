from tkinter import *
import math
import tkinter.messagebox
root = Tk()
root.title("GUI SCIENTIFIC CALCULATOR BY ASHUTOSH PANDIT")
root.configure(bg="powder blue")
root.resizable(width=False, height=False)
root.geometry("480x560")
calc = Frame(root)
calc.grid()

class calc1():
    def __init__(self):
        self.total = 0
        self.current = ""
        self.input_value = True
        self.check_sum = False
        self.op = ""
        self.result = False

    def numen(self, num1):
        self.result = False
        firstnum = display.get()
        secondnum = str(num1)
        if self.input_value:
            self.current = secondnum
            self.input_value = False
        else:
            if secondnum == '.':
                if secondnum in firstnum:
                    return
            self.current = firstnum+secondnum
        self.display1(self.current)

    def sum_of_total(self):
        self.result = True
        self.current = float(self.current)
        if self.check_sum == True:
            self.valid_function()
        else:
            self.total = float(display.get())

    def display1(self, value):
        display.delete(0, END)
        display.insert(0, value)

    def valid_function(self):
        if self.op == "add":
            self.total += self.current
        if self.op == "sub":
            self.total -= self.current
        if self.op == "mul":
            self.total *= self.current
        try:
            if self.op == "div":
                self.total /= self.current
        except:
            self.total = "Error"
        if self.op == "mod":
            self.total %= self.current
        self.input_value = True
        self.check_sum = False
        self.display1(self.total)

    def operation(self, op):
        self.current = float(self.current)
        if self.check_sum:
            self.valid_function()
        elif not self.result:
            self.total = self.current
            self.input_value = True
        self.check_sum = True
        self.op = op
        self.result = False

    def clear_entry(self):
        self.result = False
        self.current = "0"
        self.display1(0)
        self.input_value = True

    def all_clear_entry(self):
        self.clear_entry()
        self.total = 0

    def mathsPM(self):
        self.result = False
        self.current = -(float(display.get()))
        self.display1(self.current)

    def squared(self):
        self.result = False
        self.current = math.sqrt(float(display.get()))
        self.display1(self.current)

    def cos(self):
        self.result = False
        self.current = math.cos(math.radians(float(display.get())))
        self.display1(self.current)

    def cosh(self):
        self.result = False
        self.current = math.cosh(math.radians(float(display.get())))
        self.display1(self.current)

    def tanh(self):
        self.result = False
        self.current = math.tanh(math.radians(float(display.get())))
        self.display1(self.current)

    def sin(self):
        self.result = False
        self.current = math.sin(math.radians(float(display.get())))
        self.display1(self.current)

    def sinh(self):
        self.result = False
        self.current = math.sinh(math.radians(float(display.get())))
        self.display1(self.current)

    def tan(self):
        self.result = False
        self.current = math.tan(math.radians(float(display.get())))
        self.display1(self.current)

    def log(self):
        self.result = False
        self.current = math.log(float(display.get()))
        self.display1(self.current)

    def exp(self):
        self.result = False
        self.current = math.exp(float(display.get()))
        self.display1(self.current)

    def pi(self):
        self.result = False
        self.current = math.pi
        self.display1(self.current)

    def tau(self):
        self.result = False
        self.current = math.tau
        self.display1(self.current)

    def e(self):
        self.result = False
        self.current = math.e
        self.display1(self.current)

    def acosh(self):
        self.result = False
        self.current = math.acosh(float(display.get()))
        self.display1(self.current)

    def asinh(self):
        self.result = False
        self.current = math.asinh(float(display.get()))
        self.display1(self.current)

    def radians(self):
        self.result = False
        self.current = math.radians(float(display.get()))
        self.display1(self.current)

    def factorial(self):
        self.result = False
        self.current = math.factorial(float(display.get()))
        self.display1(self.current)

    def degree(self):
        self.result = False
        self.current = math.degrees(float(display.get()))
        self.display1(self.current)

    def log2(self):
        self.result = False
        self.current = math.log2(float(display.get()))
        self.display1(self.current)

    def log10(self):
        self.result = False
        self.current = math.log10(float(display.get()))
        self.display1(self.current)

    def log1p(self):
        self.result = False
        self.current = math.log1p(float(display.get()))
        self.display1(self.current)

added_value = calc1()

display = Entry(calc, font="lucida 20 bold", bg="sky blue", fg="red", bd=30, width=28, justify=RIGHT)
display.grid(row=0, column=0, columnspan=4, pady=1)
display.insert(0, "0")

num = "789456123"
i = 0
btn = []
for j in range(2, 5):
    for k in range(3):
        btn.append(Button(calc, width=6, height=2, font="lucida 20 bold", bd=4, bg="yellow", text=num[i]))
        btn[i].grid(row=j, column=k, pady=1)
        btn[i]["command"] = lambda x = num[i]: added_value.numen(x)
        i += 1

Button(calc, text="C", width=6, height=2, font="lucida 20 bold", bd=4, bg="light coral", command=added_value.clear_entry
       ).grid(row=1, column=0, pady=1)
Button(calc, text="CE", width=6, height=2, font="lucida 20 bold", bd=4, bg="light coral", command=added_value.all_clear_entry
       ).grid(row=1, column=1, pady=1)
Button(calc, text="√", width=6, height=2, font="lucida 20 bold", bd=4, bg="pink", command=added_value.squared).grid(
    row=1, column=2, pady=1)
Button(calc, text="+", width=6, height=2, font="lucida 20 bold", bd=4, bg="pink", command=lambda: added_value.operation("add")
       ).grid(row=1, column=3, pady=1)
Button(calc, text="-", width=6, height=2, font="lucida 20 bold", bd=4, bg="pink", command=lambda: added_value.operation("sub")
       ).grid(row=2, column=3, pady=1)
Button(calc, text="*", width=6, height=2, font="lucida 20 bold", bd=4, bg="pink", command=lambda: added_value.operation("mul")
       ).grid(row=3, column=3, pady=1)
Button(calc, text="/", width=6, height=2, font="lucida 20 bold", bd=4, bg="pink", command=lambda: added_value.operation("div")
       ).grid(row=4, column=3, pady=1)

Button(calc, text="0", width=6, height=2, font="lucida 20 bold", bd=4, bg="pink", command=lambda: added_value.numen(0)
               ).grid(row=5, column=0, pady=1)
Button(calc, text=".", width=6, height=2, font="lucida 20 bold", bd=4, bg="pink", command=lambda: added_value.numen(".")
       ).grid(row=5, column=1, pady=1)
Button(calc, text=chr(177), width=6, height=2, font="lucida 20 bold", bd=4, bg="pink", command=added_value.mathsPM).grid(
    row=5, column=2, pady=1)
Button(calc, text="=", width=6, height=2, font="lucida 20 bold", bd=4, bg="pink", command=added_value.sum_of_total).grid(
    row=5, column=3, pady=1)

Button(calc, text="π", width=6, height=2, font="lucida 20 bold", bd=4, bg="pink", command=added_value.pi).grid(
    row=1, column=4, pady=1)
Button(calc, text="sin", width=6, height=2, font="lucida 20 bold", bd=4, bg="spring green", command=added_value.sin).grid(
    row=1, column=5, pady=1)
Button(calc, text="cos", width=6, height=2, font="lucida 20 bold", bd=4, bg="spring green", command=added_value.cos).grid(
    row=1, column=6, pady=1)
Button(calc, text="tan", width=6, height=2, font="lucida 20 bold", bd=4, bg="spring green", command=added_value.tan).grid(
    row=1, column=7, pady=1)

Button(calc, text="2π", width=6, height=2, font="lucida 20 bold", bd=4, bg="pink", command=added_value.tau).grid(
    row=2, column=4, pady=1)
Button(calc, text="sinh", width=6, height=2, font="lucida 20 bold", bd=4, bg="spring green", command=added_value.sinh).grid(
    row=2, column=5, pady=1)
Button(calc, text="cosh", width=6, height=2, font="lucida 20 bold", bd=4, bg="spring green", command=added_value.cosh).grid(
    row=2, column=6, pady=1)
Button(calc, text="tanh", width=6, height=2, font="lucida 20 bold", bd=4, bg="spring green", command=added_value.tanh).grid(
    row=2, column=7, pady=1)

Button(calc, text="e", width=6, height=2, font="lucida 20 bold", bd=4, bg="pink", command=added_value.e).grid(
    row=3, column=4, pady=1)
Button(calc, text="asinh", width=6, height=2, font="lucida 20 bold", bd=4, bg="spring green", command=added_value.asinh).grid(
    row=3, column=5, pady=1)
Button(calc, text="acosh", width=6, height=2, font="lucida 20 bold", bd=4, bg="spring green", command=added_value.acosh).grid(
    row=3, column=6, pady=1)
Button(calc, text="deg", width=6, height=2, font="lucida 20 bold", bd=4, bg="spring green", command=added_value.degree).grid(
    row=3, column=7, pady=1)

Button(calc, text="%", width=6, height=2, font="lucida 20 bold", bd=4, bg="pink", command=lambda: added_value.operation("mod")
       ).grid(row=4, column=4, pady=1)
Button(calc, text="log", width=6, height=2, font="lucida 20 bold", bd=4, bg="khaki", command=added_value.log).grid(
    row=4, column=5, pady=1)
Button(calc, text="log2", width=6, height=2, font="lucida 20 bold", bd=4, bg="khaki", command=added_value.log2).grid(
    row=4, column=6, pady=1)
Button(calc, text="log10", width=6, height=2, font="lucida 20 bold", bd=4, bg="khaki", command=added_value.log10).grid(
    row=4, column=7, pady=1)

Button(calc, text="Exp", width=6, height=2, font="lucida 20 bold", bd=4, bg="pink", command=added_value.exp).grid(
    row=5, column=4, pady=1)
Button(calc, text="log1p", width=6, height=2, font="lucida 20 bold", bd=4, bg="khaki", command=added_value.log1p).grid(
    row=5, column=5, pady=1)
Button(calc, text="radians", width=6, height=2, font="lucida 20 bold", bd=4, bg="khaki", command=added_value.radians).grid(
    row=5, column=6, pady=1)
Button(calc, text="factorial", width=6, height=2, font="lucida 20 bold", bd=4, bg="khaki", command=added_value.factorial).grid(
    row=5, column=7, pady=1)
lbl=Label(calc, text="scientific calculator", font="lucida 20 bold", bg="turquoise", bd=30, width=25, justify=CENTER)
lbl.grid(row=0, column=4, columnspan=4)

######################## MENU ########################
def iexit():
    iexit=tkinter.messagebox.askyesno("scientific calculator", "conform if you want to exit")
    if iexit>0:
        root.destroy()
        return
def scientific():
    root.resizable(width=False, height=False)
    root.geometry("980x560")
def standard():
    root.resizable(width=False, height=False)
    root.geometry("480x560")

menu=Menu(calc)
f1=Menu(menu, tearoff=0)
menu.add_cascade(label="file",  menu=f1)
f1.add_command(label="standard", command=standard)
f1.add_command(label="scientific", command=scientific)
f1.add_separator()
f1.add_command(label="Exit", command=iexit)

f2=Menu(menu, tearoff=0)
menu.add_cascade(label="edit", menu=f2)
f2.add_command(label="cut")
f2.add_command(label="copy")
f2.add_separator()
f2.add_command(label="Paste")

f3=Menu(menu, tearoff=0)
menu.add_cascade(label="help", menu=f3)
f3.add_command(label="view help")

root.configure(menu=menu)
root.mainloop()
