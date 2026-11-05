def number(N):
    if N>0:
        number(N//10)
        print(N%10)
N = int(input('Введите натуральное число: '))
number(N)
        
        



