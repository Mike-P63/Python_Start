# Задача 49
# Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt.
# Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в текстовом файле
# 3. Пользователь может ввести одну из характеристик для поиска определенной записи
#    (например имя или фамилию человека)
# 4. Использование функций. Ваша программа не должна быть линейной
# '''

def inputText():
    with open('tel_dir.txt', 'a', encoding="utf-8") as data:
        surname = data.write(input('Введите фамилию: '))
        data.write(' ')
        name = data.write(input('Введите имя: '))
        data.write(' ')
        fathername = data.write(input('Введите отчество: '))
        data.write(' ')
        phoneNumber = data.write(input('Введите номер телефона: '))
        data.write('\n\n')

def printText():
    print()
    with open('tel_dir.txt', 'r') as data:
        for line in data:
            print(line)
        print()


def checkText(userInfo):
    print()
    with open('tel_dir.txt', 'r') as data:
        for line in data.readlines():
            if userInfo in line:
                print(line)
        print()


def import_file():
    new_phonebook = input("Введите ссылку: ")
    with open(new_phonebook, "r", encoding="utf-8") as data:
        with open("tel_dir.txt", "a+", encoding="utf-8") as data_1:
            for line in data:
                if line not in data_1:
                    data_1.write(line)
            data_1.write("\n")


def change_data():
    line_str=input("Введите запись, которую нужно изменить: ")          
    with open("tel_dir.txt", "r+", encoding="utf-8") as f:     
        lines=f.readlines()
        with open("tel_dir.txt", "w+", encoding="utf-8") as f1:     
            for line in lines:
                if line_str not in line:
                    f1.write(line)  
                else :
                    ask=input("Что хотите поменять (1-Фамилия,2-Имя,3-Телефон) : ")
                    while ask not in ("1","2","3"):
                        print("ввод некорректный")
                        ask=input("Что хотите поменять (1-Фамилия,2-Имя,3-Телефон) : ")
                    new_data=input("Введите новые данные : ")    
                    line_list=line.split()
                    line_list[int(ask)-1]=new_data
                    f1.write("\t".join(line_list)+"\n")
    print("Done!")  


def del_data(name):                       
    with open("tel_dir.txt", "r+") as f:
        lines = f.readlines()
    with open("tel_dir.txt", "w+") as f1:
        for line in lines:
            if name not in line:
                f1.write(line)
            else:
                print(line)
                ask=input("Желаете удалить эту строку (y,n): ") # Спрашиваем пользователя если абонентов несколько
                while ask not in ("y","n"):
                    print("Ввод некорректный, ")
                    ask=input("Желаете удалить эту строку (y,n): ")
                if ask=="n":
                   f1.write(line)
    print("Delited")


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
    old_data = input('кого хотим переименовать?: ')
    new_data = input('как хотим его назвать?: ')
    change_data(new_data, old_data)
elif ask == 6:
    del_data(input("Кого удаляем?: "))
else:
    print("Такой команды не существует!")






# От Дмитрия:

# def writing_person():
#     lastname = input("фамилия: ")
#     name = input("имя: ")
#     surname = input("отчество: ")
#     tel = input("телефон: ")
#     data = open("new_phonebook.txt", "a", encoding="utf-8")
#     data.writelines(
#         f"фамилия:{lastname} имя:{name} отчество:{surname} телефон:{tel}\n\n")
#     data.close()


# def search():
#     lookfor = input("кого ищем? ")
#     with open("new_phonebook.txt", "r", encoding="utf-8") as data:
#         for line in data:
#             if lookfor in line:
#                 print(line)


# def print_phonebook():
#     with open("new_phonebook.txt", "r", encoding="utf-8") as data:
#         for line in data:
#             print(line)


# def load():
#     new_phonebook = input("Введите ссылку: ")
#     with open(new_phonebook, "r+", encoding="utf-8") as data:
#         with open("tel_dir.txt", "a+", encoding="utf-8") as data_1:
#                 for line in data:
#                     if line not in data_1.readlines():
#                         data_1.write(line)
#                 data_1.write("\n")


# print("""Выберите действие:
# 1 - Добавление,
# 2 - Поиск,
# 3 - Вывод на экран,
# 4 - Импорт в файл,
# """)
# ask = int(input())
# if ask == 1:
#     writing_person()
# elif ask == 2:
#     search()
# elif ask == 3:
#     print_phonebook()
# elif ask == 4:
#     load()
# else:
#     print("Такой команды не существует!")


# def user_action(phonebook):
#     while True:
#         print('Что вы хотите сделать?')
#         user_choice = input('1 - Импортировать данные\n2 - Найти контакт\n3 - Добавить контакт\n\
# 4 - Изменить контакт\n5 - Удалить контакт\n6 - Просмотреть все контакты\n0 - Выйти из приложения\n')
#         print()
#         if user_choice == '1':
#             file_to_add = input('Введите название импортируемого файла: ')
#             import_data(file_to_add, phonebook)
#         elif user_choice == '2':
#             contact_list = read_file_to_dict(phonebook)
#             find_number(contact_list)
#         elif user_choice == '3':
#             add_phone_number(phonebook)
#         elif user_choice == '4':
#             change_phone_number(phonebook)
#         elif user_choice == '5':
#             delete_contact(phonebook)
#         elif user_choice == '6':
#             show_phonebook(phonebook)
#         elif user_choice == '0':
#             print('До свидания!')
#             break
#         else:
#             print('Неправильно выбрана команда!')
#             print()
#             continue


