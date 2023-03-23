from Main_3 import*

def all_square():
    n = int(input("Введите количество фигур: "))
    s = 0    
    for num_fig in range(n):
        plus_minus = input("- or + : ")
        symbol = 1
        if plus_minus == "-":
            symbol = -1
        fig = str(input("Введите фигуру т,п,к: "))
        if fig == "т":
            n = int(input("Введите ширину: "))
            m = int(input("Введите длину: "))
            s += symbol*rect(n,m)
        elif fig == "п":
            h = int(input('Введите ширину: '))
            m = int(input('Введите основание: '))
            s += symbol*tri(h,m)
        else:
            r = int(input("Введите радиус: ")) 
            s += symbol*circl(r)
    return s
print(all_square())

