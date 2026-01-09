class students:
    college_name: 'ACHS'

    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno
    
    def welcome(self):
        print("welcome ", self.name)


s1 = students("sandesh", 23081019)
print(s1.name, s1.rollno)
s1.welcome()

