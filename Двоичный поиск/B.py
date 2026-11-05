import random
mass=[random.randint(0,10) for i in range (10)]
print("Массив:",mass)
mass.sort()
print("После сортировки:",mass)
X=int(input("Введите число X: "))
l=0
r=len(mass)
k=0
while l<(r-1):
    c=(l+r)//2
    if X<mass[c]:
        r=c
    else:    
        l=c
    if X==mass[l]:
        k+=1
        mass.pop(c)
        l=0
        r-=1
if k!=0:
    print("Число",X,"встречается",k,"раз(а)")
else:
     print("Число",X,"не встречается")