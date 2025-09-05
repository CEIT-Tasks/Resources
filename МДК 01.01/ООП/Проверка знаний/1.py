from abc import ABC, abstractmethod

class Animal(ABC):
  @abstractmethod
  def speak(self, loud=False) -> str:
    pass

class Dog(Animal):
  def speak(self, loud=False):
    return "ГАВ!" if loud else "гав"

class Cat(Animal):
  def speak(self, loud=False):
    return "МЯУ!" if loud else "мяу"

class Cow(Animal):
  def speak(self, loud=False):
    return "МУУУ!" if loud else "муу"