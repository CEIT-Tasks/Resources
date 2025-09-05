print("Введите число: ")

try:
    number = int(input())
except ValueError:
    print("Ошибка: некорректное число")

even = 0
uneven = 0

while number > 0:
    digit = number % 10
    if digit % 2 == 0:
        even += 1
    else:
        uneven += 1
    number //= 10

print("Чётных: ", even)
print("Нечётных: ", uneven)
