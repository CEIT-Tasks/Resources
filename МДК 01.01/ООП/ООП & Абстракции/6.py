class Student:
  def __init__(self, name, gradelist):
    self.name = name
    self.gradelist = []
    
  def add_grade(self, grade):
    if not (0 <= grade <= 100):
      raise ValueError("Grade must be between 0 and 100")
    self.gradelist.append(grade)
    
    def average_grade(self):
      if not self.gradelist:
        return 0
      return sum(self.gradelist) / len(self.gradelist)
    
class Gradebook(Student):
  def __init__(self):
    self.students = []
      
  def add_student(self, student):
    if not isinstance(student, Student):
      raise TypeError("Only Student instances can be added")
    self.students.append(student)
  
  def search_student(self, name):
    for student in self.students:
      if student.name == name:
        return student
    raise ValueError(f"Student with name {name} not found")
  
  def printAllWithAverage(self):
    for student in self.students:
      avg = student.average_grade()
      print(f"Student: {student.name}, Average Grade: {avg:.2f}")