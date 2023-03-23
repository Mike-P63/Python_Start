# Задача №33. 

# Хакер Василий получил доступ к классному журналу и
# хочет заменить все свои минимальные оценки на
# максимальные. Напишите программу, которая
# заменяет оценки Василия, но наоборот: все
# максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1

# from random import randint
# n = int(input('Введите кол-во оценок бестолкового Василия:  '))
# a = [randint(1,5) for i in range (n)]
# print(*a)
# max_point = max(a)
# min_point = min(a)
# print(max(a))
# print(min(a))
# for i in range(len(a)):
#     if a[i] == max_point:
#             a[i] = min_point 
# print(*a)




from random import randint
def magazin(n):
    array = [randint(1,5) for i in range (n)]
    print(array)
    return array

def minmax(array):
    small = min(array)
    large = max (array)
    for i in range(len(array)-1):
          if array[i]==large:
               array[i] = small
    return array

arraynew = magazin(10)
print(minmax(arraynew))