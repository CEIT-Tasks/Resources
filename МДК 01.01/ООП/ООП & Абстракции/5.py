class Product:
  def __init__(self, name, price, quantity):
    self.name = name
    self.price = price
    self.quantity = quantity
    
  def decrease_quantity(self, amount):
    if amount > self.quantity:
      raise ValueError("Cannot decrease quantity below zero")
    self.quantity -= amount
    
  def change_price(self, new_price):
    if new_price < 0:
      raise ValueError("Price cannot be negative")
    self.price = new_price
    
class ShoppingCart(Product):
  def __init__(self):
    self.items = []
    
  def add_item(self, product):
    if not isinstance(product, Product):
      raise TypeError("Only Product instances can be added")
    self.items.append(product)
      
  def total_price(self):
    return sum(item.price * item.quantity for item in self.items)