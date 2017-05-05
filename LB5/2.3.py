import matrix
a=[]
m=int(input('Введите кол-во строк: '))
n=int(input('Введите кол-во столбцов: '))
s=0
for i in range(m):
    a.append([])
    if i%2==0:
        [a[i].append(s+j) for j in range(n)]
        s=s+n
    else:
        [a[i].append(s+n-j-1) for j in range(n)]
        s=s+n
matrix.MatrixOutput(a)
