import random
a=[]
for i in range(12):
    a.append(random.uniform(-10, 10))
    print("%.3f" % a[i])
b=0
for i in range(1,11):
    if (a[i]>a[i-1]) and (a[i]>a[i+1]):
        b=b+1
print("Кол-во локальных максимумов: ", b)
