class PhoneTariff:
    def __init__(self):
        self.time=int()
        self.cost=int()
    def info(self):
        print('Название класса: PhoneTariff')
        print('Значение атрибута time: ',self.time)
        print('Значение атрибута cost: ',self.cost)
    def TotalCost(self):
        return(self.time*self.cost)

class PhoneTariffDay(PhoneTariff):
    def __init__(self):
        self.n=int()
    def DayCost(self):
        return(self.TotalCost()*self.n)

c=PhoneTariff()
d=PhoneTariffDay()
edit=[]
edit.append(int(input('Введите кол-во минут разговора: ')))
edit.append(int(input('Введите стоимость разговора за 1 минуту: ')))
c.time, c.cost = edit
memo=c.TotalCost()
print('Стоимость разговора: ',memo)
edit=[]
edit.append(int(input('Введите кол-во минут разговора: ')))
edit.append(int(input('Введите стоимость разговора за 1 минуту: ')))
edit.append(int(input('Введите кол-во разговоров за сутки: ')))
d.time, d.cost, d.n = edit
memo=[d.TotalCost(), d.DayCost()]
print('Стоимость одного разговора: ',memo[0],'\nСтоимость разговоров за сутки: ',memo[1])
