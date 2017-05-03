import random

def swap(a,b):
    buf=a
    a=b
    b=buf

arr=[]

m=input('Введите кол-во строк: ')
n=input('Введите кол-во столбцов: ')

for i in range(m):
    arr.append([])
    for j in range(n):
        arr[i].append(random.randint(-10,10))
    print(arr[i])
    
k=0
buf=0

for p in range(0,n,2):
    ex=arr[0][p]
    for i in range(m):
        for j in range(i,m):
            if arr[j][p]<ex:
                arr[j][p]=ex
                k=j
        swap(a[k][p],a[i][p])
        
for q in range(1,n,2):
    ex=arr[0][q]
    for i in range(m):
        for j in range(i,m):
            if arr[j][p]>ex:
                arr[j][p]=ex
                k=j
        swap(a[k][p],a[i][p])
