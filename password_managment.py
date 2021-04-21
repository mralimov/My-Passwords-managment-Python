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


website_label = Label(text="Website: ")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)
