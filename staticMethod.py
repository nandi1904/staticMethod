# Use of class method and static method. 

from datetime import date 
  
class Student: 
    def __init__(self, name, age): 
        self.name = name 
        self.age = age 
      
    # a class method to create a Student object by birth year. 
    @classmethod
    def fromBirthYear(cls, name, year): 
        # use self for the first argument to instance methods
        # use cls for the first argument to class methods.
        return cls(name, date.today().year - year) 
      
    # a static method to check if a Student is adult or not. 
    @staticmethod
    def isAdult(age): 
        return age > 18
  
Student1 = Student('Ravi', 25) 
Student2 = Student1.fromBirthYear('Ravi', 1990) 
  
print Student1.age 
print Student2.age 
  
# print the result 
print Student.isAdult(22) 