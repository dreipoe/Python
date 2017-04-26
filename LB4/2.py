string=input('Введите фразу: ')
i=1
while i in range(len(string)):
    if ord(string[i]) in range(ord('A'), ord('Z')):
        string=string[0:i]+'. '+string[i:len(string)]
        i=i+3
    else:
        i=i+1
print(string)
