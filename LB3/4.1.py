import math
y=[]
i=0
x=1
while(x<=29):
    y.append(math.log(x**2)-x+4)
    print("%.1f   %.3f" % (x, y[i]))
    i=i+1
    x=x+0.2
