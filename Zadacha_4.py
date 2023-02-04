#Пользователь вводит число N. Затем он вводит личные данные (имя и возраст) своих N друзей. Создайте список friends и добавьте в него N словарей с ключами name и age. Выведите средний возраст всех друзей и самое длинное имя.

n = int(input('Введите колличество друзей: '))
list_friends = []
list_age = []

for i in range(n):
    list_friends.append(input('Введите имя: '))
    list_age.append(int(input('Введите возраст: ')))

frands_age = dict(zip(list_friends,list_age))
print(frands_age)

middle_age = 0
for value in frands_age.values():
    middle_age += value
print(f'Средний возраст: {middle_age/len(frands_age)}')

longest_name = ''
for key in frands_age:
    if len(longest_name) < len(key): 
        longest_name = key
print(f'Самое длинное имя: {longest_name}')
