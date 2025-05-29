import random
import string
import tkinter
from tkinter import *

from textdistance import length


def get_password(length, numflag, capitalflag, spflag, num_length, sp_length):
    special_characters = string.punctuation
    numbers = string.digits
    alphabets = string.ascii_lowercase
    cap_alphabets = string.ascii_uppercase
    guranteed = ''.join(random.choice(numbers) for _ in range(num_length))
    guranteed += ''.join(random.choice(special_characters) for _ in range(sp_length))

    rand = alphabets
    if numflag:
        rand += numbers
    if capitalflag:
        rand += cap_alphabets
    if spflag:
        rand += special_characters

    guranteed += (''.join(random.choice(rand) for _ in range(length-num_length-sp_length)))

    return (''.join(random.shuffle(guranteed)))

def buttonclicked() -> None:
    length = var4.get()
    num_flag = var1.get()
    capital_flag = var2.get()
    sp_flag = var3.get()
    num_length = var5.get()
    sp_length = var6.get()
    passkey = get_password(length, num_flag, capital_flag, sp_flag, num_length, sp_length)
    output.config(text=f"{passkey}")

# Root window
root = Tk()
root.title("Password Generator")
root.geometry("800x600")
root.configure(bg="#1e1e2f")

# Frame
f = Frame(root, bg="#1e1e2f")
f.pack(expand=True)

# Variables
var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar(value=8)
var5 = IntVar(value=1)
var6 = IntVar(value=1)

# Title
Label(f, text="Password Generator",
         font=('Segoe UI', 24, 'bold'), bg="#1e1e2f", fg="#f0f0f0").pack(pady=20)

# Password Length
Label(f, text="Password Length:", font=('Segoe UI', 14),
      bg="#1e1e2f", fg="#f0f0f0").pack(pady=(20, 5))

Spinbox(f, from_=4, to=32, textvariable=var4, width=5,
        font=('Segoe UI', 14, 'bold'), bg='#ffffff', fg='black').pack(pady=5)


#Include Label
Label(f, text="Include",
         font=('Segoe UI', 24, 'bold'), bg="#1e1e2f", fg="#f0f0f0").pack(pady=20)

# Checkbuttons
Checkbutton(f, text="0-9", variable=var1,
               font=("Segoe UI", 14), bg="#1e1e2f", fg="#f0f0f0",
               selectcolor="#2196F3", activebackground="#1e1e2f").pack(side="left", padx=10, pady=5)
Checkbutton(f, text="A-Z", variable=var2,
               font=("Segoe UI", 14), bg="#1e1e2f", fg="#f0f0f0",
               selectcolor="#2196F3", activebackground="#1e1e2f").pack(side="left", padx=10, pady=5)
Checkbutton(f, text="!@#$%^&*", variable=var3,
               font=("Segoe UI", 14), bg="#1e1e2f", fg="#f0f0f0",
               selectcolor="#2196F3", activebackground="#1e1e2f").pack(side="left", padx=10, pady=5)

#Minimum no of numerals
Label(f, text="Minimum Numbers", font=("Soque UI", 14),
          bg="#1e1e2f", fg="#f0f0f0").pack(pady=(10, 5))
Spinbox(f, from_=1,to=length, textvariable=var5, width=5,
           font=('Segoe UI', 14, 'bold'), bg='#ffffff', fg='black').pack(pady=5)

#Minimum no of special characters
Label(f, text="Minimum Special Characters", font=("Soque UI", 14),
          bg="#1e1e2f", fg="#f0f0f0").pack(pady=(10, 5))
Spinbox(f, from_=1,to=length, textvariable=var6, width=5,
           font=('Segoe UI', 14, 'bold'), bg='#ffffff', fg='black').pack(pady=5)

# Generate Button
Button(f, text="Generate Password", font=('Segoe UI', 14, 'bold'),
          bg="#4CAF50", fg="white", command=buttonclicked,
          activebackground="#45a049").pack(pady=20)

# Output Label
output = Label(f, text="", font=('Courier New', 14, 'bold'),
                  bg="#1e1e2f", fg="#ffd54f")
output.pack(pady=10)

root.mainloop()
