c = str(input('Введите фразу: '))
j = int(len(c))
for i in range(len(c)):
    if c[i] == ' ':
        i = i + 1
    if c[j] == ' ':
        j = j - 1
    if c[i] != c[j]:
        no = true
        break
    j = j - 1
if no:
    print('Эта фраза - палиндром!')
else:
    print('Эта фраза - не палиндром')
