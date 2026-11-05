from random import randint
N = 1000
A = [randint(1, 15) for x in range(N)]
B = [randint(1, 15) for x in range(N)]
C = [randint(1, 15) for x in range(N)]
D = [randint(1, 15) for x in range(N)]
E = [randint(1, 15) for x in range(N)]
def couch(A):
    c = 0
    for i in range(N-1):
        nMin = i
        for j in range(i+1, N):
            c += 1
            if A[j] < A[nMin]:
                nMin = j
        if i != nMin:
            A[i], A[nMin] = A[nMin], A[i]
    return c
print(*A)

