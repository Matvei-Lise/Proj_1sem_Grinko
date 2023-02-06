# В последовательности на n целых чисел умножить элементы до n-1 на элемент n.

import random

n = int(input("Введите количество элементов в последовательности: "))
sequence = []

t = 0
while t < n:
    sequence.append(random.randint(-100, 100))
    t += 1
print("Старый список:  ",sequence)
mul = sequence[n-1]
sequence = (list(map(lambda x: x*mul, sequence)))
del sequence[n-1]
sequence.append(mul)
print("Новый список:  ", sequence)
