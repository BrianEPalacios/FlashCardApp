import tkinter as tk
from flashcard import Flashcard
import random
import pandas as pd

BACKGROUND_COLOR = "#B1DDC6"
# counter to see if its the first time pressing the button so it doesn't save the opening text
counter = 0
french_words_csv_file_path = "data/french_words.csv"
words_to_learn_csv_file_path = "data/words_to_learn.csv"

try:
    word_df = pd.read_csv(words_to_learn_csv_file_path)
except FileNotFoundError:
    print("Using French Words")
    word_df = pd.read_csv(french_words_csv_file_path)
    word_dict = word_df.to_dict(orient="records")
else:
    print("Using Words to learn")
    word_dict = word_df.to_dict(orient="records")
    print(word_dict)


# ------------------------------ generate random word -----------------------------------==#


def generate_random_word():
    global word_dict
    current_card = random.choice(word_dict)
    french_word = current_card["French"]
    english_word = current_card["English"]
    return french_word, english_word


# ---------------------------------- Button Functionality --------------------------------------------#
# work around function for flipping the card: tkinter needs a function, was having problems calling the flashcard.back
def button_flip_card():
    flashcard.back_of_card()


def x_button_click():
    global flip_timer, counter
    counter += 1
    window.after_cancel(flip_timer)
    french_word, english_word = generate_random_word()
    flashcard.front_of_card(french_word=french_word, english_word=english_word)
    flip_timer = window.after(3000, func=button_flip_card)


def checkmark_button_click():
    global flip_timer, counter
    counter += 1
    window.after_cancel(flip_timer)
    french_word, english_word = generate_random_word()
    flashcard.front_of_card(french_word=french_word, english_word=english_word)
    flip_timer = window.after(3000, func=button_flip_card)
    # creating value to remove from dictionary
    print(word_dict)
    d = {"French": french_word, "English": english_word}
    print(d in word_dict)
    if counter > 1:
        word_dict.remove(d)
    # rewrite the csv so that it has the words you haven't learned
    data = pd.DataFrame(data=word_dict)
    # index equals false gets rid of the problem of always adding the index each time we save it!!!! Does'nt add index nums
    data.to_csv("data/words_to_learn.csv", index=False)


# --------------------------- UI Setup --------------------------------------------------------------#
window = tk.Tk()
window.title("Flashcard")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flashcard = Flashcard()
flip_timer = window.after(3000, func=button_flip_card)

# create buttons
x_image = tk.PhotoImage(file="images/wrong.png")
x_button = tk.Button(image=x_image, highlightthickness=0, command=x_button_click)
x_button.grid(row=1, column=0)

checkmark_img = tk.PhotoImage(file="images/right.png")
checkmark_button = tk.Button(image=checkmark_img, highlightthickness=0, command=checkmark_button_click)
checkmark_button.grid(row=1, column=1)

window.mainloop()
