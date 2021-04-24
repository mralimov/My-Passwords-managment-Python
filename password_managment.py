from tkinter import *
from tkinter import messagebox
from random import randint, shuffle, choice
import pyperclip
from password_create import password_generator
import json

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
    new_data = {
        website: {
            "email": email,
            "password": password
        }}

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(
            title="Warning!", message="Please make sure you did not leave any empty fileds.")
    else:
        try:
            with open("data.json", "r") as data_file:
                # Reading old date
                new_data2 = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", 'w') as data_file2:
                json.dump(new_data, data_file2, indent=4)

        else:
            # Updating old data with new data
            new_data2.update(new_data)

            with open("data.json", 'w') as data_file3:
                # Saving updated data
                json.dump(new_data, data_file3, indent=4)
        finally:
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

search_button = Button(text="Search", width=13, command=find_password)
search_button.grid(row=1, column=2)
generate_button = Button(text="Generate Password",
                         command=insert_new_password())
generate_button.grid(row=3, column=2)
add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)


window.mainloop()
