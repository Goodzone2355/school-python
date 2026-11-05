def summa(n):
    s = 0
    while n>0:
        k = n%10
        n = n//10
        s += k
    return s
A=open("E:/Python/Обработка массивов из файлов/B.txt")
B=open('E:/Python/Обработка массивов из файлов/B1.txt','w')
s = A.read().split()
array = list(map(int, s))
array.sort(key = summa)
B.write(str(array))
A.close()
B.close()
