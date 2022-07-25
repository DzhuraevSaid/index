# animals = {'crocodil','begemot','jiraf','begemot'}
# print(animals)


# list_names = ['Aza','Kuma','Buma','Anna','Vika']
# get_names = ['Kuma','Anna','Adilet','Sasha']
# #2new_list = list(set(list_names)-set(get_names))
# #3new_list = list(set(list_names)^set(get_names))
# nw_list = list(set(list_names) & set(get_names))
# print(nw_list)

# # my_str = "frg5gth57ubdfh67 sbf4dsbdr0dxbf 2"
# # s = []
# # for i in list(my_str):
# #     if i.isdigit():
# #         s += i
# # print(list(s))




#У вас есть словарь студентов  IT Academy:






students = [
    {'name': 'Mark', 'age': 18, 'course': 'java', 'gender': 'Male'},
    {'name': 'John', 'age': 15, 'course': 'python', 'gender': 'Male'},
    {'name': 'Andrew', 'age': 20, 'course': 'javascript', 'gender': 'Male'},
    {'name': 'Marcus', 'age': 25, 'course': 'java', 'gender': 'Male'},
    {'name': 'Agnes', 'age': 40, 'course': 'python', 'gender': 'Female'},
    {'name': 'Doe', 'age': 42, 'course': 'java', 'gender': 'Male'},
    {'name': 'Michael', 'age': 17, 'course': 'javascript', 'gender': 'Male'},
    {'name': 'Jennifer', 'age': 16, 'course': 'java', 'gender': 'Female'},
    {'name': 'Angela', 'age': 16, 'course': 'python', 'gender': 'Female'},
    {'name': 'Eniston', 'age': 34, 'course': 'java', 'gender': 'Male'},
    {'name': 'Albert', 'age': 33, 'course': 'javascript', 'gender': 'Male'},
    {'name': 'Nash', 'age': 28, 'course': 'python', 'gender': 'Male'},
    {'name': 'Nicolas', 'age': 19, 'course': 'java', 'gender': 'Male'},
    {'name': 'Alex', 'age': 21, 'course': 'java', 'gender': 'Male'},
    {'name': 'Martin', 'age': 22, 'course': 'python', 'gender': 'Male'},
    {'name': 'Gloria', 'age': 23, 'course': 'java', 'gender': 'Female'},
    {'name': 'Mikkel', 'age': 24, 'course': 'python', 'gender': 'Male'},
    {'name': 'Susann', 'age': 25, 'course': 'javascript', 'gender': 'Female'},
    {'name': 'Steve', 'age': 26, 'course': 'python', 'gender': 'Male'},
    {'name': 'Mark', 'age': 18, 'course': 'java', 'gender': 'Male'},
    {'name': 'Johnathan', 'age': 15, 'course': 'python', 'gender': 'Male'},
    {'name': 'Aidin', 'age': 20, 'course': 'javascript', 'gender': 'Male'},
    {'name': 'Mirbek', 'age': 25, 'course': 'java', 'gender': 'Male'},
    {'name': 'Atay', 'age': 42, 'course': 'java', 'gender': 'Male'},
    {'name': 'Chyngyz', 'age': 17, 'course': 'javascript', 'gender': 'Male'},
    {'name': 'Aigerim', 'age': 16, 'course': 'java', 'gender': 'Female'},
    {'name': 'Jyldyz', 'age': 16, 'course': 'python', 'gender': 'Female'},
    {'name': 'Emir', 'age': 34, 'course': 'java', 'gender': 'Male'},
    {'name': 'Emirlan', 'age': 12, 'course': 'javascript', 'gender': 'Male'},
    {'name': 'Nursultan', 'age': 13, 'course': 'python', 'gender': 'Male'},
    {'name': 'Aliaskar', 'age': 19, 'course': 'java', 'gender': 'Male'},
    {'name': 'Aktan', 'age': 21, 'course': 'java', 'gender': 'Male'},
    {'name': 'Adyl', 'age': 14, 'course': 'python', 'gender': 'Male'},
    {'name': 'Gloria', 'age': 23, 'course': 'java', 'gender': 'Female'},
    {'name': 'Janyl', 'age': 16, 'course': 'python', 'gender': 'Female'},
    {'name': 'Meerim', 'age': 12, 'course': 'javascript', 'gender': 'Female'},
    {'name': 'Sultan', 'age': 13, 'course': 'python', 'gender': 'Male'},
]

#1) высните процентное соотношение мужского пола и женского.

#2) выведите всех студентов с курса python


#3) уберите дубликаты

a = 'python'
if a in students:
    students.pop(a)
print (students)

#4) выведите студентов, которые старше 30 и найдите процент их количества относительно других

#5) отсортируйте студентов по:
        # имени
        # курсу
        # полу
        # возрасту

#6) все студенты курса  javascript  перешли на курс  python.  Как вы поменяете это в словаре ?
# Напишите код



#7) Добавьте по 5 новых студентов на курсы  java  и  python

#8) Отчислите всех студентов младше 15 лет