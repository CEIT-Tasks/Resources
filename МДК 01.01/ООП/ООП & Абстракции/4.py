class Employee:
  def __init__(self, name, position, salary):
    self.name = name
    self.position = position
    self.salary = salary
    
  def getEmployeeInfo(self):
    return f"Name: {self.name}, Position: {self.position}, Salary: {self.salary}"
  
  def changeSalary(self, new_salary):
    self.salary = new_salary
    print(f"Salary for {self.name} changed to {self.salary}")
    
class Manager(Employee):
  def __init__(self, name, position, salary, department):
    super().__init__(name, position, salary)
    self.department = department
    
  def getEmployeeInfo(self):
    return f"Name: {self.name}, Position: {self.position}, Salary: {self.salary}, Department: {self.department}"
  
class Developer(Employee):
  def __init__(self, name, position, salary, programming_language):
    super().__init__(name, position, salary)
    self.programming_language = programming_language
    
  def getEmployeeInfo(self):
    return f"Name: {self.name}, Position: {self.position}, Salary: {self.salary}, Programming Language: {self.programming_language}"