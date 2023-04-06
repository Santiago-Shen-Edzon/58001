class Person:
    def __init__(self, name, prelim, midterm, final):
        self.name = name
        self.__pre = prelim
        self.__mid = midterm
        self.__fin = final

    def prelim_grade(self):
        return self.__pre
    
    def midterm_grade(self):
        return self.__mid
    
    def final_grade(self):
        return self.__fin
    
    def average_grades(self):
        return (self.__pre + self.__mid + self.__fin) / 3
    
person1 = Person("Student 1", 85, 90, 92)
person2 = Person("Student 2", 75, 80, 85)
person3 = Person("Student 3", 90, 95, 88)

print(f"Student 1 prelim grade: {person1.prelim_grade()}, midterm grade: {person1.midterm_grade()}, final grade: {person1.final_grade()}")
print(f"Student 1 average grade is: {person1.average_grades()}\n")

print(f"Student 2 prelim grade: {person2.prelim_grade()}, midterm grade: {person2.midterm_grade()}, final grade: {person2.final_grade()}")
print(f"Student 2 average grade is: {person2.average_grades()}\n")

print(f"Student 3 prelim grade: {person3.prelim_grade()}, midterm grade: {person3.midterm_grade()}, final grade: {person3.final_grade()}")
print(f"Student 3 average grade is: {person3.average_grades()}\n")