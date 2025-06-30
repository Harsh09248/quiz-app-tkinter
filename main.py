from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import QuizInterface
from score_db import create_table


create_table()


question_bank = [
    Question(q["question"], q["correct_answer"])
    for q in question_data
]


quiz = QuizBrain(question_bank)
quiz_ui = QuizInterface(quiz)
