class BankAccount:
    def __init__(self, initial_balance=0):
        self.balance = initial_balance
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"На счет внесено {amount}. Текущий баланс: {self.balance}")
        else:
            print("Сумма для внесения должна быть положительной")
    
    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Со счета снято {amount}. Текущий баланс: {self.balance}")
            else:
                print(f"Недостаточно средств. Доступно: {self.balance}")
        else:
            print("Сумма для снятия должна быть положительной")
    
    def get_balance(self):
        return self.balance