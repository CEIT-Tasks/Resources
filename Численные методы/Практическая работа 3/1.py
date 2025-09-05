from math import factorial

number = 0

try:
    number = int(input())
except ValueError:
    if number <= 0:
        exit()

print(factorial(number))