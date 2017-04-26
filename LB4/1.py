string=input('Введите фразу: ')
russian=bool(0)
i=0
while (i<len(string)) and (not russian):
    if (ord(string[i]) in range(ord('а'),ord('я')+1)) or (ord(string[i]) in range(ord('А'),ord('Я')+1)):
        russian=1
        print('В этой строке есть русские буквы')
    else:
        i=i+1
if not russian:
    print('В этой строке нет русских букв')
