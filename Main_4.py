# Калькулятор

def multiply(a,b):
    return a*b

def division(a,b):
    return a/b

def minus(a,b):
    return a - b

def summa(a,b):
    return a + b

def calc(primer):
    if primer[1] == "+":
        res = summa(float(primer[0]), float(primer[2]))
    elif primer[1] == "-":
        res = minus(float(primer[0]), float(primer[2]))
    elif primer[1] == "/":
        res = division(float(primer[0]), float(primer[2]))
    elif primer[1] == "*":
        res = multiply(float(primer[0]), float(primer[2]))    
    else:
        print("Неправильно ввели")
    return res

my_primer = input("Введите выражение: ").replace("+"," + ").replace("-"," - ").replace("*"," * ").replace("/"," / ").split()

while "/" in my_primer:
    i = my_primer.index("/")
    new_el = calc(my_primer[i-1:i+2])
    my_primer[i-1] = new_el
    del my_primer[i:i+2]
while "*" in my_primer:
    i = my_primer.index("*")
    new_el = calc(my_primer[i-1:i+2])
    my_primer[i-1] = new_el
    del my_primer[i:i+2]
while "-" in my_primer:
    i = my_primer.index("-")
    new_el = calc(my_primer[i-1:i+2])
    my_primer[i-1] = new_el
    del my_primer[i:i+2]
while "+" in my_primer:
    i = my_primer.index("+")
    new_el = calc(my_primer[i-1:i+2])
    my_primer[i-1] = new_el
    del my_primer[i:i+2]
print(*my_primer)

