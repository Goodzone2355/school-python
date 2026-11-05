stroka = "C:/Фото/2013/Поход/vasya.jpg"
s1 = ""
for c in stroka:
    if c == "/": c = "\n"
    s1 = s1 + c
print(s1)
