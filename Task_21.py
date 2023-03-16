# Задача №21. 
# Напишите программу для печати всех уникальных
# значений в словаре.
# Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
# {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII
# ":" S007 "}]
# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}


# List = [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
# n = set()
# for dict_i in List:
#     for key in dict_i:
#        n.add(dict_i[key])
# print(n)


data = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII ":" S007 "}]
unique_values = []
for el in data:
    for value in el.values():
        value = value.strip()  # удаляем лишние пробелы вокруг значений
        if value not in unique_values:
            unique_values.append(value)
print(set(unique_values))