from tkinter import *
from math import *

#Create The Root
root = Tk()
root.title("My First Calcualor")

#Create decimal done

decimal_done = "n"

#Create the entry field

e = Entry(root, width=35, borderwidth=5)

#Place the entry Field

e.grid(row=0, column=0, ipady=30, ipadx=5, columnspan=3)

#The functions


    #If you click a number, it indentifies which number (Parameter), gets the current number in the var current, deletes the current number, and adds the current number + the parameter (In strings).
def number_click(number):
    try:
        current = e.get()
        e.delete(0, END)
        e.insert(0, str(current) + str(number))
    except:
        e.insert(0, "ERROR")

    #Adds a decimalpoint, gets the current number in the var current, deletes the current number, and adds the current number + decimal point. The decimal_done makes sure that there is just 1 decimal.
def decimal():
    global decimal_done
    if decimal_done == "n":
        decimal_done = "y"
        current = e.get()
        e.delete(0, END)
        e.insert(0, str(current) + ".")        

    #Gets the current number, and puts it in the global var first_number. Then it creates the global, math, and adds addition to it.
def add():
    try:
        global first_number
        first_number = float(e.get())
        global math
        math = "+"
        e.delete(0, END)
        global decimal_done
        decimal_done = "n"
    except:
        e.insert(0, "ERROR")

    #Gets the current number, and puts it in the global var first_number. Then it creates the global, math, and adds subtraction to it.
def subtract():
    try:
        global first_number
        first_number = float(e.get())
        global math
        math = "-"
        e.delete(0, END)
        global decimal_done
        decimal_done = "n"
    except:
        e.insert(0, "ERROR")

    #Gets the current number, and puts it in the global var first_number. Then it creates the global, math, and adds multiplication to it.
def multiply():
    try:
        global first_number
        first_number = float(e.get())
        global math
        math = "*"
        e.delete(0, END)
        global decimal_done
        decimal_done = "n"
    except:
        e.insert(0, "ERROR")

    #Gets the current number, and puts it in the global var first_number. Then it creates the global, math, and adds division to it.
def divide():
    try:
        global first_number
        first_number = float(e.get())
        global math
        math = "/"
        e.delete(0, END)
        global decimal_done
        decimal_done = "n"
    except:
        e.insert(0, "ERROR")

    #Gets the current number, squares it, and puts that in the var square_num. Deletes the current number and inserts the squared number.
def square():
    try:
        number = float(e.get())
        square_num = number ** 2
        e.delete(0, END)
        e.insert(0, square_num)
    except:
        e.insert(0, "ERROR")

    #Gets the current number, and puts it in the global var first_number. Then it creates the global, math, and adds the exponents to it.
def exponent():
    try:
        global first_number
        first_number = float(e.get())
        global math
        math = "**"
        e.delete(0, END)
        global decimal_done
        decimal_done = "n"
    except:
        e.insert(0, "ERROR")

    #Gets the current number, finds the squareroot, and puts that in the var squareroot_num. Deletes the current number and inserts the number.
def squareroot():
    try:
        number = float(e.get())
        squareroot_num = sqrt(number)
        e.delete(0, END)
        e.insert(0, squareroot_num)
    except:
        e.insert(0, "ERROR")
    
    #Gets the current number, and puts it in the global var first_number. Then it creates the global, math, and adds the exponentroot to it.
def exponentroot():
    try:
        global first_number
        first_number = float(e.get())
        global math
        math = "//"
        e.delete(0, END)
        global decimal_done
        decimal_done = "n"
    except:
        e.insert(0, "ERROR")

def result():
    second_number = float(e.get())#gets the second number
    e.delete(0, END)#deletes the current numbers
    try:
        if math == "+":#If the global var math is + 
            e.insert(0, first_number + second_number)#Adds the first number and second number, and adds that to the entry field
        elif math == "-":#If the global var math is -
            e.insert(0, first_number - second_number)#Subtracts the first number and second number, and adds that to the entry field
        elif math == "*":#If the global var math is *
            e.insert(0, first_number * second_number)#Multiplies the first number and second number, and adds that to the entry field
        elif math == "/":#If the global var math is /
            e.insert(0, first_number / second_number)#Divides the first number and second number, and adds that to the entry field
        elif math == "**":#If the global var math is **
            e.insert(0, first_number ** second_number)#Gets the first number to the power of the second number, and adds that to the entry field
        elif math == "//":#If the gloval var math is // 
            e.insert(0, first_number ** (1./second_number))#Gets the 2nd number-root of the first number, and adds that to the entry field
    except:
        e.insert(0, "ERROR")

def clear():
    try:
        e.delete(0, END)
        global decimal_done
        decimal_done = "n"
    except:
        e.insert(0, "ERROR")

    


#Creating the buttons

button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: number_click(1))
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: number_click(2))
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: number_click(3))
button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: number_click(4))
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: number_click(5))
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: number_click(6))
button_7 = Button(root, text="7", padx=40, pady=20, bg="red", command=lambda: number_click(7))
button_8 = Button(root, text="8", padx=40, pady=20, bg="red", command=lambda: number_click(8))
button_9 = Button(root, text="9", padx=40, pady=20, bg="red", command=lambda: number_click(9))
button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: number_click(0))
button_decimal = Button(root, text=".", padx=42, pady=20, command=decimal)

button_equals = Button(root, text="=", padx=40, pady=20, command=result)
button_add = Button(root, text="+", padx=39, pady=20, command=add)
button_subtract = Button(root, text="-", padx=40, pady=20, command=subtract)
button_multiply = Button(root, text="x", padx=40, pady=20, command=multiply)
button_divide = Button(root, text="÷", padx=39, pady=20, command=divide)
button_clear = Button(root, text="AC", padx=35, pady=35, command=clear)
button_square = Button(root, text="x²", padx=39, pady=20, command=square)
button_exponent = Button(root, text="xⁿ", padx=38, pady=20, command=exponent)
button_squareroot = Button(root, text="√", padx=40, pady=20, command=squareroot)
button_root = Button(root, text="ⁿ√", padx=36, pady=20, command=exponentroot)


#Place the buttons

#Row 3 (Numbers)
button_1.grid(row=4, column=0)
button_2.grid(row=4, column=1)
button_3.grid(row=4, column=2)

#Row2 (Numbers)
button_4.grid(row=3, column=0)
button_5.grid(row=3, column=1)
button_6.grid(row=3, column=2)

#Row 1 (Numbers)
button_7.grid(row=2, column=0)
button_8.grid(row=2, column=1)
button_9.grid(row=2, column=2)

#Row 4 (Numbers + decimal)
button_0.grid(row=5, column=0)
button_decimal.grid(row=5, column=1)

#Equals
button_equals.grid(row=5, column=2)

#Operations(Row 1)
button_square.grid(row=1, column=0)
button_exponent.grid(row=1, column=1)
button_squareroot.grid(row=1, column=2)
button_root.grid(row=1, column=3)

#Operations (Column 3)
button_add.grid(row=2, column=3)
button_subtract.grid(row=3, column=3)
button_multiply.grid(row=4, column=3)
button_divide.grid(row=5, column=3)

#Clear
button_clear.grid(row=0, column = 3)



#Mainloop

root.mainloop()
