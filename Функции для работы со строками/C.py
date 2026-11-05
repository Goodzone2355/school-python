Stroka = input("Введите строку: ")
poisk = input("Что меняем: ")
zamena = input("На что меняем: ")
Stroka1 = Stroka.split()
s1 = " "
for c in Stroka1:
    if c == poisk: c = zamena
    s1 = s1 + " " + c
print(s1)