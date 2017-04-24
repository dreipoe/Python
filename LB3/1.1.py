import math
d=0
while(d<=0):
    d=float(input('Введите d: '))
    if(d<=0):
        print('d должен быть положительным')
a=2.5
ap=2
k=2
while(math.fabs(a-ap)>=d):
    ap=a
    a=2+1/a
    k=k+1
print('Число k: ',k)
print('Число a[k-1]: ',ap)
print('Число a[k]: ',a)
