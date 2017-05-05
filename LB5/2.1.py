import random, matrix
a=[]
m=4
n=4
matrix.MatrixRandomInput(a,-1000,1000,m,n,0)
matrix.MatrixOutput(a)
s=0
k=1
for j in range(n):
    s=s+a[0][j]
min=s
for i in range(1,m):
    s=0
    for j in range(n):
        s=s+a[i][j]
    if s<min:
        min=s
        k=i+1
print("%d-я строка с наименьшей суммой элементов: %d" % (k, min))
    
    
