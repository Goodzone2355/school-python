#(x > A) ∨ (y > x) ∨ (2y + x < 110)
def f(a, x, y):
    return ((x>a)or(y>x)or(2*y+x<110))

for a in range(300,1,-1):
    flag = True

    for x in range(300):
        for y in range(300):
            if not f(a, x, y):
                flag = False
                break

        if not flag:
            break

    if flag:
        print(a)
        break