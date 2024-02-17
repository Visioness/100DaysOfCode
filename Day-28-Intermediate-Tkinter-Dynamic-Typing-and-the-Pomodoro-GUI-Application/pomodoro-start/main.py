from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#508D69"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 45
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# Repeat count, work-break remaining time in second, current timer 
reps = 0
work_sec = int(WORK_MIN * 60)
short_break_sec = int(SHORT_BREAK_MIN * 60)
long_break_sec = int(LONG_BREAK_MIN * 60)
timer = None


# ---------------------------- TIMER RESET ------------------------------- # 
def timer_reset():
    global reps
    window.after_cancel(timer)
    label.config(text="-Pomodoro-", fg=PINK)
    checkmarks.config(text="")
    canvas.itemconfig(timer_text, text="00.00")
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    if reps < 9:
        if reps == 8:
            label.config(text="-Long Break-", fg=RED)
            countdown(long_break_sec)  
        elif reps % 2 == 0:
            label.config(text="-Work-", fg=GREEN)
            countdown(work_sec)
        elif reps % 2 == 1:
            label.config(text="-Break-", fg=PINK)
            checkmarks["text"] += "|✔|"
            countdown(short_break_sec)
        reps += 1
    else:
        timer_reset()


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(seconds):
    # Calculating remaining minutes and seconds
    count_min = math.floor(seconds / 60)
    count_sec = seconds % 60
    canvas.itemconfig(timer_text, text=f"{count_min:02d}:{count_sec:02d}")
    if seconds > 0:
        global timer
        # Decreasing the remaining time by one second and keep counting down
        timer = window.after(1000, countdown, seconds - 1)
    else:
        # When the count down is done goes for the next work or break
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #
# Creating window and configuring it
window = Tk()
window.title("Study with Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# Main Text
label = Label(text="-Pomodoro-", font=(FONT_NAME, 35, "bold"), fg=PINK, bg=YELLOW, width=11)
label.grid(row=1, column=5)

# A canvas that includes timer text and tomato image
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="/mnt/c/Users/VISIONESS/Projects/100DaysOfPython/day-28/pomodoro-start/tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00.00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=3,column=5)

# Checkmarks for the completed work sets
checkmarks = Label(text="", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 18, "bold"))
checkmarks.grid(row=5, column=5)

# Start button that starts the timer
button_start = Button(text="Start", font=(FONT_NAME, 10, "bold"), command=start_timer)
button_start.config(bg=GREEN, activebackground=GREEN)
button_start.grid(row=5, column=2)

# Reset button for resetting the program
button_reset = Button(text="Reset", font=(FONT_NAME, 10, "bold"), command=timer_reset)
button_reset.config(bg=RED, activebackground=RED)
button_reset.grid(row=5, column=8)

window.mainloop()