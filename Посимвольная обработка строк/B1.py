a = " Я хочуee пиццууууу f "
word = []
B = []
space = []
for i in a:
    if i == ' ':
        word.append(space)
        space = []
    elif i != " ":
        space.append(i)
if space:
    word.append(space)
print(word)
for x in word:
    if x != []:
        B.append(x)
print(B)
print(len(B))

z = []
for k in B:
    z.append(len(k))
print(z)
print(max(z))



