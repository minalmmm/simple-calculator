import tkinter
from tkinter import *
import tkinter as tk

# Python program to create a simple GUI 
# calculator using Tkinter 
 
# import everything from tkinter module 
from tkinter import *
 
# globally declare the expression variable gi
expression = "" 
 
 
# Function to update expression 
# in the text entry box 
def press(num): 
    # point out the global expression variable 
    global expression 
 
    # concatenation of string 
    expression = expression + str(num) 
 
    # update the expression by using set method 
    equation.set(expression) 
 
 
# Function to evaluate the final expression 
def equalpress(): 
    # Try and except statement is used 
    # for handling the errors like zero 
    # division error etc. 
 
    # Put that code inside the try block 
    # which may generate the error 
    try: 
 
        global expression 
 
        # eval function evaluate the expression 
        # and str function convert the result 
        # into string 
        total = str(eval(expression)) 
 
        equation.set(total) 
 
        # initialize the expression variable 
        # by empty string 
        expression = "" 
 
    # if error is generate then handle 
    # by the except block 
    except: 
 
        equation.set(" error ") 
        expression = "" 
 
 
# Function to clear the contents 
# of text entry box 
def clear(): 
    global expression 
    expression = "" 
    equation.set("") 
 
 
# Driver code 
if __name__ == "__main__":  


#create main window
    
        import tkinter as tk
     
        r = tk.Tk()
        r.title('project 1: MANUAL CALCULATOR')
        r.iconbitmap('icon.ico')
#r.geometry('270x300')
        r.maxsize(width=290,height=300)
        r.minsize(width=290,height=300)
        r.configure(background="light blue")

# StringVar() is the variable class 
    # we create an instance of this class 
        equation = StringVar()


#create label
        lb1 = Label(r, 
                  text = " CALCULATOR-BY MINAL    ",bg='yellow',fg='dark blue',bd=10)
        lb1.grid(row=2,columnspan=6,ipadx=70,ipady=10)
                                            
#create entry box

        ent= Entry(r,text=   "                     ", textvariable=equation) 
        ent.grid(row=3,columnspan=6,ipadx=90,ipady=10)


#create buttons in calculator

        button1 = Button(r, text=' 1 ', fg='white', bg='black', 
                     height=2, width=8,command=lambda: press(1)) 
        button1.grid(row=5, column=0,rowspan=1,columnspan=1) 
 
        button2 = Button(r, text=' 2 ', fg='white', bg='black', 
                     height=2, width=8,command=lambda: press(2))  
        button2.grid(row=5, column=1,rowspan=1,columnspan=1) 
 
        button3 = Button(r, text=' 3 ', fg='white', bg='black', 
                     height=2, width=8,command=lambda: press(3))  
        button3.grid(row=5, column=2,rowspan=1,columnspan=1) 

        clear =  Button(r, text=' clear ', fg='white', bg='black', 
                     height=2, width=8,command=clear)
        clear.grid(row=5, column=3,rowspan=1,columnspan=1) 


        button4 = Button(r, text=' 4 ', fg='white', bg='black', 
                     height=2, width=8,command=lambda: press(4))
        button4.grid(row=6, column=0,rowspan=1,columnspan=1) 
 
        button5 =  Button(r, text=' 5 ', fg='white', bg='black', 
                     height=2, width=8,command=lambda: press(5)) 
        button5.grid(row=6, column=1,rowspan=1,columnspan=1) 
 
        button6 =  Button(r, text=' 6 ', fg='white', bg='black', 
                     height=2, width=8,command=lambda: press(6)) 
        button6.grid(row=6, column=2,rowspan=1,columnspan=1) 

        plus = Button(r, text= "+", fg='white', bg='black', 
                     height=2, width=8,command=lambda: press("+"))
        plus.grid(row=6, column=3,rowspan=1,columnspan=1)

        button7 =  Button(r, text=' 7 ', fg='white', bg='black', 
                     height=2, width=8,command=lambda: press(7))
        button7.grid(row=7, column=0,rowspan=1,columnspan=1) 
 
        button8 =  Button(r, text=' 8 ', fg='white', bg='black', 
                     height=2, width=8,command=lambda: press(8)) 
        button8.grid(row=7, column=1,rowspan=1,columnspan=1) 
 
        button9 =  Button(r, text=' 9 ', fg='white', bg='black', 
                     height=2, width=8,command=lambda: press(9)) 
        button9.grid(row=7, column=2,rowspan=1,columnspan=1) 

        minus =  Button(r, text="-", fg='white', bg='black', 
                     height=2, width=8,command=lambda: press("-")) 
        minus.grid(row=7, column=3,rowspan=1,columnspan=1)

 
        button0 =  Button(r, text=' 0 ', fg='white', bg='black', 
                     height=2, width=8,command=lambda: press(0))
        button0.grid(row=8, column=0,rowspan=1,columnspan=1) 
 
        divide =  Button(r, text=' / ', fg='white', bg='black', 
                     height=2, width=8,command=lambda: press("/")) 
        divide.grid(row=8, column=1,rowspan=1,columnspan=1)

        brkt2= Button(r, text=' ( ', fg='white', bg='black', 
                     height=2, width=8,command=lambda: press('('))
        brkt2.grid(row=9, column=1,rowspan=1,columnspan=1)

        multiply =  Button(r, text=' * ', fg='white', bg='black', 
                     height=2, width=8,command=lambda: press("*")) 
        multiply.grid(row=8, column=3,rowspan=1,columnspan=1)
 
        Decimal= Button(r, text=' . ', fg='white', bg='black', 
                     height=2, width=8,command=lambda: press("."))
        Decimal.grid(row=9, column=0,rowspan=1,columnspan=1) 

        double_zero= Button(r, text=' 00 ', fg='white', bg='black', 
                     height=2, width=8,command=lambda: press("00"))
        double_zero.grid(row=8, column=2,rowspan=1,columnspan=1)

        brkt1= Button(r, text=' ) ', fg='white', bg='black', 
                     height=2, width=8,command=lambda: press(')'))
        brkt1.grid(row=9, column=2,rowspan=1,columnspan=1)

        equal =  Button(r, text=' = ', fg='white', bg='black', 
                     height=2, width=8,command=equalpress) 
        equal.grid(row=9, column=3,rowspan=1,columnspan=1)

        r.mainloop()