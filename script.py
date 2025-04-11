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