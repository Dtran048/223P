class Person:
    def __init__(self, first_name, last_name, /):
        self.firstname = first_name
        self.lastname = last_name

class Faculty(Person):
    def __init__(self, first_name, last_name, department, / ):
        super().__init__(first_name, last_name)
        self.department = department

class Student(Person):
    def __init__(self, first_name, last_name, / ):
        super().__init__(first_name, last_name)
    def set_class(self, class_year, /):
        self.classyear = class_year
    def set_major(self, major, /):
        self.major = major
    def set_advisor(self, Faculty, /):
        self.advisor = Faculty