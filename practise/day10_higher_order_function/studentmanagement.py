class student():
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.marks = {}
    
    def addMarks(self, subject , mark):
        self.marks.append[subject] = mark
    
    def total_marks(self):
        return sum(self.marks.values())
    
    

        