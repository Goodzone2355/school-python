from random import randint 
def fibbonachi (x):
    if x == 1:
        x = True
    elif x == 0:
        x = False
    else:
        a = 1
        b = 1 
        c = 0
        while c < x:
            c = a + b 
            a = b 
            b = c
        if c == x:
            x = True
        else:
             x = False
    return x
A = []
B = []
for x in range(15):
    a = randint(1,100)
    A.append(a)
    if fibbonachi(a):
        B.append(a)
print(*A)
print(*B)
