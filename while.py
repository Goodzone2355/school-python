n = int(input())

if n < 0:
    print("Укажите положительное число")
elif n <= 1:
    print("Сумма = 0")
else:
    sum = 1

    prev1 = 0
    prev2 = 1
    cur = 1

    sequence = "0 1"

    while cur < n:
        sequence += " " + str(cur)
        prev1 = prev2
        prev2 = cur
        sum += cur
        cur = prev1 + prev2

    print("Посследовательность: " + sequence)
    print("Сумма: " + str(sum))