#"Пора учить английский язык", - сказал себе Степа и решил написать программу для изучения английского языка. Программа получает на вход слово на английском языке и несколько его переводов на русском языке. Составьте словарь, в котором ключ - это английское слово, а значение - это список русских слов. В этой задаче нужно использовать строчный метод split().

n = int(input('Введите колличество слов в словаре: '))
list_ing = []
list_russian = []

for i in range(n):
    list_ing.append(input('Введите слово на английском: '))
    list_russian.append(input('Введите несколько вариантов перевода через пробел: ').split())

translate_dict = dict(zip(list_ing,list_russian))
print(translate_dict)
