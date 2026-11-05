def f(n):
    if n == 0:
        return 0
    if n % 2 == 0 and n>0:
        return f(n/2)
    if n%2!=0:
        return 1+f(n-1)
ans=0
while f(ans)!=12:
    ans+=1
print(ans)