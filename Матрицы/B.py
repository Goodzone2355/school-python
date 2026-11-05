import random
def printMatrix(A):
    for i in range(N):
        for j in range(M):
            print("{:4d}".format(A[i][j]), end = "")
        print()
N = 10
M = 6
S = 0
q = 0 
A = [[0]*M for i in range(N)]
for i in range(N):
    for j in range(M):
        A[i][j] = random.randint(0,255)
        S += A[i][j]
        q += 1
printMatrix(A)
median = S/q
print(S)
print(q)
print("Средня яркость:", "{:.3f}".format(median))
for i in range(N):
    for j in range(M):
        if A[i][j] > median:
            A[i][j] = 255
        else:
            A[i][j] = 0
printMatrix(A)
s = "123456"
while len(s) > 0:
    s = s[2:]
    print ( "1", end="" )

image = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]
n_rows = len(image)
n_cols = len(image[0])
flipped_image = [[0] * n_cols for _ in range(n_rows)]

for i in range(n_rows):
    flipped_image[i] = image[n_rows - i - 1]

print(flipped_image)