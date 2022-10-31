from data import question_data
from question_model import Question
from quiz_brain import Quizbrain

question_bank = []
for data in question_data:
    question_text = data["question"]
    question_answer = data["correct_answer"]
    new_question = Question(q_text=question_text, q_answer=question_answer)
    question_bank.append(new_question)

quiz = Quizbrain(question_bank)
while quiz.still_has_question():
    quiz.next_question()
# print(question_bank[11].text)

print(f"You have completed all the {quiz.question_number} Questions.")
print(f"Your final score is {quiz.score}/{quiz.question_number}")