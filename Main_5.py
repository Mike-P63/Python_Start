
# Задача 47
# У вас есть код, который вы не можете менять(так часто бывает, когда код в глубине
# программы используется множество раз и вы не хотите ничего сломать):
# transformation = <???>
# values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
# или любой другой список transormed_values = list(map(transformation, values))
# Единственный способ вашего взаимодействия с этим кодом - посредством задания
# функции transformation. Однако вы поняли, что для вашей текущей задачи вам не нужно
# никак преобразовывать список значений, а нужно получить его как есть.
# Напишите такое лямбда-выражение transformation, чтобы transformed_values получился
# копией values.
# Ввод:
# values = [1, 23, 42, ‘asdfg’]
# transformed_values = list(map(trasformation, values))
# if values == transformed_values:
#     print(‘ok’)
# else:
#     print(‘fail’)
# Вывод:
# ok



# transformation = lambda x: x                            # вводим в код строку, lambda (анонимную) функцию которая ничего не делает х=х
# values = [1, 23, 42, 'asdfg']                           # чтобы не писать return
# transformed_values = list(map(transformation, values))  #list функция, которая оборачивает в список работу map
#                                                         # если не поставить list, то выдаст объект map <map object at 0x000000B67783B070>                                                    
#                                                         # map применяет функцию transformation, на 
#                                                         # каждый элемент списка values
# if values == transformed_values:
#     print('ok')
# else:
#     print('fail')

# print(values)
# print(transformed_values)




# Задача №49. Решение в группах
# Ввод:
# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# print(*find_farthest_orbit(orbits))
# Вывод:
# 2.5 10




# def find_farthest_orbit(orbits):
#    pi = 3.14
#    orbits_new = [(0, 0)]
#    max = 0
#    for i in orbits:
#         if i[0] != i[1]:
#             if max < pi * i[0] * i[1]:
#                max = pi * i[0] * i[1]
#                orbits_new.pop()        # если выполняется условие, то удаляем предыдущее значение кортежа
#                orbits_new.append(i)    # и добавляем новое, чтобы в списке оставалась только одно, max
#    return orbits_new[0]                # добавили [0], чтобы распаковывался список


# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# print(*find_farthest_orbit(orbits))



# Задача №51.

# Напишите функцию same_by(characteristic, objects), которая
# проверяет, все ли объекты имеют одинаковое значение
# некоторой характеристики, и возвращают True, если это так.
# Если значение характеристики для разных объектов
# отличается - то False. Для пустого набора объектов, функция
# должна возвращать True. Аргумент characteristic - это
# функция, которая принимает объект и вычисляет его
# характеристику.

# Ввод:                            
# values = [0, 2, 10, 6]          
# if same_by(lambda x: x % 2, values):
# print(‘same’)
# else:
# print(‘different’)

# Вывод:same

# def same_by(charac, objects): # charac это lambda x: x % 2, objects это values
#     list_characteristic = [charac(i) for i in objects] # list comprehension - генератор списка
#     for i in range(len(list_characteristic) - 1):
#         if list_characteristic[i] != list_characteristic[i+1]:
#             return False
#         return True
    
# values = [0, 2, 10, 6]

# if same_by(lambda x: x % 2, values):
#     print('same')
# else:
#     print('different')



def f(words):
    return sum(1 for i in words if i in 'аеёиоуыэюя')
        
stih = "Хорошо-живет-на-свете-Винни-Пух! Оттого-поет-он-эти-Песни-вслух!"
stih2 = stih.lower().split()
print(stih2)
n = f(stih2[0])
print(n)
if all([f(i) == n for i in stih2]):
    print('Парам пам-пам')
else:
    print('Пам парам')