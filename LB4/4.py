string=input('Введите предложение: ')
string=string+' '
a=[]
s=0
for i in range(len(string)):
    if string[i]==' ':
        a.append(string[s:i])
        s=i+1
print('a)')
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if a[i][0]==a[j][0]:
            print(a[i],' & ',a[j])
s=0
print('б)')
for i in range(len(a)):
    for j in range(len(a[i])):
        if (a[i][j]=='e' or a[i][j]=='е') and s!=3:
            s=s+1
        elif s==3:
            print(a[i])
            break
print('в)')
for i in range(len(a)):
    for j in range(len(a[i])):
        if (a[i][j]=='о' or a[i][j]=='o'):
            print(a[i])
            break
