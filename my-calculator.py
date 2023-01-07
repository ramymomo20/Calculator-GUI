import tkinter as tk
from calcLogic import *
from tkinter import *
import math

main = tk.Tk()
main.geometry("280x230")
main['background'] = '#4CCD97'
main.title("Scientific Calculator")

# Entry Widgets to show calculations and output
input = Entry(main,width=20,borderwidth=1,relief=RIDGE)
input.grid(pady=7,row=0,sticky="w",padx=20)

output = Entry(main,width=12,borderwidth=1,relief=RIDGE,state='readonly',justify='center')
output.grid(pady=5,row=1,sticky="w",padx=42)

# <====================  Button Operation code starts here.. ==============>
def calc_expression(expression):
    x = Calculator(f'{expression}')
    res = x.calculate
    return str(res)

def clear():
    length = len(input.get())
    try:
        if len(input.get()) <= 1 and input.get()[-1] == '':
            input.delete(0, 'end')
    except IndexError:
        input.insert("end",'')
        
    if len(input.get()) > 1 and input.get()[-1] == ' ':
        input.delete(length-2,'end')
    else:
        input.delete(length-1,'end')

def result():
    if input.get() == "":
        output.config(state=NORMAL)
        output.delete(0,"end")
        output.insert("end","")
        output.config(state='readonly')            
    elif input.get()[0] == "0":
        input.delete(0,"end")
        output.config(state=NORMAL)
        output.delete(0,"end")
        output.insert("end","0")
        output.config(state='readonly')
    else:
        res = input.get()
        output.config(state=NORMAL)
        input.delete(0,"end")
        output.delete(0,"end")
        try:
            output.insert("end",calc_expression(str(res)))
            output.config(state='readonly')
        except:
            input.delete(0,"end")
            output.config(state=NORMAL)
            output.delete(0,"end")
            output.insert("end","invalid input")
            output.config(state='readonly')
            
# <============ end code ================>
class Other: 
    def sinF():
        try:
            if input.get() == "":
                output.config(state=NORMAL)
                output.delete(0,"end")
                output.insert("end","")
                output.config(state='readonly')
            else:
                inp = input.get()
                ans = math.sin(int(inp))

                ans = int(ans) if ans - int(ans) == 0 else str(round(ans,4))

                output.config(state=NORMAL)
                input.delete(0,"end")
                output.delete(0,"end")
                output.insert("end",str(ans))
                output.config(state='readonly')

        except:
            input.delete(0,"end")
            output.config(state=NORMAL)
            output.delete(0,"end")
            output.insert("end","invalid input")
            output.config(state='readonly')    

    def cosF():
        try:
            if input.get() == "":
                output.config(state=NORMAL)
                output.delete(0,"end")
                output.insert("end","")
                output.config(state='readonly')
            else:
                inp = input.get()
                ans = math.cos(int(inp))

                ans = int(ans) if ans - int(ans) == 0 else str(round(ans,4))

                output.config(state=NORMAL)
                input.delete(0,"end")
                output.delete(0,"end")
                output.insert("end",str(ans))
                output.config(state='readonly')

        except:
            input.delete(0,"end")
            output.config(state=NORMAL)
            output.delete(0,"end")
            output.insert("end","invalid input")
            output.config(state='readonly') 

    def tanF():
        try:
            if input.get() == "":
                output.config(state=NORMAL)
                output.delete(0,"end")
                output.insert("end","")
                output.config(state='readonly')
            else:
                inp = input.get()
                ans = math.tan(int(inp))

                ans = int(ans) if ans - int(ans) == 0 else str(round(ans,4))

                output.config(state=NORMAL)
                input.delete(0,"end")
                output.delete(0,"end")
                output.insert("end",str(ans))
                output.config(state='readonly')

        except:
            input.delete(0,"end")
            output.config(state=NORMAL)
            output.delete(0,"end")
            output.insert("end","invalid input")
            output.config(state='readonly')
            
# <============= Button Design Code starts here.. ==================>
clear = Button(main, text="⌫",width=5,command=clear,bg="blue",fg="white",borderwidth=1,relief=RIDGE)
clear.grid(row=0,sticky="e",padx=155,pady=5)


clearall = Button(main,text="C",width=2,command=lambda:input.delete(0,"end"),bg="red",fg="white",borderwidth=1,relief=RIDGE)
clearall.grid(row=0,sticky="e",padx=115,pady=5)



result = Button(main,text="=",width=7,command=result,bg="red",fg="white",borderwidth=1,relief=RIDGE)
result.grid(row=1,sticky="w",padx=130)



