#Средствами языка Python сформировать текстовый файл (.txt), содержащий
#последовательность из целых положительных и отрицательных чисел. Сформировать
#новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую
#обработку элементов:
#Исходные данные:
#Количество элементов:
#Минимальный элемент:
#Элементы, умноженные на первый максимальный элемент:

l = ['83 -35 -21 12 24 -1 6 93 -71']
f11 = open('data_11.txt', 'w')
f11.writelines(l)
f11.close()

f12 = open('data_12.txt', 'w')
f12.write('Исходные данные:  ')
f12.writelines(l)
f12.close()

f11 = open('data_11.txt')
k = f11.read()
k = k.split()
for i in range(len(k)):
    k[i] = int(k[i])
f11.close()

f11 = open('data_11.txt')
min = 0
for i in range(len(k)):
    min = min if min < k[i] else k[i]
max = max(k)
lm = []
for i in range(len(k)):
    a = k[i]*max
    lm.append(str(a))
result = " ".join(lm)
f11.close()

f12 = open('data_12.txt', 'a')
f12.write('\n')
print('Количество элементов: ', len(k),'\n' 'Минимальный элемент: ', min,
      '\n' 'Элементы, умноженные на первый максимальный элемент: ', result, file=f12)
f12.close()