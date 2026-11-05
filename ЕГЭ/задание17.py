f = open('17.txt').readlines()
f = list([int(s) for s in f])
count , maxim = 0, -10e16
for i in range(len(f) - 1):
    x, y = f[i], f[i + 1]
    if (x * y) % 15==0 and (x+y)%7==0:
        count += 1
        maxim = max(maxim,x+y)

print(count, maxim)