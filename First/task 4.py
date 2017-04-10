a = int(input('Введите интервал А: '))
b = int(input('Введите интервал В: '))
c = int(input('Введите нужный остаток: '))
d = int(input('Введите делитель: '))
for i in range(a, b+1):
   if (i%d==c): print(i) 

