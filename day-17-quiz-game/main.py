from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
import random


question_bank = []
for question in question_data:
    question_text = question['question']
    answer_text = question['correct_answer']
    new_question = Question(question_text, answer_text)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()
print('Quiz complete')
print(f'Final score: {quiz.score}/{quiz.question_number}')
print(f'Average: {round(quiz.score/quiz.question_number, 2)*100}%')
