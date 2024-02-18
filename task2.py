#calculator 
from tkinter import *
import ast
root = Tk()
i = 0
def get_number(num):
    global i
    display.insert(i, num)
    i+=1
def get_operation(operator):
    global i
    length = len(operator)
    display.insert(i, operator)
    i+=length
def clear_all():
    display.delete(0, END)
def calculate():
    try:
        entire_string = display.get()
        node = ast.parse(entire_string, mode="eval")
        result = eval(compile(node, "<string>", "eval"))
        clear_all()
        display.insert(END, result)
    except:
        clear_all()
        display.insert(0, 'Error')

def backspace():
    entire_string = display.get()
    if len(entire_string):
       new_string = entire_string[:-1]
       clear_all()
       display.insert(END, new_string)
    else:
        clear_all()
        display.insert(0, "")

def decimal():
    global i
    display.insert(i, '.')
    i+=1

display = Entry(root)
display.grid(row=1, columnspan=6)

#while loop
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
counter = 0
for x in range(3):
    for y in range(3):
        button_text = numbers[counter]
        button = Button(root, text=button_text,width=4, height=4, command=lambda text=button_text: get_number(text))
        button.grid(row=x+2, column=y)
        counter+=1
#number 0 print
button = Button(root, text="0", width=4, height=4, command=lambda text=button_text: get_number(0))
button.grid(row=5, column=1)

operations= ['+', '-', '*', '/', '%', '3.14', '2', '(', ')', '*']
count = 0
for x in range(4):
       for y in range(3):
           if count < len(operations):
               operation = operations[count]
               button = Button(root, text=operation, width=4, height=4, command=lambda text=operation: get_operation(text))
               button.grid(row=x+2, column=y+3)
               count+=1

button= Button(root, text="AC", width=4, height=4, command=clear_all)
button.grid(row=5, column=0)

button= Button(root, text=".", width=4, height=4, command=decimal)
button.grid(row=5, column=2)

button= Button(root, text="<--", width=4, height=4, command=backspace)
button.grid(row=5, column=4)

button= Button(root, text="=", width=4, height=4, command=calculate)
button.grid(row=5, column=5)

root.mainloop()