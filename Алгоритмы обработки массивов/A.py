from random import randint 
N = int(input("длина"))
A = [randint(1, 10) for x in range(N)]
c = A[N-1]
print (*A)
print (c)
for i in range(1, N-1):
    A[i-1] = A[i+1]
print(*A)