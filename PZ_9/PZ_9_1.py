# Дан словарь с четным количеством элементов. Найти суммы значений
# элементов первой и второй половин с использованием функции. Результаты вывести
# на экран.

import random
a = int(input("Введите чётный размер словаря: "))

dict1 = {x: random.randint(-100, 100) for x in range(a)}
print(dict1)