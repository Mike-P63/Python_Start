# Задача 28: 

# Напишите рекурсивную функцию sum(a, b),
# возвращающую сумму двух целых неотрицательных чисел. Из
# всех арифметических операций допускаются только +1 и -1.
# Также нельзя использовать циклы.


def AsumB(a,b):
    if b == 0:
        return a
    return 1 + AsumB(a,b-1) 
a = int(input("Введите число а: "))
b = int(input("Введите число б: "))
print(AsumB(a,b))
