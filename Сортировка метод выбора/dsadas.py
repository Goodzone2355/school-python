from random import randint
N=15
A = [randint(1, 15) for _ in range(N)]
B = []
for i in range(N-1):
    nMin = i
    for j in range(i+1, N):
        if A[j] < A[nMin]:
            nMin = j
    if i != nMin:
        A[i], A[nMin] = A[nMin], A[i]
    for x in A:
        if x not in B:
            B.append(x)
print(len(B))
print(*A)
print(*B)