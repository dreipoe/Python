import math
y = float(input('Введите y: '))
k = float(input('Введите k: '))
R = (math.sqrt(math.sin(y)**2+6.835))/(math.log1p(y+k)+3*y**2)
print(R)
