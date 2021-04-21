from tkinter import *
from tkinter import messagebox
from random import randint, shuffle, choice
import pyperclip
from password_create import password_generator


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("My Password manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
my_pass_img = PhotoImage(file="./logo.png")
canvas.create_image(100, 100, image=my_pass_img)
canvas.grid(row=0, column=1)
