from tkinter import *
import pandas as pd 
import random

BACKGROUND_COLOR = "#B1DDC6"

# Read Data
try: 
    french_words = pd.read_csv("Day_31/flash_card_project/data/words_to_learn.csv")
except:
    french_words = pd.read_csv("Day_31/flash_card_project/data/french_words.csv")
finally:
    to_learn = french_words.to_dict(orient="records")

def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=card_front_image)
    flip_timer = window.after(3000, func=flip_card)

def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back_image)

def is_known():
    to_learn.remove(current_card)

    df = pd.DataFrame(to_learn)
    df.to_csv("Day_31/flash_card_project/data/words_to_learn.csv", index=False)
    next_card()

#------------------------------UI-------------------------------#
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526)
card_front_image = PhotoImage(file="Day_31/flash_card_project/images/card_front.png")
card_back_image = PhotoImage(file="Day_31/flash_card_project/images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_image)
card_title = canvas.create_text(400, 150, font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, font=("Ariel", 60, "bold"))

canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

wrong_button_image = PhotoImage(file="Day_31/flash_card_project/images/wrong.png")
wrong_button = Button(image=wrong_button_image, highlightthickness=0, command=next_card)
wrong_button.grid(row=1, column=0)

right_button_image = PhotoImage(file="Day_31/flash_card_project/images/right.png")
right_button = Button(image=right_button_image, highlightthickness=0, command=is_known)
right_button.grid(row=1, column=1)




next_card()

window.mainloop()