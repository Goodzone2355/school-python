from random import randint
N = int(input("Введите длину массива: "))
A = [randint(1, 15) for x in range(N)]
n = 1 
print(*A)
while n < len(A):
     isChange = False
     for i in range(len(A)-n):
          if A[i] > A[i+1]:
               A[i],A[i+1] = A[i+1], A[i]
               isChange = True
     n += 1
     if not isChange:
        break
print(*A)