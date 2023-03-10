# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы
# расплачивались за проезд и получали билет с номером. Счастливым
# билетом называют такой билет с шестизначным номером, где сумма
# первых трех цифр равна сумме последних трех. Т.е. билет с номером
# 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать
# программу, которая проверяет счастливость билета.

# 385916 -> yes
# 123456 -> no


# n = int(input("Введите шестизначный номер билета: "))
# a = n % 10
# n = n // 10
# b = n % 10
# n = n // 10
# c = n % 10
# n = n // 10
# d = n % 10
# n = n // 10
# e = n % 10
# n = n // 10
# if (a+b+c) == (d+e+n):
#     print("Билет счастливый")
# else:
#     print("Билет не счастливый")

#Вариант с данными str:

n = input('Введите шестизначный номер билета: ')
if len(n) != 6:
    print(f'Число {n} не шестизначное')
else:
    n1 = int(n[0]) + int(n[1]) + int(n[2])
    n2 = int(n[3]) + int(n[4]) + int(n[5])
    if n1 == n2:
        print('Билет счастливый')
    else:
        print('Билет не счастливый')    