#Пользователь вводит число N. Затем он вводит личные данные (имя и возраст) своих N друзей. Создайте список friends и добавьте в него N словарей с ключами name и age. Найдите самого младшего из друзей и выведите его имя.

n = int(input('Введите колличество друзей: '))
list_friends = []
list_age = []

for i in range(n):
    list_friends.append(input('Введите имя: '))
    list_age.append(int(input('Введите возраст: ')))

frands_age = dict(zip(list_friends,list_age))
print(frands_age)

min = max(list_age)
name = ''
for key in frands_age:
    if frands_age[key]<min:
        min = frands_age[key]
        name = key

print(f'Самый младший: {name}')
