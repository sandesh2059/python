#  ko banxa crore pati is a game where a player gets money if he/she gives correct answer


class Question():
    def __init__(self, text, option, correct_ans, prize):
        self.text = text
        self.options = options
        self.correct_ans = correct_ans
        self.prize = prize

    def display(self):
        print(self.text)
        for i, option in enumerate(self.options, start = 1):
            print(f"{i}. {option}")

    def is_Correct(self, answer):
        return answer == self.correct_ans

class game():
    def __init__(self):
        self.question = []
        self.winning = 0

    def add_Question(self, question):
        self.question.append(question)
    
    def start(self):
        for q in self.question:
            q.display()
            answer = int(input("enter your answer(1-4): ", ))
            


        