c = str(input('Введите фразу: '))
a = 1
for i in range(len(c)):
    if c[i] == ' ':
        a = a + 1
print('В этой фразе',a,'слов')
