import tkinter as tk

BACKGROUND_COLOR = "#B1DDC6"
FRONT_OF_CARD_LANGUAGE = "French"
BACK_OF_CARD_LANGUAGE = "English"


class Flashcard:
    def __init__(self):
        # Creating word
        self.french_word = None
        self.english_word = None
        #
        self.canvas = tk.Canvas(width=800, height=526)
        # Create images of card
        self.front_of_card_img = tk.PhotoImage(file="images/card_front.png")
        self.back_of_card_img = tk.PhotoImage(file="images/card_back.png")
        # creating background of card
        self.canvas.create_image(400, 263, image=self.front_of_card_img)
        self.canvas.create_text(400, 150, text="Hello", font=("Ariel", 40, "italic"))
        self.canvas.create_text(400, 263, text=f"press any button", font=("Ariel", 60, "bold"))
        self.canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
        self.canvas.grid(row=0, column=0, columnspan=2)

    def front_of_card(self, french_word, english_word):
        self.french_word = french_word
        self.english_word = english_word
        self.canvas.create_image(400, 263, image=self.front_of_card_img)
        self.canvas.create_text(400, 150, text=f"{FRONT_OF_CARD_LANGUAGE}", font=("Ariel", 40, "italic"))
        self.canvas.create_text(400, 263, text=f"{self.french_word}", font=("Ariel", 60, "bold"))
        # self.canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
        # self.canvas.grid(row=0, column=0, columnspan=2)

    def back_of_card(self):
        self.canvas.create_image(400, 263, image=self.back_of_card_img)
        self.canvas.create_text(400, 150, text=f"{BACK_OF_CARD_LANGUAGE}", font=("Ariel", 40, "italic"), fill="white")
        self.canvas.create_text(400, 263, text=f"{self.english_word}", font=("Ariel", 60, "bold"), fill="white")
        # self.canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
        # self.canvas.grid(row=0, column=0, columnspan=2)