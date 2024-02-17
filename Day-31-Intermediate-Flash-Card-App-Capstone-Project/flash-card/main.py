from tkinter import *
import pandas
import random


BACKGROUND_COLOR = "#B1DDC6"
current_word = None


def next_word():
    global timer, current_word, words

    # Checking if correct button clicked
    if button_correct["state"] == ACTIVE:
        words.remove(current_word)
        data = pandas.DataFrame(words)
        data.to_csv("data/words_to_learn.csv", index=False)
    
        # Reading CSV as a dataframe and converting it to a dictionary
        try:
            words = pandas.read_csv("data/words_to_learn.csv").to_dict(orient="records")
        except FileNotFoundError:
            words = pandas.read_csv("data/french_words.csv").to_dict(orient="records")
    
    current_word = random.choice(words)
    window.after_cancel(timer)
    canvas.itemconfig(image, image=front)
    canvas.itemconfig(language, text="French", fill="black")
    canvas.itemconfig(word, text=f"{current_word['French']}", fill="black")
    timer = window.after(3000, translation)
    

def translation():
    canvas.itemconfig(image, image=back)
    canvas.itemconfig(language, text="English", fill="white")
    canvas.itemconfig(word, text=f"{current_word['English']}", fill="white")


try:
    words = pandas.read_csv("data/words_to_learn.csv").to_dict(orient="records")
except FileNotFoundError:
    words = pandas.read_csv("data/french_words.csv").to_dict(orient="records")


# User Interface
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
current_word = random.choice(words)
timer = window.after(3000, translation)


canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
back = PhotoImage(file="images/card_back.png")
front = PhotoImage(file="images/card_front.png")
image = canvas.create_image(400, 263, image=front)
language = canvas.create_text(400, 150, text=f"French", font=("Ariel", 40, "italic"))
word = canvas.create_text(400, 263, text=f"{current_word['French']}", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=7)

image_wrong = PhotoImage(file="images/wrong.png")
image_correct = PhotoImage(file="images/right.png")
button_wrong = Button(image=image_wrong, relief="flat", command=next_word)
button_wrong.grid(row=1, column=1)

button_correct = Button(image=image_correct, relief="flat", command=next_word)
button_correct.grid(row=1, column=5)

window.mainloop()