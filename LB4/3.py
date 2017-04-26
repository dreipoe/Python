string=input('Введите фразу: ')
string=' '+string
nstr=str()
j=len(string)
for i in range(j-1,-1,-1):
    if string[i]==' ':
        nstr=nstr+string[i+1:j]+' '
        j=i
print(nstr)
        
