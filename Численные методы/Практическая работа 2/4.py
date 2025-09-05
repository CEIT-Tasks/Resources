try:
    number = int(input("Введите число: "))
except ValueError:
    print("Ошибка: некорректное число")
    
if number > 1:
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            print("Нет")
            break
    else:
        print("Да")
