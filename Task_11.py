# Дано натуральное число A > 1. Определите, каким по
# счету числом Фибоначчи оно является, то есть
# выведите такое число n, что φ(n)=A. Если А не
# является числом Фибоначчи, выведите число -1.
# Input: 5
# Output: 6 

a = int(input("Введите число а, больше чем 1:  "))
N1 = 0
#N2 = 1
result = 1
i = 2
while result < a:
    N1, result  = result, N1 + result 
    # N1 = N2
    # N2 = result
    i += 1     
if result == a:
    print(i)
else:
    print(-1)   




numberA = int(input('Введите число: '))
count = 2
number0 = 0
number1 = 1
key = True
while key:
    numberFibonacci = number0 + number1
    if numberFibonacci < numberA:
        number0 = number1
        number1 = numberFibonacci
        count += 1
    elif numberFibonacci == numberA:
        count += 1
        key = False
    else:
        count = -1
        key = False
print(count)  
