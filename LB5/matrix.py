import random

def MatrixOutput(arr):
    if not(type(arr)==list and type(arr[0])==list):
        print('MatrixOutput: Параметр не является матрицей')
        return
    
    m=len(arr)
    n=len(arr[0])

    if type(arr[0][0])==int:
        for i in range(m):
            [print('{0:>10}'.format(arr[i][j]), end=' ') for j in range(n)]
            print()
    else:
        for i in range(m):
            [print('{0:5.3f}'.format(arr[i][j]), end=' ') for j in range(n)]
            print()

def MatrixRandomInput(arr,a,b,m,n,*keytype):
    if not(type(arr)==list):
        print('MatrixRandomInt: Параметр не объявлен как массив')
        return
    if (m<=0 or n<=0):
        print('MatrixRandomInt: Число строк или столбцов должно быть натуральным')
        return
    if not keytype:
        [arr.append([random.randint(a,b) for j in range(n)]) for i in range(m)]
    else:
        [arr.append([random.uniform(a,b) for j in range(n)]) for i in range(m)]
