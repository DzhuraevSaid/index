# i = 10
# while i != 0:
#     print('aziret', end = ",")
#     i -= 1
# list - списки - [1,2,3,'str',True]#изменяемый
# tuple - кортежи - (1,2,3,'str',True)#неизменяемый
# dict - словари - {
#     1:2,
#     3:'str',
#     'hello':True
# } #изменяемый
# set - множества -{3,4,5,4,3} #он хранит только уник.знач., изменяемый


# student = {1:'Aziret','age':55}
# stud2 = dict(name ="Aziret2", age=56)
# student[1] ='Radik'
# print(student[1])
# # print(stud2['name'], stud2['age'])


contact_name = {"Aidana":771404040, 'Aziret': 771404141, 'Almaz':404042, 'Baha': 771404043, 'Jaka':771404044, 'Maga':771404045}
while True:
    command = input("1 - создать \n2 - удалить \n3 - найти \n4 - все контакты \n")
    if command == '1':
        name = input("Name:")
        number = int(input("Num:"))
        contact_name.setdefault(name, number)
        print(f"Контакт {name} добавлен")
    elif command == '2':
        delete = input("Какой контакт вы хотите удалить:")
        if delete in contact_name:
            contact_name.pop(delete)
            print("Контакт удалён")
        else:
            print("Такого контакта нет")
    elif command == '3':
        find= input("Какой контакт вы хотите найти? ")
        title_find = find.title()
        if title_find in contact_name:
            print("Контакт найден")
            print(contact_name[title_find])
        else:
            print("Контакт не найден")
    elif command == '4':
        print(contact_name)
    else:
        print("Неверная команда")