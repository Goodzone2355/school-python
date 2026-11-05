def summa(N):
    sum = 0
    while N>0:
        posl = N%10
        sum = sum + posl
        N//=10
    return sum
N = int(input())
print(summa(N))



