class soldier:
    def __init__(self):
        self.family=str()
        self.height=float()
        self.weight=int()
    def volume(self):
        return(self.height*self.weight)
    def info(self):
        print('Информация о солдате: ')
        print('Фамилия солдата: ', self.family)
        print('Рост: %d см' % (self.height))
        print('Вес: %d кг\n' % (self.weight))

class officer(soldier):
    def __init__(self):
        self.education=0
    def volume(self):
        if self.education=='начальный':
            return(self.height*self.weight/2)
        elif self.education=='средний':
            return(self.height*self.weight)
        elif self.education=='высший':
            return(self.height*self.weight*2)
        else:
            return('Несуществующий уровень образования')

print('Демонстрация класса 1\n')
ivanov=soldier()
a=input('Введите фамилию солдата: ')
b=float(input('Введите рост: '))
c=int(input('Введите вес: '))
print()
ivanov.family,ivanov.height,ivanov.weight=a,b,c
ivanov.info()
print('Объем солдата: ',ivanov.volume(),'у.е.\n')
print('Демонстрация класса 2\n')
sidorov=officer()
a=input('Введите фамилию офицера: ')
b=float(input('Введите рост: '))
c=int(input('Введите вес: '))
d=input('Введите уровень образования: ')
print()
sidorov.family,sidorov.height,sidorov.weight,sidorov.education=a,b,c,d
sidorov.info()
print('Полезность солдата: ',sidorov.volume(),'у.е.\n')
