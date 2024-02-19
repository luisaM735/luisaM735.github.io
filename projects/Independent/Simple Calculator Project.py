# Luisa Martinez
#Calculator Project

import tkinter
import math

root = tkinter.Tk()
root.geometry("312x323")

label = tkinter.Label(text="Calculator")
label.pack()


#Defining button functions
def button(item):
    global expression
    expression += str(item)
    input_text.set(expression)
    
def clear_button():
    global expression
    expression = ""
    input_text.set("")

def equal_button():
    global expression
    result = str(eval(expression))
    input_text.set(result)
    expression = ""
    
expression = ""
input_text = tkinter.StringVar()

def print_text(text):
   Label(win, text=text,font=("typewriter" ,13, "bold")).pack()
 

input_frame = tkinter.Frame(root, width = 312, height = 50, highlightbackground = "Black", highlightthickness = 3)
input_frame.pack(side = "top")

input_field = tkinter.Entry(input_frame, font = ('typewriter', 18, 'bold'), textvariable = input_text, width = 50, bg = "#eee",  justify = "right")
input_field.grid(row = 0, column = 0)
input_field.pack(ipady = 10)

btns_frame = tkinter.Frame(root, width = 312, height = 272.5, bg = "grey")
btns_frame.pack()

clear = tkinter.Button(btns_frame, text = "Clear", fg = "black", width = 10, height = 2, bg = "#eee", cursor = "hand2", command = lambda: clear_button())
clear.grid(row = 0, column = 0, columnspan = 1, padx = 1, pady = 1)

Rparens = tkinter.Button(btns_frame, text = "(", fg = "black", width = 10, height = 2, bg ="#eee", cursor = "hand2", command = lambda: button("("))
Rparens.grid(row = 0,column = 1)

Lparens = tkinter.Button(btns_frame, text = ")", fg = "black", width = 10, height = 2, bg ="#eee", cursor = "hand2", command = lambda: button(")"))
Lparens.grid(row = 0,column = 2)

divide = tkinter.Button(btns_frame, text = "/", fg = "black", width = 10, height = 2, bg = "#eee", cursor = "hand2", command = lambda: button("/"))
divide.grid(row = 0, column = 3, padx = 1, pady = 1)

seven = tkinter.Button(btns_frame, text = "7", fg = "black", width = 10, height = 3, bg = "#fff", cursor = "hand2", command = lambda: button('7'))
seven.grid(row = 1, column = 0, padx = 1, pady = 1)

eight = tkinter.Button(btns_frame, text = "8", fg = "black", width = 10, height = 3, bg = "#fff", cursor = "hand2", command = lambda: button('8'))
eight.grid(row = 1, column = 1, padx = 1, pady = 1)

nine = tkinter.Button(btns_frame, text = "9", fg = "black", width = 10, height = 3, bg = "#fff", cursor = "hand2", command = lambda: button('9'))
nine.grid(row = 1, column = 2, padx = 1, pady = 1)

multiply = tkinter.Button(btns_frame, text = "*", fg = "black", width = 10, height = 3, bg = "#eee", cursor = "hand2", command = lambda: button("*"))
multiply.grid(row = 1, column = 3, padx = 1, pady = 1)

four = tkinter.Button(btns_frame, text = "4", fg = "black", width = 10, height = 3, bg = "#fff", cursor = "hand2", command = lambda: button('4'))
four.grid(row = 2, column = 0, padx = 1, pady = 1)

five = tkinter.Button(btns_frame, text = "5", fg = "black", width = 10, height = 3, bg = "#fff", cursor = "hand2", command = lambda: button('5'))
five.grid(row = 2, column = 1, padx = 1, pady = 1)

six = tkinter.Button(btns_frame, text = "6", fg = "black", width = 10, height = 3, bg = "#fff", cursor = "hand2", command = lambda: button('6'))
six.grid(row = 2, column = 2, padx = 1, pady = 1)

minus = tkinter.Button(btns_frame, text = "-", fg = "black", width = 10, height = 3, bg = "#eee", cursor = "hand2", command = lambda: button("-"))
minus.grid(row = 2, column = 3, padx = 1, pady = 1)

one = tkinter.Button(btns_frame, text = "1", fg = "black", width = 10, height = 3, bg = "#fff", cursor = "hand2", command = lambda: button('1'))
one.grid(row = 3, column = 0, padx = 1, pady = 1)

two = tkinter.Button(btns_frame, text = "2", fg = "black", width = 10, height = 3, bg = "#fff", cursor = "hand2", command = lambda: button('2'))
two.grid(row = 3, column = 1, padx = 1, pady = 1)

three = tkinter.Button(btns_frame, text = "3", fg = "black", width = 10, height = 3, bg = "#fff", cursor = "hand2", command = lambda: button('3'))
three.grid(row = 3, column = 2, padx = 1, pady = 1)

plus = tkinter.Button(btns_frame, text = "+", fg = "black", width = 10, height = 3, bg = "#eee", cursor = "hand2", command = lambda: button("+"))
plus.grid(row = 3, column = 3, padx = 1, pady = 1)

zero = tkinter.Button(btns_frame, text = "0", fg = "black", width = 22, height = 3, bg = "#fff", cursor = "hand2", command = lambda: button("0"))
zero.grid(row = 4, column = 0, columnspan = 2, padx = 1, pady = 1)

point = tkinter.Button(btns_frame, text = ".", fg = "black", width = 10, height = 3, bg = "#eee", cursor = "hand2", command = lambda: button("."))
point.grid(row = 4, column = 2, padx = 1, pady = 1)

equals = tkinter.Button(btns_frame, text = "=", fg = "black", width = 10, height = 3, bg = "#eee", cursor = "hand2", command = lambda: equal_button())
equals.grid(row = 4, column = 3, padx = 1, pady = 1)

root.mainloop()


    

    



    
