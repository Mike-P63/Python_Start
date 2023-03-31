# Задача №49. 
# Ввод:
# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# print(*find_farthest_orbit(orbits))
# Вывод:
# 2.5 10

# def find_farthest_orbit(orbits):
#    orbits_new = [(0, 0)]
#    max = 0
#    for i in orbits:
#         if i[0] != i[1]:
#             if max < i[0] * i[1]:
#                max = i[0] * i[1]
#                orbits_new.pop()        
#                orbits_new.append(i)    
#    return orbits_new[0] 

# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# print(*find_farthest_orbit(orbits))





orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]

def find_farthest_orbit(orbits):
    # orbits = list(filter(lambda x:x[0]!=x[1],orbits))
    # s = list(map(lambda x: x[0]*x[1],orbits))
    # large = s.index(max(s))
    # return orbits[large]
    i_max = 0
    s_max = 0
    for i, elem in enumerate(orbits):
        if elem[0]!=elem[1] and s_max<elem[0]*elem[1]:
            s_max = elem[0]*elem[1]
            i_max = i
    return orbits[i_max]

print(*find_farthest_orbit(orbits))
