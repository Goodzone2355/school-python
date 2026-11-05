def perevertysh(a):
    b = 0
    while a > 0:
        c = a%10
        a//=10
        b*=10
        b+=c
    return b
a = int(input())
print(perevertysh(a))




