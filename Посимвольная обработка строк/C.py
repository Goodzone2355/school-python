a = "    How332323fffff   arefffffff     you543g   "
word = []
B = []
for i in a:
    if i == ' ':
        space = []
        word.append(space)
    else:
        space.append(i)
print(word)
for x in word:
    if x != []:
        B.append(x)
print(B)
n = len(B) - 1
while n < len(B):
    if n>0:
        if len(B[n]) > len(B[n-1]):
            print(len(B[n]))
        n -= 1
print(len(B[n]))