leftParenth = Button(text="(",width=2,command=lambda:input.insert("end","("),borderwidth=1,relief=RIDGE)
leftParenth.grid(row=2,sticky="w",padx=15,pady=5)

rightParenth = Button(text=")",width=2,command=lambda:input.insert("end",")"),borderwidth=1,relief=RIDGE)
rightParenth.grid(row=2,sticky="w",padx=45,pady=5)

sqrt = Button(text="√x",width=2,command=lambda:input.insert("end","√"),borderwidth=1,relief=RIDGE)
sqrt.grid(row=2,sticky="w",padx=75,pady=5)

square = Button(text="^",width=2,command=lambda:input.insert("end","^ "),borderwidth=1,relief=RIDGE)
square.grid(row=2,sticky="w",padx=105,pady=5)

plus = Button(main,text="+",width=2,command=lambda:input.insert("end"," + "),borderwidth=1,relief=RIDGE)
plus.grid(row=2,sticky="e",padx=155,pady=5)


#####################
fact = Button(text="x!",width=2,command=lambda:input.insert("end","!"),borderwidth=1,relief=RIDGE)
fact.grid(row=2,sticky="e",padx=125,pady=5)
#####################


nine = Button(text="9",width=2,command=lambda:input.insert("end","9"),borderwidth=1,relief=RIDGE)
nine.grid(row=3,sticky="w",padx=15,pady=5)

eight = Button(text="8",width=2,command=lambda:input.insert("end","8"),borderwidth=1,relief=RIDGE)
eight.grid(row=3,sticky="w",padx=45,pady=5)

seven = Button(main,text="7",width=2,command=lambda:input.insert("end","7"),borderwidth=1,relief=RIDGE)
seven.grid(row=3,sticky="w",padx=75,pady=5)

six = Button(text="6",width=2,command=lambda:input.insert("end","6"),borderwidth=1,relief=RIDGE)
six.grid(row=3,sticky="w",padx=105,pady=5)

minus = Button(main,text="-",width=2,command=lambda:input.insert("end"," - "),borderwidth=1,relief=RIDGE)
minus.grid(row=3,sticky="e",padx=155,pady=5)


#####################
sine = Button(text="sin",width=2,command=Other.sinF,borderwidth=1,relief=RIDGE)
sine.grid(row=3,sticky="e",padx=125,pady=5)
#####################


five = Button(text="5",width=2,command=lambda:input.insert("end","5"),borderwidth=1,relief=RIDGE)
five.grid(row=4,sticky="w",padx=15,pady=5)

four = Button(main,text="4",width=2,command=lambda:input.insert("end","4"),borderwidth=1,relief=RIDGE)
four.grid(row=4,sticky="w",padx=45,pady=5)

three = Button(text="3",width=2,command=lambda:input.insert("end","3"),borderwidth=1,relief=RIDGE)
three.grid(row=4,sticky="w",padx=75,pady=5)

two = Button(text="2",width=2,command=lambda:input.insert("end","2"),borderwidth=1,relief=RIDGE)
two.grid(row=4,sticky="w",padx=105,pady=5)

multiply = Button(main,text="*",width=2,command=lambda:input.insert("end"," * "),borderwidth=1,relief=RIDGE)
multiply.grid(row=4,sticky="e",padx=155,pady=5)


#####################
cosine = Button(text="cos",width=2,command=Other.cosF,borderwidth=1,relief=RIDGE)
cosine.grid(row=4,sticky="e",padx=125,pady=5)
#####################


one = Button(main,text="1",width=2,command=lambda:input.insert("end","1"),borderwidth=1,relief=RIDGE)
one.grid(row=5,sticky="w",padx=15,pady=5)

zero = Button(text="0",width=2,command=lambda:input.insert("end","0"),borderwidth=1,relief=RIDGE)
zero.grid(row=5,sticky="w",padx=45,pady=5)

double_zero = Button(text="00",width=2,command=lambda:input.insert("end","00"),borderwidth=1,relief=RIDGE)
double_zero.grid(row=5,sticky="w",padx=75,pady=5)

dot = Button(main,text=".",width=2,command=lambda:input.insert("end","."),borderwidth=1,relief=RIDGE)
dot.grid(row=5,sticky="w",padx=105,pady=5)

divide = Button(main,text="/",width=2,command=lambda:input.insert("end"," / "),borderwidth=1,relief=RIDGE)
divide.grid(row=5,sticky="e",padx=155,pady=5)


#####################
tangent = Button(text="tan",width=2,command=Other.tanF,borderwidth=1,relief=RIDGE)
tangent.grid(row=5,sticky="e",padx=125,pady=5)
#####################

if __name__ == '__main__':
    main.mainloop()