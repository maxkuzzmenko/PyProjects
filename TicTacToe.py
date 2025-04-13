grid = {}
turns = list(range(1, 10))

def printGrid():
    global grid
    pos = 1
    top = '     |     |     '
    bot = '_____|_____|_____'
    for i in range(3):
        mid = ("  " + grid[pos] + "  |  " + grid[pos + 1] + "  |  " + grid[pos + 2])
        pos += 3
        printlist = [top, mid, bot]
        if i == 2:
            printlist[2] = printlist[0]
        print(*printlist, sep="\n")

def setSymbol(grid, pos, sym):
    grid[int(pos)] = sym
    printGrid()

for cellNumber in turns:
    grid.setdefault(cellNumber, str(cellNumber))

printGrid()

for turn in turns:
    if turn % 2 != 0:
        setSymbol(grid, input(), "X")
    else:
        setSymbol(grid, input(), "O")