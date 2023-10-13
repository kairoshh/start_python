# Массив №1
persons = [
    {
        'name': 'Bob',
        'age': 30,
        'country': 'USA'
    },
    {
        'name': 'John',
        'age': 39,
        'country': 'USA'
    },
    {
        'name': 'William',
        'age': 49,
        'country': 'France'
    },
    {
        'name': 'Andry',
        'age': 18,
        'country': 'France'
    },
    {
        'name': 'Sam',
        'age': 42,
        'country': 'Japan'
    },
    {
        'name': 'Jony',
        'age': 65,
        'country': 'Poland'
    },
    {
        'name': 'Jordan',
        'age': 23,
        'country': 'UK'
    },
    {
        'name': 'Nikita',
        'age': 35,
        'country': 'France'
    },
]

# Массив №2
# array = [
#     1,2,3,4,5,'a','b','c',6,7,'d','e',8,9,'f']


# TODO 1 Выведите имя самого старшего человека | массив №1

# TODO 2 Запишите в файл France.txt имя и возраст всех кто живет во Франции | массив №1

# TODO 3 Выведите в терминал средний возраст всех людей | массив №1

# TODO 4 Прочтите файл cars.txt и выведите в терминал все машины новее 2018 года

# TODO 5 Пройдитесь циклом по массиву №2 и запишите все числа в файл numbers.txt, а все буквы в letters.txt

# TODO 6 Запишите в файл year.txt год рождения и имя каждого человека учитывая что сейчас 2023 год | массив №1

# age = 0
# name = ' '
# for i in persons:
#     if i.get('age') > age:
#         age = i.get('age')
#         name = i.get('name')

# print(name, age)

# for i in persons:
#     if i.get('country') == 'France':
#         with open('france.txt', 'a') as f:
#             f.write(f'{i.get("name")}\n')

# age = 0 
# for i in persons:
#     age += i.get('age')
# print(age/len(persons))
# year = 2018
# with open ('cars.txt', 'r') as f:
#     for line in f.readlines():
#         a = line.split(', ')
#         if int(a[2]) > year:
#             print(a[0], a[1], a[2] )

# for i in array:
#     if type(i) == int:
#         with open ('numbers.txt', 'a') as num:
#             num.write(f'{i}\n')
#     else:
#         with open ('letters.txt', 'a') as let:
#             let.write(f'{i}\n')

# year = 2023 
# for person in persons:
#     birth_year = year - person['age']
#     with open('year.txt', 'a') as file:
#         file.write(f'Name: {person["name"]}, Birth year: {birth_year}\n')
