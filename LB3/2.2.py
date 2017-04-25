def addpnlty(slc):
    slc=slc-1
    n=int(input('Кол-во секунд штрафного времени: '))
    pnlty[slc]=pnlty[slc]+n
    print('Суммарное штрафное время:\nКрасные: ',pnlty[0],'\nСиние: ',pnlty[1])

slct=1
pnlty=[0,0]
while (slct != 0):
    slct=int(input('Выберите команду:\n1. Красные\n2. Синие\n0. Конец игры\n'))
    if (slct in range(1,3)):
        addpnlty(slct)
    elif (slct == 0):
        print('Игра окончена.\nИтоговое штрафное время:\nКрасные: ',pnlty[0],'\nСиние: ',pnlty[1])
    else:
        print('Такой команды нет. Повторите ввод')
            
