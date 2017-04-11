import math
y = float(input('Введите y: '))
t = float(input('Введите t: '))
S = (4.351*math.pow(y,3)+2*t*math.log1p(t))/math.sqrt(math.cos(2*y)+4.351)
print(S)
