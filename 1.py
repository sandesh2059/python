class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    
    def total_marks(self):
        return sum(self.marks)
