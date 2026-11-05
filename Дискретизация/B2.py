import math
def L(x,v0,alpha):
    g = 9.8
    t = x/v0*math.cos(alpha)
    return v0*t*math.sin(alpha)-g*t**2/2

x=0; S=10; h=0.01; L1=0; v0=12; alpha=35.5*math.pi/180
while x<S:
    y1 = L(x,v0,alpha)
    y2 = L(x+h,v0,alpha)
    L1 = L1+math.sqrt(h**2+(y2-y1)**2)
    x = x+h
print(L1)
x=0; S=10; h=0.01; L1=0; v0=12; alpha=68.5*math.pi/180
while x<S:
    y1 = L(x,v0,alpha)
    y2 = L(x+h,v0,alpha)
    L1 = L1+math.sqrt(h**2+(y2-y1)**2)
    x = x+h
print(L1)