class student():
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.marks = {}
    
    def addMarks(self, subject , mark):
        self.marks.append[subject] = mark
    
    def total_marks(self):
        return sum(self.marks.values())
    def percentage(self):
        return self.total_marks() / len(self.marks)
    def grade(self, percent):
        perc = self.percentage()
        if perc > 80:
            return 'A+'
        elif perc > 70 and perc <=90:
            return 'A'
        elif perc > 60 and perc <=80:
            return 'B+'
        else:
            return 'Fail'
    

        