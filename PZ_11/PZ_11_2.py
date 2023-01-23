#Из предложенного текстового файла (text18-4.txt) вывести на экран его
#содержимое, количество символов, принадлежащих к группе букв.
#Сформировать новый файл, в который поместить текст в стихотворной форме
# предварительно заменив символы верхнего регистра на нижний.
t = 0
for i in open('text18-4.txt', encoding='UTF-8'):
    print(i, end='')
    for j in i:
        if j == 'а' or 'б' or 'в' or 'г' or 'д' or 'е' or 'ж' or 'з' or 'и' or 'к' or 'л' or 'м' or 'н' or 'о' or 'п' or 'р' or 'с' or 'т' or 'у' or 'ф' or 'х' or 'ц' or 'ч' or 'ш' or 'щ' or 'ъ' or 'ы' or 'ь' or 'э' or 'ю' or 'я':
            t += 1
print(end='\n')
print('Количество символов, принадлежащих к группе букв: ', t, end='\n')

f1 = open('text18-4.txt', encoding='UTF-8')
low = f1.read().lower()
f1.close()

f2 = open('text-end.txt', 'w')
print(low, file=f2)
f2.close()
