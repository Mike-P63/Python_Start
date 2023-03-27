# Задача №41. 
# Дан массив, состоящий из целых чисел. Напишите
# программу, которая в данном массиве определит
# количество элементов, у которых два соседних и, при
# этом, оба соседних элемента меньше данного. Сначала
# вводится число N — количество элементов в массиве
# Далее записаны N чисел — элементы массива. Массив
# состоит из целых чисел.

from random import randint

def FilArray(arraySize):
    return [randint(1,10) for i in range (arraySize)]

len_array1 = int(input("Ввведите число элементов 1 массива:"))
array1 = FilArray(len_array1)
count = 0
print(*array1)
for i in range(1,len_array1-1):
    if array1[i-1]<array1[i]>array1[i+1]:  
        count+=1      

print(count)