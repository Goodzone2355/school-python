#Горизонтально зеркалим
import random
def printMatrix(A):
    for i in range(N):
        for j in range(M):
            print("{:4d}".format(A[i][j]), end = "")
        print()
N = 5
M = 5
S = 0
q = 0 
A = [[0]*M for _ in range(N)]
for i in range(N):
    for j in range(M):
        A[i][j] = random.randint(0,255)
printMatrix(A)
print("AAA")
B = [[0] * M for _ in range(N)]
for i in range(N):
    B[i] = A[N - i - 1]
printMatrix(B)
print("BBB")
# поворот на 90градусов
C = [[0] * N for _ in range(M)]

for i in range(N):
    for j in range(M):
        C[j][N - i - 1] = A[i][j]

for i in range(M):
    C[i] = C[i][::-1]

printMatrix(C)
