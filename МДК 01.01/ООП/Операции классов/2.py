class Book:
  def __init__(self, title, pages):
    self.title = title
    self.pages = pages

  def __eq__(self, other):
    if isinstance(other, Book):
      return self.pages == other.pages
    return NotImplemented

  def __lt__(self, other):
    if isinstance(other, Book):
      return self.pages < other.pages
    return NotImplemented

  def __le__(self, other):
    if isinstance(other, Book):
      return self.pages <= other.pages
    return NotImplemented

  def __gt__(self, other):
    if isinstance(other, Book):
      return self.pages > other.pages
    return NotImplemented

  def __ge__(self, other):
    if isinstance(other, Book):
      return self.pages >= other.pages
    return NotImplemented

  def __ne__(self, other):
    if isinstance(other, Book):
      return self.pages != other.pages
    return NotImplemented

  def __repr__(self):
    return f"Book('{self.title}', {self.pages})"