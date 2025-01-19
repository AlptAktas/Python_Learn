import question_model
import data
import quiz_brain

question_bank = []

for question in data.question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    question_bank.append(question_model.Question(question_text, question_answer))

quiz = quiz_brain.QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_quesion()


