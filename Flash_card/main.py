from tkinter import *
import random
import pandas

BACKGROUND_COLOR = "#B1DDC6"
LANGUAGE_FONT = ("Ariel", 40, "italic")
WORD_FONT = ("Ariel", 40, "bold")
current_card = {}

try:
    # Reading CVS
    data = pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("./data/french_words.csv")
    data_dic = original_data.to_dict(orient="records")
else:
    data_dic = data.to_dict(orient="records")


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(data_dic)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=card_front_img)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back_img)


def is_known():
    data_dic.remove(current_card)
    data = pandas.DataFrame(data_dic)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()


# --------- UI ---------
window = Tk()
window.title("Flash Card Game (French/English)")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR, highlightthickness=0)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
card_front_img = PhotoImage(file="./images/card_front.png")
card_back_img = PhotoImage(file="./images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_img)
# TEXT
card_title = canvas.create_text(400, 150, font=LANGUAGE_FONT)
card_word = canvas.create_text(400, 263, font=WORD_FONT)
canvas.grid(column=0, row=0, columnspan=2)

# BUTTONS
check_image = PhotoImage(file="./images/right.png")
right_btn = Button(image=check_image, highlightthickness=0, borderwidth=0, command=is_known)
right_btn.grid(column=1, row=2)

wrong_image = PhotoImage(file="./images/wrong.png")
wrong_btn = Button(image=wrong_image, highlightthickness=0, borderwidth=0, command=next_card)
wrong_btn.grid(column=0, row=2)

next_card()

window.mainloop()
