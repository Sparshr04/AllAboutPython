from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# new_q = Question("ass", "True")
# print(new_q.text, new_q.answer)

question_bank = []

#Creating a Question Bank from the List of Dictionaries
for question in question_data:
    # print(question)
    text = question["text"]
    answer = question["answer"]
    # new_question_bank = question_bank.append(Question(text, answer))
    question_bank.append(Question(text, answer))
print(question_bank)

# Passing the List od quesions to QuizBrain Class
temp = QuizBrain(question_bank)
while temp.still_has_questions():
    temp.next_question()

print("You've completed the quiz!")
print(f"Your final score is: {temp.score}/{len(question_bank)}")