# Если в матрице имеются положительные элементы, то вывести TRUE, иначе FALSE.
# import numpy as np

arr1 = [[0, -4, -1], [2, 4, -5],
        [-3, 33, 83], [-5, -5, -5]]

arr2 = [[0, -7, -3], [-52, -4, -5],
        [-37, -9, -3], [-9, -8, -7]]
print(*arr1, sep='\n', end='\n\n')

def contains_1(arr):
    x = False
    for row in arr:
        for element in row:
            if element > 0:
                x = True
    print(x)

print(contains_1(arr1))
print(" ", *arr2, sep='\n', end='\n\n')
print(contains_1(arr2))