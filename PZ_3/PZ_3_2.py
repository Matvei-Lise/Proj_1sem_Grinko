# Cпектр видимого излучения предоставлен в таблице. Составить программу
# определяющую название цвета в зависимости от введённой длинны волны

a = input("Введите длинну волны: ")

while type(a) != int: # обработка исключеий
    try:
        a = int(a)
    except ValueError:
        print('Неправильно ввели!')
        a = input("Введите длину волны: ")

if a<150 : print("Фиолетовый")
elif a>150 and a<480 : print("Синий")
elif a>480 and a<510 : print("Голубой")
elif a>510 and a<550 : print("Зелёный")
elif a>550 and a<570 : print("Желто-зелёный")
elif a>570 and a<590 : print("Желтый")
elif a>570 and a<590 : print("Оранжевый")
else: print('Красный')
