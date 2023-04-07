from Logger import *  

def interface():
    print("""Выберите действие: 
    1 - Добавление, 
    2 - Поиск, 
    3 - Вывод на экран, 
    4 - Импорт в файл,
    5 - Редактирование,
    6 - Удаление,
    """)
    ask = int(input())
    if ask == 1:
        inputText()
    elif ask == 2:
        checkText(input("Введите данные: "))
    elif ask == 3:
        printText()
    elif ask == 4:
        import_file()
    elif ask == 5:
        change_data()
    elif ask == 6:
        del_data(input("Кого удаляем?: "))
    else:
        print("Такой команды не существует!")