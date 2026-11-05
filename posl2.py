n = int(input())
c, b, summa = "0", 1, 0

if n<0:
    print("Отриц.число")
    exit

# основной код 
while True:
    if b >= n:
        break
    c += " " + str(b)
    summa += b
    b += 2
    
print(summa)
print(c)