from tkinter import *
import pandas
import random

# ---------------------------- CONSTANTS ------------------------------- #
BACKGROUND_COLOR = "#B1DDC6"
NAME_OF_APP = "Flashy"

data = pandas.read_csv("data/french_words.csv")
to_learn = data.to_dict(orient="records")
current_card = {}


# ---------------------------- NEXT CARD ------------------------------- #
def next_card():
    global current_card
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=card_font_img)
    window.after(3000, func=flip_card)


# ---------------------------- FLIP CARD ------------------------------- #
def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back_img)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title(NAME_OF_APP)
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526)
card_font_img = PhotoImage(file="./img/card_front.png")
card_back_img = PhotoImage(file="./img/card_back.png")
card_background = canvas.create_image(400, 263, image=card_font_img)
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

# Button
cross_img = PhotoImage(file="./img/wrong.png")
unknow_button = Button(image=cross_img)
unknow_button.config(bg=BACKGROUND_COLOR, highlightthickness=0, command=next_card)
unknow_button.grid(row=1, column=0)

check_img = PhotoImage(file="./img/right.png")
know_button = Button(image=check_img)
know_button.config(bg=BACKGROUND_COLOR, highlightthickness=0, command=next_card)
know_button.grid(row=1, column=1)

next_card()

window.mainloop()
