from functools import cache
def moves(x):
    return x * 2, x + 1
@cache
def game(n):
    if n >= 129:
        return 'end'
    if any(game(x)=='end' for x in moves(n)):
        return 'p1'
    if all(game(x) == 'p1' for x in moves(n)):
        return 'v1'
    if any(game(x)=='v1' for x in moves(n)):
        return 'p2'
    if all(game(x) == 'p1' or game(x) == 'p2' for x in moves(n)):
        return 'v2'
for i in range(1,128):
    print(i, game(i))