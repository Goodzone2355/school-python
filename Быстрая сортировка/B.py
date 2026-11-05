from random import randint
N = 10
A = [randint(1, 15) for _ in range(N)]
print(*A)
B = []

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
            L += 1; R -=1
        for x in A:
            if x not in B:
                B.append(x)
    qSort (A, nStart, R)
    qSort (A, L, nEnd)
    return c
qSort(A, 0, N-1)
print(*A)
print(len(B))