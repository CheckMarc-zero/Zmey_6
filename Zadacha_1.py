#Создайте список из случайных чисел. Найдите количество различных элементов в нем.
from random import randint
n = int(input('Введите колличество элементов списка: '))
a = int(input('Введите минимальное значение элементов списка: '))
b = int(input('Введите максимальное значение элементов списка: '))

random_list = [randint(a,b) for i in range(n)]
print(*random_list,sep=  ' ')

k = 0
for i in range(len(random_list)):
    if not random_list[i] in random_list[0:i]:
        k += 1
print(f'Количество различных элементов: {k}')  
      