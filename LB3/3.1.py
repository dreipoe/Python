import math
n=int(input('Введите n: '))
x=float(input('Введите x: '))
i=2
sum=float(0)
while(i/2<=n):
    sum=sum+(math.cos(i*x))/((i+1)*(i-1))
    i=i+2
print(sum)
