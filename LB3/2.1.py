p=[2]
n=2
while(len(p)<=100):
    i=0
    while(i<len(p)):
        if (n%p[i]==0):
            break
        else:
            i=i+1
    if (i==len(p)):
        p.append(n)
    n=n+1
print(p)
