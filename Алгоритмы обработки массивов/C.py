import random
mass=[]
mass=[random.randint(-100, 100) for i in range(5)]
print("Maссив:", *mass)
a1 = [i for i in mass if i>0]
a2 = [i for i in mass if i<0]
a3 = [i for i in mass if i== 0]
b=a1+a2+a3
print('Результат:', *b)
X = mass
count = 0
for i in X:
    if i > 0:
        count += 1
print("Количество количество положительных элементов: ", count)