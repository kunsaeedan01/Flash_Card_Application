import random
from tkinter import *
import pandas
from random import *
BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
learned_words = []


def save_progress():
    dictionary.remove(current_card)
    data = pandas.DataFrame(dictionary)
    data.to_csv(r"C:\Users\Lenovo LEGION\Desktop\flash-card-project-start\data\words_to_learn.csv", index=False)
    next_card()


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = choice(dictionary)
    card.itemconfig(title, text="French", fill="black")
    card.itemconfig(word_text, text=current_card["French"], fill="black")
    card.itemconfig(card_image, image=front_card)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    card.itemconfig(title, text="English", fill="white")
    card.itemconfig(word_text, text=current_card["English"], fill="white")
    card.itemconfig(card_image, image=back_card)


# DataFrame
try:
    words_file = pandas.read_csv(r"C:\Users\Lenovo LEGION\Desktop\flash-card-project-start\data\words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv(r"C:\Users\Lenovo LEGION\Desktop\flash-card-project-start\data\french_words.csv")
    dictionary= original_data.to_dict(orient="records")
else:
    dictionary = words_file.to_dict(orient="records")


# Window
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

# Canvas
card = Canvas(height=526, width=800, bg=BACKGROUND_COLOR, highlightthickness=0)
front_card = PhotoImage(file=r"C:\Users\Lenovo LEGION\Desktop\flash-card-project-start\images\card_front.png")
back_card = PhotoImage(file=r"C:\Users\Lenovo LEGION\Desktop\flash-card-project-start\images\card_back.png")
card_image = card.create_image(400, 263, image=front_card)
title = card.create_text(400, 150, text="", font=("Arial", 40, "italic"))
word_text = card.create_text(400, 263, text="", font=("Arial", 60, "bold"))
card.grid(column=0, row=0, columnspan=2)

# Buttons
checkmark_img = PhotoImage(file=r"C:\Users\Lenovo LEGION\Desktop\flash-card-project-start\images\right.png")
cross_img = PhotoImage(file=r"C:\Users\Lenovo LEGION\Desktop\flash-card-project-start\images\wrong.png")
checkmark = Button(image=checkmark_img, highlightthickness=0, command=save_progress)
checkmark.grid(column=0, row=1)
cross = Button(image=cross_img, highlightthickness=0, command=next_card)
cross.grid(column=1, row=1)



window.mainloop()