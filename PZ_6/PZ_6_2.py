#Дан список размера N. Найти номер его последнего локального максимума.

import random

d = int(input('Введите размер массива'))
List = []
t = 0
while t < d:
    List.append(random.randint(-100, 100))
    if List[t] % 2 == 0:
        k = List[t]
    t += 1

print('Исходный массив: ', sep='\n')
print(List)
b = min(List)
print('Минимальный элемент списка: ', min(List))
print(list.index(b))