s = " "
for n in range(1,54):
    c = 0
    for k in range(2,n):
        if n%k==0:
            c+=1
    if c == 0:
        s = s + n
        print(s)