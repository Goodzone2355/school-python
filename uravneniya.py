import math
def f(x):
    return x**3 + 3*x**2-9*x-5+10*math.sin(x)-10*math.cos(x)
e=0.001
x=int(input("Введите левую границу интервала:"))
d=2*e
o=[]
y=0

for p in range(3):
    while f(x)*f(x+d)>0:
        if x>5:
            y+=1 
            break
        else: x+=d
    if x<5: o.append(x+e)
    x+=2*e
if y==0:    
    print("Решения:", "{:6.3f}, {:6.3f}, {:6.3f}".format(o[0], o[1], o[2]))
elif y==1:    
    print("Решения:", "{:6.3f}, {:6.3f}".format(o[0], o[1]), "и одно решение левее границы")
elif y==2:    
    print("Решение:", "{:6.3f}".format(o[0]), "и два решения левее границы")
else:
    print("Все решения левее границы")