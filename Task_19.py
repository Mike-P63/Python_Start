# Задача №19. Решение в группах
# Дана последовательность из N целых чисел и число
# K. Необходимо сдвинуть всю последовательность
# (сдвиг - циклический) на K элементов вправо, K –
# положительное число.
# Input: [1, 2, 3, 4, 5] k = 3
# Output: [4, 5, 1, 2, 3]

numbers = [1,2,3,4,5]
print(numbers)
step = int(input("Введите число, на которое будет произведен сдвиг: ")) %len(numbers)
for i in range(step-1):
    numbers.insert(0, numbers.pop())
print(numbers)



# numbers = [1, 2, 3, 4, 5]
# k = int(input("Введите число для сдвига элементов: "))
# k = k%len(numbers)
# print(numbers[k:]+ numbers[:k])