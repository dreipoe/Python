import math
k=int(input('Введите k: '))
p=float(1)
j=int(-1)
for j in range(k):
    p1=0
    i=j
    for i in range(k+3):
        if not(i==7):
            p1=p1+(i-5**1/4)/(i-7)
        print('p1 =',p1)
    p=p*(((j-j**2)*j)/(j+14))*p1
    print('p =',p)
