#Password Generator
from tkinter import *
from tkinter import messagebox
import random
import string

root = Tk()
root.title("Password Generator")

canvas = Canvas(root, height=600, width=600)
canvas.pack()

def password_generator():
    password_length = int(entry_length.get())

    if password_length >= 7:
        if random.choice([True, False]):
            prefix = ''.join(random.choice(string.ascii_lowercase) for _ in range(3))
        else:
            prefix = ''.join(random.choice(string.ascii_letters) for _ in range(3))

        special_char = '@'
        remaining_length = password_length - len(prefix + special_char)
        suffix = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(remaining_length))
        generated_password = f"{prefix}{special_char}{suffix}"
        
        list_password.delete(0, END)  
        list_password.insert(0, generated_password)
    else:
        list_password.delete(0, END)
        messagebox.showerror("Error", "Password length must be at least 7 characters.")

label_password = Label(root, text="Password Generator", fg='red', font=('Libre Baskerville', 30))
canvas.create_window(300, 50, window=label_password)

label_length = Label(root, text="Enter length you want")
canvas.create_window(300, 150, window=label_length)

entry_length = Entry(root)
canvas.create_window(300, 200, window=entry_length)

button = Button(root, text="Generate Password", command=password_generator)
canvas.create_window(300, 250, window=button)

list_password = Listbox(root, height=3)
canvas.create_window(300, 300, window=list_password)

root.mainloop()
