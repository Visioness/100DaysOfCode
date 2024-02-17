from tkinter import *

window = Tk()

window.title("|-  My First GUI Program  -|")
window.minsize(width=800, height=600)

label = Label(text="My first text!", font=("Arial", 24, "bold"), bg="green")
label.pack()

def change_text():
    label["text"] = "My very new text!"


def change_font():
    label["font"] = ("Times New Roman", 24, "bold")


font_button = Button(text="Change font to Times New Roman", command=change_font)
font_button.pack()

text_button = Button(text="Change text", command=change_text)
text_button.pack()





window.mainloop()