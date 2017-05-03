def matrixoutput(a):
    m=len(a)
    n=len(a[0])
    max=a[0][0]
    min=a[0][0]
    
    for i in range(m):
        for j in range(n):
            if a[i][j]>max:
                max=a[i][j]
            elif a[i][j]<min:
                a[i][j]=min
                
    if min<0:
        min=min-2*min
        
    if min>max:
        max=min
        
    r=2
    while(max>=10):
        max=max/10
        r=r+1
    
    for i in range(m):
        for j in range(n):
            print('{0:{r}}'.format(a[i][j],r=r),end=' ')
        print()
                
arr=[[1,20,3],[40,5,60],[7,80,9]]
matrixoutput(arr)
    
