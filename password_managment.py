from tkinter import *
from tkinter import messagebox
from random import randint, shuffle, choice
import pyperclip
from password_create import password_generator

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def insert_new_password():
    random_new_password = password_generator()
    password_label_entry.insert(0, random_new_password)
    pyperclip.copy(random_new_password())

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = website_label_entry.get()
    email = email_label_entry.get()
    password = password_label_entry.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(
            title="Warning!", message="Please make sure you did not leave any empty fileds.")
    else:
        is_ok = messagebox.askyesno(title=website, message=f"Please check your entry: \nEmail: {email}"
                                    f"\nPassword: {password} \nIs it ok to save?")
        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website} | {password} | {email}\n")
                website_label_entry.delete(0, END)
                password_label_entry.delete(0, END)


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

website_label_entry = Entry(width=35)
website_label_entry.grid(row=1, column=1, columnspan=2)
website_label_entry.focus()
email_label_entry = Entry(width=35)
email_label_entry.grid(row=2, column=1, columnspan=2)
email_label_entry.insert(0, "mralimov89@gmail.com")
password_label_entry = Entry(width=21)
password_label_entry.grid(row=3, column=1)


generate_button = Button(text="Generate Password",
                         command=insert_new_password())
generate_button.grid(row=3, column=2)
add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)


window.mainloop()
