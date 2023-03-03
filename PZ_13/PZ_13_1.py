# В квадратной матрице все элементы, не лежащие на главной диагонали увеличить в
# 2 раза.

from random import randint

n = 3
arr = [[randint(1, 20) for _ in range(n)] for _ in range(n)]
print(*arr, sep='\n', end='\n\n')

for i in range(n):
    for j in range(n):
        if i < j:
            arr[i][j] = arr[i][j]*2
        elif i > j:
            arr[i][j] = arr[i][j]*2

print(*arr, sep='\n', end='\n\n')