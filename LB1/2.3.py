import math
a = float(input('Введите длину стороны a: '))
b = float(input('Введите длину стороны b: '))
c = float(input('Введите длину стороны c: '))
if ((a+b>c) and (a+c>b) and (b+c>a)):
    print('Длина биссектрисы a: ',math.sqrt(b*c*(a+b+c)*(b+c-a))/(b+c))
    print('Длина биссектрисы b: ',math.sqrt(a*c*(a+b+c)*(a+c-b))/(a+c))
    print('Длина биссектрисы c: ',math.sqrt(a*b*(a+b+c)*(a+b-c))/(a+b))
else:
    print('Такого треугольника нет')
