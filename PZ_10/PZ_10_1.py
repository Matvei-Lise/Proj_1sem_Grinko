# Книжные магазины предлагают следующие коллекции книг.
# Магистр – Лермонтов, Достоевский, Пушкин, Тютчев
# ДомКниги – Толстой, Грибоедов, Чехов, Пушкин.
# БукМаркет – Пушкин, Достоевский, Маяковский.
# Галерея – Чехов, Тютчев, Пушкин. Определить в каких магазинах
# можно приобрести книги Маяковского

Magistr = {'Лермонтов', 'Достоевский', 'Пушкин', 'Тютчев'}
DomKnigi = {'Толстой', 'Грибоедов', 'Чехов', 'Пушкин'}
BookMarket = {'Пушкин', 'Достоевский', 'Маяковский'}
Galerea = {'Чехов', 'Тютчев', 'Пушкин'}

if 'Маяковский' in Magistr:
    print('Магистр')
elif 'Маяковский' in DomKnigi:
    print('ДомКниги')
elif 'Маяковский' in BookMarket:
    print('БукМаркет')
else: print('Галерея')