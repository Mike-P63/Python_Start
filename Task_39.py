# Задача 39:
# Даны два массива чисел. Требуется вывести те элементы
# первого массива (в том порядке, в каком они идут в первом
# массиве), которых нет во втором массиве. Пользователь вводит
# число N - количество элементов в первом массиве, затем N
# чисел - элементы массива. Затем число M - количество
# элементов во втором массиве. Затем элементы второго массива

# a = [int(input('Введите элемент массива А: ')) for i in range(int(input('Ввведите количество элементов массива А = ')))]
# b = [int(input('Введите элемент массива Б: ')) for i in range(int(input('Ввведите количество элементов массива Б = ')))]
# c = [i for i in a if i not in b]
# print("Элементы массива А, которых нет в массиве Б -> ", *c)


from random import randint
def FilArray(arraySize):
    array = []
    for i in range (arraySize):
        num = randint(1,10)
        array.append(num)
    return array


def Find_Number(array1, array2):
    for i in range(len_array1):
        if array1[i] not in array2:
            print(array1[i], end=" ")

len_array1 = int(input("Ввведите число элементов 1 массива:"))
my_array1 = FilArray(len_array1)
len_array2 = int(input("Ввведите число элементов 2 массива:"))
my_array2 = FilArray(len_array2)
Find_Number(my_array1, my_array2)




# n = int(input('Введите кол-во элементов массива А:  '))
# a = {randint(1,10) for i in range (n)}
# print(*a)

# m = int(input('Введите кол-во элементов массива B:  '))
# b = []
# for i in range(m):
#     b.append(randint(1, 10))
# print(*b)

# c = (a.difference(b))
# print("Элементы массива А, которых нет в массиве Б -> ", *c,  end = ";")



