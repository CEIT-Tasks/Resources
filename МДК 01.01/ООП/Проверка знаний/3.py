class User:
  def __init__(self, name: str, age: int, address: str):
    self.__name = name
    self.__age = age
    self.__address = address
    
  def get_name(self):
    return self.__name

  def get_age(self):
    return self.__age

  def get_address(self):
    return self.__address

  def set_name(self, name):
    self.__name = name

  def set_age(self, age):
    self.__age = age

  def set_address(self, address):
    self.__address = address
    
  def update_info(self, *args):
    if len(args) == 1 and isinstance(args[0], int):
      self.__age = args[0]
    elif len(args) == 2 and isinstance(args[0], str) and isinstance(args[1], int):
      self.__name = args[0]
      self.__age = args[1]
    elif len(args) == 3 and isinstance(args[0], str) and isinstance(args[1], int) and isinstance(args[2], str):
      self.__name = args[0]
      self.__age = args[1]
      self.__address = args[2]
    else:
      raise ValueError("Неверные аргументы для обновления информации пользователя.")

  def __str__(self):
    return f"User(name={self.__name}, age={self.__age}, address={self.__address})"