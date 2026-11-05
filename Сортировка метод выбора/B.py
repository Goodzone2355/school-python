from random import randint
N = 10
A = [randint(1, 15) for x in range(N)]
print(*A)
k = 1
for i in range(N-1):
    nMin = i
    for j in range(i+1, N):
        if A[j] < A[nMin]:
            nMin = j
    if i != nMin:
        A[i], A[nMin] = A[nMin], A[i]
print(k)
print(*A)