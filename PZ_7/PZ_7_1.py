# Дано целое число N (1<N<26). Вывести N первых прописных (то есть заглавных) букв латинского
# алфавита.

import random

N = random.randrange(1, 26)
print('N = ', N)

for i in range(N):
    print(chr(ord('A')+i), end=" ")