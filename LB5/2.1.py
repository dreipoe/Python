import random
a=[]
for i in range(4):
    a.append([])
    for j in range(4):
        a[i].append(random.randint(-10,10))
    print(a[i])
s=0
k=0
for j in range(4):
    s=s+a[i][j]
min=s
for i in range(1,4):
    s=0
    for j in range(4):
        s=s+a[i][j]
    if s<min:
        min=s
        k=i+1
print("%d-я строка с наименьшей суммой элементов: %d" % (k, min))
    
    
