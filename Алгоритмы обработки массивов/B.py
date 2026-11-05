from random import randint 
N = int(input("длина"))
A = [randint(1, 10) for x in range(N)]
print (*A)
first = A[0:N//2]
second = A[N//2:N]
first.reverse()
second.reverse()
Gotov = first + second
print(*Gotov)