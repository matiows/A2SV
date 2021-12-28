from collections import defaultdict

class Student(object):
    def __init__(self, STUDENT_ID, grades):
        self.STUDENT_ID = STUDENT_ID
        self.grades = defaultdict(dict, grades)
    
    def set_age (self, age):
        if age>0 and age<100:
            self.__age = age

    def get_age (self):
        return self.__age
    
    def __str__ (self):
        return self.STUDENT_ID
    
    def compare_grade(self, other, course):
        return self.grades[course] > other.grades[course]
    
    def grade_report(self):
        return self.STUDENT_ID, [[x,y] for x,y in self.grades.items()]
    
    def __lt__ (self, other):
        return sum(self.grades.values()) < sum(other.grades.values())
    
    def __gt__ (self, other):
        return sum(self.grades.values()) > sum(other.grades.values())

    def __eq__ (self, other):
        return sum(self.grades.values()) == sum(other.grades.values())
    
stud1 = Student ("ETS0684/11", {
    "Eng": 82,
    "Amh": 90,
    "Math": 95
})
stud1.set_age (21)
stud2 = Student ("ETS0943/11", {
    "Eng": 78,
    "Amh": 98,
    "Math": 89
})
stud2.set_age (23)
stud3 = Student("ETS0845/11", {

})