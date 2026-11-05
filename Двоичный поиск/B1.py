import random
A =[random.randint(0,30) for i in range (10)]
print("Массив:")
print(*A)
A.sort()
print("После сортировки:")
print(*A)
X=int(input("Введите число X: "))
l=0
r=len(A)
k=0
while l<(r-1):
    c=(l+r)//2
    if X<A[c]:
        r=c
    else:    
        l=c
    if X==A[l]:
        k+=1
if k!=0:
    print("Число",X,"найдено")
else:
    print("Число", X, "не найдено")
    if abs(A[l+1] - X) < abs(A[l] - X):
        print(A[l+1])
    elif abs(A[l+1] - X) >  abs(A[l] - X):
        print(A[l])
    else:
        print("Ближайшие числа равноудалены по модулю от числа Х, поэтому ближайшие числа", A[l], A[l+1])
