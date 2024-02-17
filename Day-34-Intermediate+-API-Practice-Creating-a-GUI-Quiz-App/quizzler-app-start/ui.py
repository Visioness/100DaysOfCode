from tkinter import *
from quiz_brain import QuizBrain
from data import parameters


THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.canvas = Canvas(width=300, height=300, bg="white")
        self.question_text = self.canvas.create_text(150, 150, text="Hello canvas!", font=("Arial", 20, "italic"), width=250, fill=THEME_COLOR)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        self.score_label = Label(text=f"Score: {self.quiz.score} / {parameters['amount']}", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        image_false = PhotoImage(file="images/false.png")
        image_true = PhotoImage(file="images/true.png")

        self.false_button = Button(image=image_false, highlightthickness=0, command=self.false_pressed)
        self.false_button.grid(row=2, column=0)

        self.true_button = Button(image=image_true, highlightthickness=0, command=self.true_pressed)
        self.true_button.grid(row=2, column=1)

        self.next_question()

        self.window.mainloop()
    

    def next_question(self):
        self.canvas.config(bg="white")
        self.score_label.config(text=f"Score: {self.quiz.score} / {parameters['amount']}")
        if self.quiz.still_has_questions():
            question = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=question)
        else:
            self.canvas.itemconfig(self.question_text, text="You finished the quiz!")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")
    

    def true_pressed(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)


    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)


    def give_feedback(self, is_right: bool):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        
        self.window.after(1000, self.next_question)
