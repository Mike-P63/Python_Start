# В некоторой школе решили набрать три новых
# математических класса и оборудовать кабинеты для
# них новыми партами. За каждой партой может сидеть
# два учащихся. Известно количество учащихся в
# каждом из трех классов. Выведите наименьшее
# число парт, которое нужно приобрести для них.

#Input: 20 21 22(ввод чисел НЕ в одну строку)
#32

a = int(input("Enter a class pupils quantity = "))
b = int(input("Enter b class pupils quantity = "))
c = int(input("Enter c class pupils quantity = "))
print("Min tables quantity = ", ((a+1)//2 +(b+1)//2 +(c+1)//2))


#result = math.ceil(class1 / 2) + math.ceil(class2 / 2) +  math.ceil(class3 / 2)