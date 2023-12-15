def t(x, y, z):
    # Проверяем неравенство треугольника
    if x + y > z and x + z > y and y + z > x:
        return True
    else:
        return False

# Вводим значения сторон треугольника
x = float(input("Введите длину первой стороны треугольника: "))
y = float(input("Введите длину второй стороны треугольника: "))
z = float(input("Введите длину третьей стороны треугольника: "))

# Проверяем, существует ли треугольник
if t(x, y, z):
    print("Треугольник существует.")
else:
    print("Треугольник не существует.")





import math

def find_closer_point(x1, y1, x2, y2): 
    c = math.sqrt(x1**2 + y1**2)
    c2 = math.sqrt(x2**2 + y2**2)

    if c < c2:
        return "M1({}, {}) ближе к началу координат".format(x1, y1)
    elif c > c2:
        return "M2({}, {}) ближе к началу координат".format(x2, y2)
    else:
        return "Точки находятся на одинаковом расстоянии от начала координат"

# Пример использования
x1 = float(input("Введите x1: "))
y1 = float(input("Введите y1: "))
x2 = float(input("Введите x2: "))
y2 = float(input("Введите y2: "))

z = find_closer_point(x1, y1, x2, y2)
print(z)



a = int(input())
r = int(input())

S = a*a #площадь кв
S1 = 3.14*(r**2) #площадь круга

if S < S1:
    print('Площадь круга:', S1)
else:
    print('Площадь квадрата:', S)








import math

def is_point_in_circle(x, y, x0, y0, r):
    c = math.sqrt((x - x0)**2 + (y - y0)**2)
    if c <= r:
        return True
    else:
        return False

x = float(input("Введите координату x точки M: "))
y = float(input("Введите координату y точки M: "))
x0 = float(input("Введите координату x центра круга: "))
y0 = float(input("Введите координату y центра круга: "))
r = float(input("Введите радиус круга: "))

if is_point_in_circle(x, y, x0, y0, r):
    print("Точка M находится внутри круга")
else:
    print("Точка M находится за пределами круга")













