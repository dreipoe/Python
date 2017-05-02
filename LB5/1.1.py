import random
a=[]
for i in range(12):
    a.append(random.uniform(-10, 10))
    print("%.3f" % a[i])
min=a[0]
max=a[0]
for i in range(1,12):
    if a[i]>max:
        max=a[i]
    elif a[i]<min:
        min=a[i]
print("Интервал значений от %.3f до %.3f" % (min, max))
