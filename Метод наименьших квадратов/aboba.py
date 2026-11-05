with open("E://Python/Метод наименьших квадратов/1.txt", "r") as file:
    lines = file.readlines()
    matrix = []
    for line in lines:
        row = [float(x) for x in line.split()]
        matrix.append(row)
print(matrix)
x = []
y = []
for i in matrix:
    x.append(i[0])
print(x)
for j in matrix:
    y.append(j[1])
print(y)
xx = [d*d for d in x]
xy = [x[k]*y[k] for k in range(len(x))]
B = sum(xy)
A = sum(xx)
print(B/A)