f=open("E:/Python/Файловый ввод и вывод/B.txt")
g=open('E:/Python/Файловый ввод и вывод/B1.txt','w')
s=[int(i) for i in f.readlines()]
s=[i for i in s if (i>0 and i %2 == 0)]
if s != []:
    g.write(str(min(s))+' '+str(max(s)))
else:
    g.write("Таких чисел нет")
f.close()
g.close()