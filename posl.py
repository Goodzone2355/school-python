n = int(input())
c="0"
b=1
s=0
if n<0:
    print("Отриц.число")
else:
    while b<n:
        c += " "+str(b)
        s+=b
        b+=1
print(s)
print(c)
