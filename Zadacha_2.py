#Пользователь вводит число K - количество фруктов. Затем он вводит K фруктов в формате: название фрукта и его количество. Добавьте все фрукты в словарь, где название фрукта - это ключ, а количество - значение.
n = int(input('Введите колличество элементов в словаре: '))
frut_dict = {}

for i in range(n):
    key = input('Введите название фрукта: ')
    frut_dict[key] = input('Введите колличество: ')

print(frut_dict)
