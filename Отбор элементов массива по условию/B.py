from random import randint 
def simple (x):
    k = 2
    while x % k != 0:
        k += 1
    return k == x
A = []
B = []
for x in range(15):
    a = randint(1,100)
    A.append(a)
    if simple(a):
        B.append(a)
print(*A)
print(*B)