def summ (m):
    s = 0
    while m > 0:
        s += m%10
        m = m//10
    return s

from random import randint
N = 10
A = [randint(1, 100) for x in range(N)]
print(*A)

for i in range(N-1): # количество переборов 9
    for j in range(N-i-1): # при первом переборе i=0
        if summ(A[j]) > summ(A[j+1]):
            A[j], A[j+1] = A[j+1], A[j]
print(*A)