# Задача №29. 
# Ваня и Петя поспорили, кто быстрее решит
# следующую задачу: “Задана последовательность
# неотрицательных целых чисел. Требуется определить
# значение наибольшего элемента
# последовательности, которая завершается первым
# встретившимся нулем (число 0 не входит в
# последовательность)”. Однако 2 друга оказались не
# такими смышлеными. Никто из ребят не смог до
# конца сделать это задание. Они решили так: у кого
# будет меньше ошибок в коде, тот и выиграл спор. За
# помощью товарищи обратились к Вам, студентам.


# n = int(input('Введите число: '))   
# max = n                             
# while n != 0:                       
#     n = int(input('Введите число: ')) 
#     if n > max:
#         max = n
# print(f'Максимальное число в введнной последовательности: {max}')



# n = int(input())
# max_number = 1000               1
# while n != 0:
#     n = int(input())             1
#     if max_number > n:           1
#         max_number = n
# print(max_number)


# n = int(input())
# max_number = -1          
# while n < 0:                1
#  n = int(input())         1
#  if max_number < n:        
#     n = max_number          1
# print(n)                       1

# Ваня
n = int(input())
max_number = n  # max_number = 1000  ошибка №1
while n != 0:
    if max_number < n: # if max_number > n: ошибка №2 
        max_number = n
    n = int(input()) # ошибка №3   
print(max_number)

# Петя
n = int(input())
max_number = -1
while n != 0: # while n < 0: ошибка №1
    if max_number < n:
        max_number = n # n = max_number ошибка №2
    n = int(input()) # ошибка №3   
print(max_number) # print(n) ошибка №4