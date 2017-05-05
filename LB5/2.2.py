import matrix

def swap(a,b):
    return(b,a)

arr=[]

m=int(input('Введите кол-во строк: '))
n=int(input('Введите кол-во столбцов: '))

matrix.MatrixRandomInput(arr,-1000,1000,m,n)
print('До: ')
matrix.MatrixOutput(arr)

for p in range(0,n,2):
    for i in range(m):
        ext=arr[i][p]
        k=i
        for j in range(i+1,m):
            if arr[j][p]>ext:
                ext=arr[j][p]
                k=j
        arr[i][p],arr[k][p]=swap(arr[i][p],arr[k][p])
        
for q in range(1,n,2):
    for i in range(m):
        ext=arr[i][q]
        k=i
        for j in range(i+1,m):
            if arr[j][q]<ext:
                ext=arr[j][q]
                k=j
        arr[i][q],arr[k][q]=swap(arr[i][q],arr[k][q])

print('После: ')
matrix.MatrixOutput(arr)
