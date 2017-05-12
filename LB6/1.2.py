class vector:
    def __init__(self, a=2, b=1, c=4, d=3):
        self.p1=[float(a), float(b)] 
        self.p2=[float(c), float(d)]
    def __del__(self):
        print('Вектор успешно удален')
    def info(self):
        print('Информация об объекте:\nКласс: vector\nТекущие атрибуты:\nx1=%.3f\ny1=%.3f\nx2=%.3f\ny2=%.3f\n' % (self.p1[0],self.p1[1],self.p2[0],self.p2[1]))
    def middle(self):
        self.x=(self.p1[0]+self.p2[0])/2
        self.y=(self.p1[1]+self.p2[1])/2
        return(self.x, self.y)
    def pi4q(self):
        return((self.p2[0]-self.p1[0])==(self.p2[1]-self.p1[1]))

class CommonPointVectors(vector):
    def __init__(self, e=3, f=5):
        self.p3=[float(e), float(f)]
    def __del__(self):
        print('Объект успешно удален')
    def info(self):
        print('Информация об объекте:\nКласс: CommonPointVectors\nТекущие атрибуты:\nx1=%.3f\ny1=%.3f\nx2=%.3f\ny2=%.3f\nx3=%.3f\ny3=%.3f\n' % (self.p1[0],self.p1[1],self.p2[0],self.p2[1],self.p3[0],self.p3[1]))
    def summ(self):
        return(self.p1[0], self.p1[1], self.p2[0]+self.p3[0], self.p2[1]+self.p3[1])

print('Демонстрация родительского класса\n')
m=vector()
n=vector()
edit=[]
for i in range(2):
    edit.append([])
    for j in range(2):
        edit[i].append(float(input('Введите значение %s точки %d: ' % (chr(ord('x')+j), i+1))))
print()
n.p1, n.p2 = edit
m.info()
n.info()
memo=[[m.middle(), m.pi4q()], [n.middle(), n.pi4q()]]
for i in range(2):
    print('Информация о векторе №%d' % (i+1))
    print('Точка середины: ',memo[i][0])
    print('Имеет угол наклона 45 граздусов\n' if memo[i][1] else 'Не имеет угла наклона 45 граздусов\n' )
del m, n
print()

print('Демонстрация класса-потомка\n')
o=CommonPointVectors()
edit=[]
for i in range(3):
    edit.append([])
    for j in range(2):
        edit[i].append(float(input('Введите значение %s точки %d: ' % (chr(ord('x')+j), i+1))))
print()
o.p1, o.p2, o.p3 = edit
o.info()
memo=[o.middle(), o.pi4q(), o.summ()]
print('Информация о первом векторе объекта: ')
print('Точка середины: ',memo[0])
print('Имеет угол наклона 45 граздусов\n' if memo[1] else 'Не имеет угла наклона 45 граздусов\n' )
print('Сумма векторов объекта: ',memo[2])
del o
