# Дан список размера N. Переставить в обратном порядке элементы списка, расположенные
# между его минимальным и максимальным элементами, включая минимальный и максимальный
# элементы.

import random

d = int(input('Введите размер массива '))
List = []
t = 0
while t < d:
    List.append(random.randint(-100, 100))
    if List[t] % 2 == 0:
        k = List[t]
    t += 1

print('Исходный массив: ', List)
mi = min(List)
ma = max(List)
print('Минимальный элемент списка: ', mi, 'Максимальный элемент списка: ', ma)

mi_idx = List.index(mi)
ma_idx = List.index(ma) + 1
mi_idx, ma_idx = min(mi_idx, ma_idx), max(mi_idx, ma_idx)
End = List[0:mi_idx]+List[mi_idx:ma_idx][::-1]+List[ma_idx:]
print('Изменённый масив: ', End)