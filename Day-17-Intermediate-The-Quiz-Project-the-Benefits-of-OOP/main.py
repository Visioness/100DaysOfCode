from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = [Question(data["text"], data["answer"]) for data in question_data]

quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()

print(f"You have completed the quiz!\nYour final score is {quiz.score}/{len(question_bank)}")