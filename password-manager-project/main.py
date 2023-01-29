from tkinter import *
from tkinter import messagebox

# ---------------------------- CONSTANTS ------------------------------- #
NAME_OF_APP = "Password Manager"
BLUE = "#cce5ff"
FONT_NAME = "Courier"
EXAMPLE_EMAIL = "abc@gmail.com"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    with open("data.txt", "a") as data_file:
        data_file.write(f"{website} | {email} | {password}\n")
        website_entry.delete(0, END)
        password_entry.delete(0, END)

        if email != EXAMPLE_EMAIL:
            email_entry.delete(0, END)
            email_entry.insert(0, EXAMPLE_EMAIL)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title(NAME_OF_APP)
window.config(padx=60, pady=60, bg=BLUE)

canvas = Canvas(width=200, height=200, bg=BLUE, highlightthickness=0)
lock_img = PhotoImage(file="./img/logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(row=0, column=1)

# Labels
website_label = Label(text="Website:", bg=BLUE, font=(FONT_NAME, 11, "bold"))
website_label.grid(row=1, column=0)

email_label = Label(text="Email/Username:", bg=BLUE, font=(FONT_NAME, 11, "bold"))
email_label.grid(row=2, column=0)

password_label = Label(text="Password:", bg=BLUE, font=(FONT_NAME, 11, "bold"))
password_label.grid(row=3, column=0)

# Entries
website_entry = Entry(width=46)
website_entry.grid(row=1, column=1, columnspan=2, padx=2, pady=2)
website_entry.focus()

email_entry = Entry(width=46)
email_entry.grid(row=2, column=1, columnspan=2, padx=2, pady=2)
email_entry.insert(0, EXAMPLE_EMAIL)

password_entry = Entry(width=28)
password_entry.grid(row=3, column=1, padx=3, pady=2)

# Buttons
generate_password_button = Button(text="Generate Password", font=(FONT_NAME, 8))
generate_password_button.grid(row=3, column=2, pady=2)

add_button = Button(text="Add", width=46, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()