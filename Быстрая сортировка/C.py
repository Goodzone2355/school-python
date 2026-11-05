import random
from random import randint
N = 1000
A = [randint(1, 15) for x in range(N)]
E = [randint(1, 15) for x in range(N)]
C = [randint(1, 15) for x in range(N)]
def bubble(A):
    c = 0
    for i in range(N-1): # количество переборов 9
        for j in range(N-i-1): # при первом переборе i=0
            if A[j] > A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]
                c += 1
    return(c)
a = bubble(A)
print(a)


def couch(A):
    c = 0
    for i in range(N-1):
        nMin = i
        for j in range(i + 1, N):
            if A[j] < A[nMin]:
                nMin = j
        if i != nMin:
            A[i], A[nMin] = A[nMin], A[i]
            c += 1
    return c
c = couch(C)
print(c)

def qSort(A, nStart, nEnd): 
    c = 0
    if nStart >= nEnd: return
    L = nStart; R= nEnd
    X = A[(L+R)//2]
    while L <= R:
        while A[L] < X: L +=1 
        while A[R] > X: R -= 1
        if L <= R:
            A[L], A[R] = A[R], A[L]
            c += 1
            L += 1; R -=1
    qSort (A, nStart, R)
    qSort (A, L, nEnd)
    return c
qSort(E, 0, N-1)
e = qSort(E, 0, N-1)
print(e)

