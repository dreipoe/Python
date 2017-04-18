cost = float(input('Введите стоимость покупки в грн: '))
if (cost in range(1000, 1999)):
    cost = cost * 0.95
elif (cost in range(2000, 5000)):
    cost = cost * 0.9
print('Итого: ',cost)
