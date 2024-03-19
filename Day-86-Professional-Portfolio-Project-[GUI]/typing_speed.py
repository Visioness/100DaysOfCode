'''
Typing speed tester, checks and shows - CPM(Characters Per Minute), WPM(Words Per Minute), mistake count and remaining time.
'''
from tkinter import *
import random

# Reading text file
with open('words.txt', 'r') as file:
    words = [line.strip() for line in file.readlines()]

# Color and font variables
NORMAL_FONT = ('Arial', 18, 'normal')
BOLD_FONT = ('Arial', 1)
BACKGROUND = '#7DA1BF'
FOREGROUND = '#2F4A60'
TEXT_BG = '#B0D2DA'

# Global variables used in functions
sample_list = random.sample(words, k=120)
correct = 0
correct_chars = 0
mistakes_count = 0
word_index = 0
text_items = []
timer = None
countdown_started = False


# Creating each word separately as canvas text item to be able to color them later
def create_text_items():
    global text_canvas
    x = 20
    y = 12
    for word in sample_list:
        text_item = text_canvas.create_text(x, y, text=word, font=NORMAL_FONT, fill='black', anchor='nw')
        text_items.append(text_item)
        x += text_canvas.bbox(text_item)[2] - text_canvas.bbox(text_item)[0] + 10
        if x > 710:
            y += 50
            x = 20


# Checks user input after each spacebar press
def check_word(event):
    global correct, mistakes_count, text, word_index, text_items, correct_chars
    user_word = user_input.get('1.0', 'end-1c').strip()
    
    if sample_list[word_index] == user_word:
        correct += 1
        text_canvas.itemconfig(text_items[word_index], fill='green')
        correct_chars += len(sample_list[word_index])
    else:
        mistakes_count += 1
        text_canvas.itemconfig(text_items[word_index], fill='red')
        stats_canvas.itemconfig(mistakes, text=f'{mistakes_count}')

    # Updating for the new word
    word_index += 1
    user_input.delete('1.0', 'end')


# Starts counting down right after the first key press
def onKeyPress(event):
    global countdown_started
    if not countdown_started:
        countdown(5)
        countdown_started = True


# Counting down from given seconds
def countdown(seconds):
    global timer, correct, correct_chars
    if seconds >= 0:
        timer = window.after(1000, countdown, seconds - 1)
        stats_canvas.itemconfig(remaining, text=f'{seconds}')
        if seconds != 60:
            stats_canvas.itemconfig(wpm, text=f'{check_wpm(correct, seconds):.2f}')
            stats_canvas.itemconfig(cpm, text=f'{check_cpm(correct_chars, seconds):.2f}')
    else:
        user_input.destroy()


# Words Per Minute
def check_wpm(correct, seconds):
    return correct * 60 / (60 - seconds)


# Characters Per Minute
def check_cpm(correct_chars, seconds):
    return correct_chars * 60 / (60 - seconds)


# UI Setup
window = Tk()
window.config(padx=30, pady=20, bg=BACKGROUND)
window.title('Typing Speed Test')

label = Label(text='Typing Speed Test', font=('Microsoft Sans Serif', 15, 'bold'), bg=BACKGROUND, fg=FOREGROUND)
label.grid(row=1, column=1, pady=12)

# Canvas to display random words
text_canvas = Canvas(width=800, height=400, highlightthickness=2, highlightbackground=FOREGROUND, bg=TEXT_BG)
create_text_items()
text_canvas.grid(row=2, column=1, pady=10)

# Creating another canvas for stats
stats_canvas = Canvas(width=350, height=400, bg=BACKGROUND, highlightthickness=0)
remaining_label = stats_canvas.create_text(175, 40, text='~~ Remaining time ~~', font=('Microsoft Sans Serif', 15, 'bold'), fill=FOREGROUND)
remaining = stats_canvas.create_text(175, 70, text='60', font=('Microsoft Sans Serif', 18, 'bold'), fill=FOREGROUND)

wpm_label = stats_canvas.create_text(175, 120, text='~~ Words Per Minute ~~', font=('Microsoft Sans Serif', 15, 'bold'), fill=FOREGROUND)
wpm = stats_canvas.create_text(175, 150, text='0', font=('Microsoft Sans Serif', 18, 'bold'), fill=FOREGROUND)

cpm_label = stats_canvas.create_text(175, 200, text='~~ Characters Per Minute ~~', font=('Microsoft Sans Serif', 15, 'bold'), fill=FOREGROUND)
cpm = stats_canvas.create_text(175, 230, text='0', font=('Microsoft Sans Serif', 18, 'bold'), fill=FOREGROUND)

mistakes_label = stats_canvas.create_text(175, 280, text='~~ Mistakes Made ~~', font=('Microsoft Sans Serif', 15, 'bold'), fill=FOREGROUND)
mistakes = stats_canvas.create_text(175, 310, text='0', font=('Microsoft Sans Serif', 18, 'bold'), fill=FOREGROUND)
stats_canvas.grid(row=1, column=2, rowspan=3, padx=10)

# User input word
user_input = Text(font=NORMAL_FONT, width=15, height=1, bg=TEXT_BG, highlightthickness=1, highlightbackground=FOREGROUND)
user_input.grid(row=3, column=1, pady=10)
user_input.bind('<space>', check_word)
user_input.bind('<KeyPress>', onKeyPress)

window.mainloop()