# # Задача №13. Пользователь вводит число N (1 ≤ N ≤ 10). 
# Далее построчно N чисел от -50 до 50. 
# Нужно вывести наибольшее количество идущих 
# подряд положительных чисел.

# Input:    6 -> -20 30 -40 50 10 -10 20 30 40
# Output: 2

n = int(input("Введите количество дней периода: "))
count_temp = 0
count_max = 0
for i in range(1, n+1):
    tempr = int(input("Введите среднюю температуру в каждый день: "))
    if tempr > 0:
        count_temp += 1
    else:         
        if count_max < count_temp:
            count_max = count_temp
        count_temp = 0
if count_max < count_temp:
    count_max == count_temp
print(count_max)

            
n = int(input("Введите количество дней периода: "))
count_temp = 0
count_max = 0
for i in range(n):
    tempr = randint(-50, 50)
    print(tempr)
    if tempr > 0:
        count_temp += 1
    elif count_temp != 0:         
        if count_max < count_temp:
            count_max = count_temp
        count_temp = 0
if count_max < count_temp:
    count_max = count_temp
print(count_max)

