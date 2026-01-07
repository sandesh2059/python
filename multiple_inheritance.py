class Department:
    def __init__(self, department):
        self.department = department
    
class Employee:
    def __init__(self, employee_name):
        self.employee_name = employee_name


class FunctionalDesignation:
    def __init__(self, position):
        self.position = position
        
class Internship(Department, Employee, FunctionalDesignation):
    def __init__(self, department, employee_name, position,intern_name, internship_duration):
        Department.__init__(self, department)
        Employee.__init__(self, employee_name)
        FunctionalDesignation.__init__(self, position)
        self.internship_duration = internship_duration
        self.intern_name = intern_name
        
class InternshipInfoContainer:
    def __init__(self, marketing = None, frontend = None, backend = None):
        self.marketing = []
        self.frontend = []
        self.backend = []
    def total(self):
        for intern in intern_list:
            if intern.department == 'Marketing':
                self.marketing.append(intern.intern_name)
            elif intern.department == 'Frontend':
                self.frontend.append(intern.intern_name)
            elif intern.department == 'Backend':
                self.backend.append(intern.intern_name)
        return f"marketing: {self.marketing}\nfrontend: {self.frontend}\nbackend: {self.backend}"
    
    def count(self):
        return f"marketing: {len(self.marketing)}\nfrontend: {len(self.frontend)}\nbackend: {len(self.backend)}"
    
    def longest_and_shortest(self):
        longest = max(intern_list, key=lambda intern: intern.internship_duration)
        shortest = min(intern_list, key=lambda intern: intern.internship_duration)
        return f"longest: {longest.intern_name} of {longest.department} department = {longest.internship_duration} months\nshortest: {shortest.intern_name} of {shortest.department} department = {shortest.internship_duration} months"
            
    
intern1 = Internship('Marketing', 'Alice', 'Manager', 'John', 3)
intern2 = Internship('Frontend', 'Bob', 'Team Lead', 'Emma', 6)
intern3 = Internship('Backend', 'Charlie', 'Senior Dev', 'Liam', 4)
intern4 = Internship('Backend', 'David', 'Senior Dev', 'Olivia', 5)
intern5 = Internship('Backend', 'Eve', 'Team Lead', 'Noah', 5)
intern6 = Internship('Frontend', 'Frank', 'Developer', 'Ava', 3)
intern7 = Internship('Frontend', 'Grace', 'Developer', 'Sophia', 4)
intern8 = Internship('Frontend', 'Hannah', 'Team Lead', 'Mason', 5)
intern9 = Internship('Marketing', 'Ian', 'Manager', 'Isabella', 3)
intern10 = Internship('Marketing', 'Jack', 'Executive', 'Ethan', 5)
intern_list = [intern1, intern2, intern3, intern4, intern5, intern6, intern7, intern8, intern9, intern10]

info = InternshipInfoContainer(intern_list)
print(info.total())
print(info.count())
print(info.longest_and_shortest())




