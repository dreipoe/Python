a = float(input('Введите длину стороны a: '))
b = float(input('Введите длину стороны b: '))
c = float(input('Введите длину стороны c: '))
if (a==b) or (a==c) or (b==c):
    print('Треугольник равнобедренный')
else:
    print('Треугольник не равнобедренный')