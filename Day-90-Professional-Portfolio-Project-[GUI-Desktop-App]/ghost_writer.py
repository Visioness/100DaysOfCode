from tkinter import *
from PIL import Image, ImageTk
import time

BG_COLOR = '#A30052'
FG_COLOR = '#F9E9D0'
TEXT_FONT = ('TimesNewRoman', 15, 'italic')
COUNT_FONT = ('TimesNewRoman', 32, 'bold')
seconds = None
timer = None
counting = False

def show_text(event):
    global seconds, counting
    window.after(10, lambda: countdown_canvas.itemconfig(text, text=f'{user_input.get("1.0", "end-1c")}'))
    # RESET TIMER
    if event.char.isalpha():
        seconds = len(photo_images)
        if counting:
            counting = False
            countdown_reset()
        countdown(seconds)


def countdown_reset():
    window.after_cancel(timer)


def countdown(seconds):
    global timer, counting
    if seconds > 0:
        timer = window.after(1000, countdown, seconds - 1)
        counting = True
        countdown_canvas.itemconfig(background, image=photo_images[-seconds])
    elif seconds == 0:
        user_input.delete('1.0', 'end')
        window.after(10, lambda: countdown_canvas.itemconfig(text, text=f'{user_input.get("1.0", "end-1c")}'))
        countdown_canvas.itemconfig(background, image=photo_images[0])


# UI Setup
window = Tk()
window.geometry('900x600')
window.config(padx=50, pady=50, bg=BG_COLOR)
window.title('Ghost Writer')

# Text Widget
user_input = Text(bg=FG_COLOR, font=TEXT_FONT, highlightcolor='black', highlightthickness=3)
user_input.place(x=400, y=250, anchor='center', width=800, height=500)
user_input.focus_set()
user_input.bind('<KeyPress>', show_text)

# Countdown Widget
countdown_canvas = Canvas(bg=BG_COLOR, width=800, height=500, highlightthickness=0)
images = [Image.new('RGBA', (800, 500), (249, 233, 208, i)) for i in range(256, -1, -32)]
photo_images = [ImageTk.PhotoImage(image) for image in images]
background = countdown_canvas.create_image(400, 250, image=photo_images[0], anchor='center')
text = countdown_canvas.create_text(400, 250, text='Type something!', fill=BG_COLOR, font=TEXT_FONT)

#countdown = countdown_canvas.create_text(400, 250, text='5', fill=BG_COLOR, font=COUNT_FONT)
countdown_canvas.place(x=400, y=250, anchor='center')

window.mainloop()