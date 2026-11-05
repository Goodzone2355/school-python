from random import randint 
N = int(input("длина"))
A = [randint(-10, 10) for x in range(N)]
print (*A)
B = [x for x in A if x<0]
print(*B)