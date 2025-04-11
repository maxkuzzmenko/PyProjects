grid = {}
turns = list(range(1, 10))

for cellNumber in turns:
    grid.setdefault(cellNumber, " ")
def setSymbol(pos, sym):
    global grid
    grid[int(pos)] = sym
    print(grid)

for turn in turns:
    if turn % 2 != 0:
        setSymbol(input(), "X")
    else:
        setSymbol(input(), "O")
'''
a = "X"
b = ("_____|_____|_____")
c = ("  " + a + "  |  " + a + "  |  " + a)
d = ("     |     |     ")
printlist = (d, c, b)
for i in range(3):
    if i == 2:
        print(*printlist[:-1], d, sep="\n")
    else:
        print(*printlist, sep="\n")
'''