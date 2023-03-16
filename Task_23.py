# Задача №23. 
# Дан массив, состоящий из целых чисел. Напишите
# программу, которая подсчитает количество
# элементов массива, больших предыдущего (элемента
# с предыдущим номером)
# Input: [0, -1, 5, 2, 3]
# Output: 2 (-1 < 5, 2 < 3)

# 
# a = map(int, input("Введите числа списка: ").split())
# a = list(a)
# k = 0
# for i in range(1, len(a)):
#     if a[i] > a[i - 1]:
#         k += 1
# print("Количество элементов, больше предыдущего = ", k)



from random import randint
n = int(input())
numbers = [randint(0, 10) for _ in range(n)]
print(numbers)

count = 0
for i in range(len(numbers)-1):
    if numbers[i]<numbers[i+1]:
        count+=1
print(count)

