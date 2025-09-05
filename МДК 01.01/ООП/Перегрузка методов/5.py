from functools import singledispatchmethod

class Greeting:
  @singledispatchmethod
  def greet(self, name):
    print(f"Hello, {name}!")

  @greet.register
  def _(self, name: str, age: int):
    print(f"Hello, {name}, Your age is {age}!")