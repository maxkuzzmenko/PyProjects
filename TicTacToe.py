grid = {}
turns = list(range(1, 10))

for blockNumber in turns:
    grid.setdefault(blockNumber, " ")
def setSymbol(pos, sym):
    global grid
    grid[int(pos)] = sym
    print(grid)

for turn in turns:
    if turn % 2 != 0:
        setSymbol(input(), "X")
    else:
        setSymbol(input(), "O")