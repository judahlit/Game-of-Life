import pygame, random

# Hier wordt een nieuwe 2D array gemaakt zonder waarden
def n2Dlist(cols, rows):
    lege2Dlist = [[None for i in range(cols)] for j in range(rows)]
    return lege2Dlist


# Hier wordt een grid gevuld met nullen en eenen
def setup(grid):
    for counti, i in enumerate(grid):
        for countj, j in enumerate(i):
            grid[counti][countj] = random.randrange(2)
    return grid


# Hier wordt de grid laten zien in een programma
def draw (grid, blocksize, wincolor, blockcolor):
    countedcols = 0
    winwidth = 0
    winlength = blocksize
    for counti, i in enumerate(grid):
        if countedcols == 0:

            for countj, j in enumerate(i):
                winwidth += blocksize

            countedcols = 1

        else:
            winlength += blocksize

    win = pygame.display.set_mode((winwidth, winlength))
    win.fill(wincolor)

    for counti, i in enumerate(grid):
        for countj, j in enumerate(i):
            x = countj * blocksize
            y = counti * blocksize
            bincolor = grid[counti][countj]
            if bincolor == 1:
                pygame.draw.rect(win, blockcolor, (x, y, blocksize, blocksize))

    pygame.display.update()

cols = 150
rows = 75
blocksize = 10
wincolor = (0, 0, 0)
blockcolor = (0, 255, 0)


pygame.init()

grid = n2Dlist(cols, rows)
grid = setup(grid)


while True:

    draw(grid, blocksize, wincolor, blockcolor)

    # De volgende generation wordt hier berekend

    ngrid = n2Dlist(cols, rows)

    for counti, i in enumerate(grid):
        for countj, j in enumerate(i):
            status = grid[counti][countj]
            #print(status)

            # De levende cellen om 1 cel heen worden geteld
            levend = 0

            for k in range(-1, 2):
                for l in range(-1, 2):
                    if k != 0 or l != 0:
                        col = (counti + k + cols) % cols
                        row = (countj + l + rows) % rows
                        #print(col, row, grid[row][col])
                        #print("col = ", col)
                        #print("row = ", row)
                        levend += grid[row][col]
                        #print("k = ", k)
                        #print("l = ", l)
                        #print("grid[", counti + k, "][", countj + l, "] = ", grid[counti + k][countj + l])
                        #print("levenden = ", levend)

            # Hier staan de regels van de Game of Life

            if status == 0 and levend == 3:
                ngrid[counti][countj] = 1

            elif status == 1 and (levend < 2 or levend > 3):
                ngrid[counti][countj] = 0

            else:
                ngrid[counti][countj] = status

    grid = ngrid

    #from time import sleep
    #sleep(5)

    # Sluit de programma af wanneer Escape ingedrukt is
    key = pygame.key.get_pressed()

    if key[pygame.K_ESCAPE]:
        pygame.quit()
        quit()