# def import_data(file_to_add, phonebook):
#     with open(file_to_add, 'r', encoding='utf-8') as new_contacts, open(phonebook, 'a', encoding='utf-8') as file:
#             contacts_to_add = new_contacts.readlines()
#             file.writelines(contacts_to_add)


# def read_file_to_dict(file_name):
#     with open(file_name, 'r', encoding='utf-8') as file:
#         lines = file.readlines()
#     headers = ['Фамилия', 'Имя', 'Номер телефона']
#     contact_list = []
#     for line in lines:
#         line = line.strip().split()
#         contact_list.append(dict(zip(headers, line)))
#     return contact_list


# def read_file_to_list(file_name):
#     with open(file_name, 'r', encoding='utf-8') as file:
#         contact_list = []
#         for line in file.readlines():
#             contact_list.append(line.split())
#     return contact_list


# def search_parameters():
#     print('По какому полю выполнить поиск?')
#     search_field = input('1 - по фамилии\n2 - по имени\n3 - по номеру телефона\n')
#     print()
#     search_value = None
#     if search_field == '1':
#         search_value = input('Введите фамилию для поиска: ')
#         print()
#     elif search_field == '2':
#         search_value = input('Введите имя для поиска: ')
#         print()
#     elif search_field == '3':
#         search_value = input('Введите номер для поиска: ')
#         print()
#     return search_field, search_value


# def find_number(contact_list):
#     search_field, search_value = search_parameters()
#     search_value_dict = {'1': 'Фамилия', '2': 'Имя', '3': 'Номер телефона'}
#     found_contacts = []
#     for contact in contact_list:
#         if contact[search_value_dict[search_field]] == search_value:
#             found_contacts.append(contact)
#     if len(found_contacts) == 0:
#         print('Контакт не найден!')
#     else:
#         print_contacts(found_contacts)
#     print()


# def get_new_number():
#     last_name = input('Введите фамилию: ')
#     first_name = input('Введите имя: ')
#     phone_number = input('Введите номер телефона: ')
#     return last_name, first_name, phone_number


# def add_phone_number(file_name):
#     info = ' '.join(get_new_number())
#     with open(file_name, 'a', encoding='utf-8') as file:
#         file.write(f'{info}\n')


# def show_phonebook(file_name):
#     list_of_contacts = sorted(read_file_to_dict(file_name), key=lambda x: x['Фамилия'])
#     print_contacts(list_of_contacts)
#     print()
#     return list_of_contacts


# def search_to_modify(contact_list: list):
#     search_field, search_value = search_parameters()
#     search_result = []
#     for contact in contact_list:
#         if contact[int(search_field) - 1] == search_value:
#             search_result.append(contact)
#     if len(search_result) == 1:
#         return search_result[0]
#     elif len(search_result) > 1:
#         print('Найдено несколько контактов')
#         for i in range(len(search_result)):
#             print(f'{i + 1} - {search_result[i]}')
#         num_count = int(input('Выберите номер контакта, который нужно изменить/удалить: '))
#         return search_result[num_count - 1]
#     else:
#         print('Контакт не найден')
#     print()


# def change_phone_number(file_name):
#     contact_list = read_file_to_list(file_name)
#     number_to_change = search_to_modify(contact_list)
#     contact_list.remove(number_to_change)
#     print('Какое поле вы хотите изменить?')
#     field = input('1 - Фамилия\n2 - Имя\n3 - Номер телефона\n')
#     if field == '1':
#         number_to_change[0] = input('Введите фамилию: ')
#     elif field == '2':
#         number_to_change[1] = input('Введите имя: ')
#     elif field == '3':
#         number_to_change[2] = input('Введите номер телефона: ')
#     contact_list.append(number_to_change)
#     with open(file_name, 'w', encoding='utf-8') as file:
#         for contact in contact_list:
#             line = ' '.join(contact) + '\n'
#             file.write(line)


# def delete_contact(file_name):
#     contact_list = read_file_to_list(file_name)
#     number_to_change = search_to_modify(contact_list)
#     contact_list.remove(number_to_change)
#     with open(file_name, 'w', encoding='utf-8') as file:
#         for contact in contact_list:
#             line = ' '.join(contact) + '\n'
#             file.write(line)


# def print_contacts(contact_list: list):
#     for contact in contact_list:
#         for key, value in contact.items():
#             print(f'{key}: {value:12}', end='')
#         print()


# if __name__ == '__main__':
#     file = 'Phonebook.txt'
#     user_action(file)
