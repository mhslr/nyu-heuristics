from itertools import product
from pprint import pprint


def get_score(grid):
    # -1 or +1 -> winner
    for row in range(3):
        x = 0  # sum over row
        for col in range(3):
            x += grid[row][col]
        if abs(x) == 3:
            return x // 3
    for col in range(3):
        x = 0  # sum over col
        for row in range(3):
            x += grid[row][col]
        if abs(x) == 3:
            return x // 3
    x = 0  # sum over first diagonal
    for i in range(3):
        x += grid[i][i]
    if abs(x) == 3:
        return x // 3
    x = 0  # sum over snd diagonal
    for i in range(3):
        x += grid[i][2-i]
    if abs(x) == 3:
        return x // 3
    return 0





def minimax(player, grid):
    # player is 1 or -1
    # player wants to maximize player * outcome
    sc = get_score(grid)
    if sc:  # game is done
        return sc, ()
    nxt = []
    for row in range(3):
        for col in range(3):
            if grid[row][col] == 0:
                grid[row][col] = player
                sc, hist = minimax(-player, grid)
                nxt.append((sc, hist+((row, col),)))
                grid[row][col] = 0
    if not nxt:  # tie, game is done
        return 0, ()
    return max(nxt) if player > 0 else min(nxt)

grid = [
        [0,0,0],
        [0,0,0],
        [0,0,0],
        ]

sc, hist = minimax(1, grid)
for i, (x,y) in enumerate(hist):
    grid[x][y] = 'X' if i % 2 else 'O'
for i in range(3):
    print(grid[i])
print(sc)
