
class QuizBrain:
    def __init__(self, q_bank):
        self.question_number = 0
        self.question_list = q_bank
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.question_list)
        #Professionalism
        # if self.question_number < len(self.question_list):
        #     return True
        # else:
        #     return False

    def next_question(self):
        #forgot about the 'question_number' attribute. And prractically there is no need of a loop
        #coz we can create a new function to check whether there are questions left or not.[Professionalism]
        # for question in range(0, len(self.question_list)):
        #     current_question = self.question_list[question]
        #     user_choice = input(f"Q.{question+1}: {current_question.text}. (true/false): ").capitalize()
        #     print(user_choice)
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_choice = input(f"Q.{self.question_number}: {current_question.text}. (true/false): ").capitalize()
        self.check_answer(user_choice, current_question.answer)

    def check_answer(self, user_choice, answer):
        if user_choice.lower() == answer.lower():
            print("You got it correct")
            self.score += 1

        else:
            print("You're Wrong")


        print(f"The correct answer was: {answer}")
        print(f"Your current score is: {self.score}/{self.question_number}.")
