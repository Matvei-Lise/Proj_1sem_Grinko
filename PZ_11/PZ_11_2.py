#Из предложенного текстового файла (text18-4.txt) вывести на экран его
#содержимое, количество символов, принадлежащих к группе букв.
#Сформировать новый файл, в который поместить текст в стихотворной форме
#предварительно заменив символы верхнего регистра на нижний.
t = 0
l = 0
for i in open('text18-4.txt', encoding='UTF-8'):
    print(i, end='')
    # print('i',i)
    for j in i:
        # print('j',j)
        if j.isalpha() == True:
            t += 1

print(end='\n')
print('Количество символов, принадлежащих к группе букв: ', t, end='\n')

f1 = open('text18-4.txt', encoding='UTF-8')
l = f1.read().lower()
f1.close()

f2 = open('text-end.txt', 'a', encoding='UTF-8')
f2.writelines(l)
f2.close()
