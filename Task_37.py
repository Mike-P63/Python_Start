# Задача №37. 

# Дано натуральное число N и
# последовательность из N элементов.
# Требуется вывести эту последовательность в
# обратном порядке.

# def max_new(n):
#     if n > 0:
#         print(n)
#         max_new(n-1)

# n = int(input("Введите число: "))
# max_new(n)



# Вар 1

def f(n):
    if n == 0:
        return ''
    k = int(input())
    return f(n - 1) + f' {k}'
#   return f(n-1) + ' ' + str(k)

n = int(input())
print(f(n)[1:])




# Вар 2

def f(n):
    if n == 0:
        return
    k = int(input())
    f(n-1)
    print(k, end=" ")

n = int(input())
f(n)

