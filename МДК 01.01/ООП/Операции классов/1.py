class Rectangle:
  def __init__(self, width, height):
    self.width = width
    self.height = height

  def area(self):
    return self.width * self.height

  def __eq__(self, other):
    if isinstance(other, Rectangle):
      return self.width == other.width and self.height == other.height
    return NotImplemented

  def __ne__(self, other):
    if isinstance(other, Rectangle):
      return not self.__eq__(other)
    return NotImplemented

  def __lt__(self, other):
    if isinstance(other, Rectangle):
      return self.area() < other.area()
    return NotImplemented

  def __le__(self, other):
    if isinstance(other, Rectangle):
      return self.area() <= other.area()
    return NotImplemented

  def __gt__(self, other):
    if isinstance(other, Rectangle):
      return self.area() > other.area()
    return NotImplemented

  def __ge__(self, other):
    if isinstance(other, Rectangle):
      return self.area() >= other.area()
    return NotImplemented