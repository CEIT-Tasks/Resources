import scipy.optimize
import numpy as np

def function(x, a, b):
    return 2*x**2 - 7*x + 3 - a*x + b

def secant_method(a, b, eps=1e-4):
    x_old = 0.0
    x_new = 1.0
    i = 0
    while abs(x_new - x_old) > eps:
        x_old = x_new
        x_new = x_old - (function(x_old, a, b))/(2*(1-x_old**2))
        i += 1
    return round(x_new, 4)

a = float(input("Введите отделённый корень уравнения: "))
b = float(input("Введите свободный член уравнения: "))
print("Число итераций: ", secant_method(a, b))