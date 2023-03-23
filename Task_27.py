# Задача №27. 
# Пользователь вводит текст(строка). Словом считается
# последовательность непробельных символов идущих
# подряд, слова разделены одним или большим числом
# пробелов. Определите, сколько различных слов
# содержится в этом тексте.
# Input: She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells
# Output: 13

tekst = (input('Введите символы строки через пробел: ').lower().split())  
tekst_2 = set()         
for i in tekst:
    tekst_2.add(i)    # заполняем множество уникальными словами
print(len(tekst_2))