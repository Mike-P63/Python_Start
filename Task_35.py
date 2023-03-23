# Задача №35. 
# Напишите функцию, которая принимает одно число и
# проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое
# имеет 2 делителя: 1 и n(само число)
# Input: 5
# Output: yes


def check_number(n):
    if n==1:
        return "No"
    for i in range (2, n-1):
        if n%i == 0:
            return "No"
    return "Yes"
print(check_number(int(input("Число = ")))) 

    
