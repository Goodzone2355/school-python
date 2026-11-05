import math
def f1(x):
    return x**2
def f2(x):
    return 4*math.cos(x)
S=0
a = -1.2
b = 1.2
x=a
h = 0.01
while x<b:
    S+= f1(x)-f2(x) \
    +f1(x+h)-f2(x+h)
    x+=h
S*=h/2
print(abs(S))