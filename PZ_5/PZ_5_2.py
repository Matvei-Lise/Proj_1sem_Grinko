#Описать функцию RectPS(x1,y1,x2, y2,P,S),вычисляющую периметр P и площадь S прямоугольника со
#сторонами, параллельными осям координат, по координатам (x1,y1), (x2, y2) его противоположных вершин
# (x1,y1,x2, y2 -- входные,P и S -- выходные параметры вещественного типа). С помощью этой функции
# найти периметры и площади трех прямоугольников с данными противоположными вершинами.


x1, y1 = float(input("Координаты первого прямоугольника. Введите x1: ")), float(input("Введите y1: "))
x2, y2 = float(input("Введите x2: ")), float(input("Введите y2: "))
def RectPS(x1,y1,x2,y2):
    P = ((x2-x1) + (y2-y1)) * 2
    S = (x2-x1) * (y2-y1)
    return P,S

print("Переиметр и прощадь первого прямоугольника ", RectPS(x1, y1, x2, y2))

x1, y1 = float(input("Координаты второго прямоугольника. Введите x1: ")), float(input("Введите y1: "))
x2, y2 = float(input("Введите x2: ")), float(input("Введите y2: "))

print("Переиметр и прощадь второго прямоугольника ", RectPS(x1, y1, x2, y2))

x1, y1 = float(input("Координаты третьего прямоугольника. Введите x1: ")), float(input("Введите y1: "))
x2, y2 = float(input("Введите x2: ")), float(input("Введите y2: "))

print("Переиметр и прощадь третьегог прямоугольника ", RectPS(x1, y1, x2, y2))