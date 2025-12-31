class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    
    def total_marks(self):
        return sum(self.marks)
    def percentage(self):
        return self.total_marks() / len(self.marks)
    def grade(self):
        percent = self.percentage()
        if percent >= 90:
            return "A"
        elif percent >= 75:
            return "B"
        elif percent >= 60:
            return "C"
        else:
            return "Fail"
