import math

# Функция, корни которой нужно найти
def f(x):
    return x**2 - 2*x - 5

# Нахождение интервалов, на которых находятся корни
def find_intervals(start, end, step):
    intervals = []
    x = start
    while x < end:
        if f(x)*f(x+step) < 0:
            intervals.append((x, x+step))
        x += step
    return intervals

# Уточнение решения на заданном интервале методом перебора
def refine_solution(interval, step):
    x1, x2 = interval
    while abs(x2-x1) > step:
        x1 = x1 + step
        x2 = x2 - step
        if f(x1)*f(x2) < 0:
            x1 = x1 - step
            x2 = x2 + step
    return (x1 + x2) / 2

# Запрос пользователю левой границы интервала и вывод найденного корня
def find_root():
    a = float(input("Введите левую границу интервала: "))
    intervals = find_intervals(a, a+10, 0.1)
    for interval in intervals:
        print("Интервал:", interval)
        root = refine_solution(interval, 0.0001)
        print("Найденный корень:", root)

# Пример использования
find_root()