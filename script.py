grid = {}
turns = list(range(1, 10))

def printGrid():
    global grid
    gridpos = 1
    top = ("     |     |     ")
    bot = ("_____|_____|_____")
    for i in range(3):
        mid = ("  " + grid[gridpos] + "  |  " + grid[gridpos + 1] + "  |  " + grid[gridpos + 2])
        gridpos += 3
        printList = [top, mid, bot]
        if i == 2:
            printList[2] = printList[0]
        print(*printList, sep="\n")

def setSymbol(pos, sym):
    global grid
    grid[int(pos)] = sym
    printGrid()

for cellNumber in turns:
    grid.setdefault(cellNumber, " ")

for turn in turns:
    if turn % 2 != 0:
        setSymbol(input(), "X")
    else:
        setSymbol(input(), "O")