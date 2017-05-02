import random
a=[]
for i in range(12):
    a.append(random.randint(-10, 10))
print(a)
m=0
n=0
k=1
for i in range(1, 11):
    if (a[i]>a[i-1]) and (a[i]>a[i+1]):
        n=i
        print("Max: Разница на %d-м промежутке: %d" % (k, a[n]-a[m]))
        k=k+1
        m=i
    elif (a[i]<a[i-1]) and (a[i]<a[i+1]):
        n=i
        print("Min: Разница на %d-м промежутке: %d" % (k, a[m]-a[n]))
        k=k+1
        m=i
