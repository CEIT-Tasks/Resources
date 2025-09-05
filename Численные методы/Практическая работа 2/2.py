
number = int(input("Введите число: "))
initnum = number
summ = 0
product = 1

# Определяем значения суммы и произведения
while number > 0:
    digit = number % 10
    summ += digit
    product *= digit
    number //= 10

print(f"Сумма цифр числа {initnum} равна {summ}")
print(f"Произведение цифр числа {initnum} равна {product}")