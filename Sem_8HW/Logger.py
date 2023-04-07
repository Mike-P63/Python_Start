from Data_base import*

def inputText():
    lastname = lastname_data()     
    firstname = name_data()     
    phonenum = phone_data()   
    
    with open('tel_dir.txt',"a",encoding="utf-8") as file:      
        
        file.write(f"\n{lastname}\t{firstname}\t{phonenum}")    
  
    
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
    with open(new_phonebook, "r+", encoding="utf-8") as data:
        with open("tel_dir.txt", "a+", encoding="utf-8") as data_1:
            for line in data:
                if line not in data_1:
                    data_1.write(line)
            data_1.write("\n\n")
    print("Done!")


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
