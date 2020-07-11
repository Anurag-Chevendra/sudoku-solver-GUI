import random
import turtle

t = turtle.Turtle()
wn = turtle.Screen()
denote=[]
for i in range(9):
    ar=[]
    for j in range(9):
        ss=turtle.Turtle()
        ss.hideturtle()
        ar.append(ss)
    denote.append(ar)
def sudokuGui(grid):


    wn.title("Sudoku")

    t.width(5)
    ss = 50
    t.shape()
    t.penup()
    t.goto(-225, -225)
    t.pendown()

    line = 0
    for i in range(5):
        t.left(90)
        t.color("grey")
        if (line % 3 == 0):
            t.color("black")
            t.width(7)
        t.forward(450)
        t.width(5)
        line = line + 1
        t.right(90)
        t.color("black")
        t.forward(ss)
        t.right(90)
        t.color("grey")
        if (line % 3 == 0):
            t.color("black")
            t.width(7)
        t.forward(450)
        t.width(5)
        line = line + 1
        if (i != 4):
            t.left(90)
            t.color("black")
            t.forward(ss)
    line = 0
    t.right(90)
    for i in range(5):
        t.color("grey")
        if (line % 3 == 0):
            t.color("black")
            t.width(7)
        t.forward(450)
        t.width(5)
        line = line + 1
        t.right(90)
        t.color("black")
        t.forward(ss)
        t.color("grey")
        t.right(90)
        if (line % 3 == 0):
            t.color("black")
            t.width(7)
        t.forward(450)
        t.width(5)
        line = line + 1
        t.left(90)
        if (i != 4):
            t.color("black")
            t.forward(ss)
            t.left(90)
    t.color("Red")
    for i in range(9):
        for j in range(9):
            t.penup()
            t.goto(-200 + (j * 50), 200 - (i * 50))
            # t.goto(-200 + (i * 50), 200 - (j * 50))
            t.pendown()
            if (grid[i][j] == 0):
                t.write(" ", font=("Ariel Narrow", 12, "bold"))
            else:
                t.write(grid[i][j], font=("Ariel Narrow", 12, "bold"))
    t.pendown()
    t.hideturtle()
    solveSudoku(grid, 0, 0)
    turtle.mainloop()


def solveSudoku(grid, x, y):
    if (grid[x][y] == 0):
        for i in range(1, 10):
            if (checkX(grid, i, x) and checkY(grid, i, y) and checkBox(grid, x, y, i)):
                denote[x][y].hideturtle()
                denote[x][y].speed(0)
                grid[x][y] = i
                denote[x][y].penup()
                denote[x][y].goto(-200 + (y * 50), 200 - (x * 50))
                denote[x][y].pendown()
                denote[x][y].color("black")
                denote[x][y].clear()
                denote[x][y].write(grid[x][y], font=("Ariel Narrow", 12, "bold"))
                denote[x][y].pendown()
                if 8 > y >= 0:
                    solveSudoku(grid, x, y + 1)

                elif x == 8 and y == 8:
                    dummyLine=0
                    #Printgrid(grid)
                elif y == 8:
                    solveSudoku(grid, x + 1, 0)
        grid[x][y] = 0
    else:
        if y == 8 and x == 8:
            dummyLine=0
            #Printgrid(grid)
        elif y == 8:
            t.write(" ", )
            solveSudoku(grid, x + 1, 0)
        elif 8 > y >= 0:
            solveSudoku(grid, x, y + 1)


def checkX(grid, num, row):
    c = 0
    for i in range(9):
        if (grid[row][i] == num):
            c = 1
            break
        else:
            c = 0
    if (c == 1):
        return False
    else:
        return True


def checkY(grid, num, col):
    c = 0
    for i in range(9):

        if grid[i][col] == num:
            c = 1
            break
        else:
            c = 0
    if (c == 1):
        return False
    else:
        return True


def checkBox(grid, row, col, num):
    c = 0
    pointerX = 0
    pointerY = 0
    if 2 >= row >= 0:
        pointerX = 0
    elif 3 <= row <= 5:
        pointerX = 3
    elif 6 <= row <= 8:
        pointerX = 6

    if 2 >= col >= 0:
        pointerY = 0
    elif 3 <= col <= 5:
        pointerY = 3
    elif 6 <= col <= 8:
        pointerY = 6

    for x in range(pointerX, pointerX + 3):
        for y in range(pointerY, pointerY + 3):
            if (grid[x][y] == num):
                c = 1

    if (c == 1):
        return False
    else:
        return True


def MakeSudoku():
    Grid = [[0 for x in range(9)] for y in range(9)]
    choice=str(int(wn.numinput("Input", "Do you wish to input the Grid data ?  enter 1 for : yes , enter 2 for : no ", 1, minval=1, maxval=2)))

    if (choice == "1"):
        t.write("open terminal and start entering" , font=("Ariel Narrow", 12, "bold"))
        ss = ""
        for i in range(9):
            for j in range(9):
                ss = ss + " (" + str(i) + "," + str(j) + ")" + " |"
            print("|" + ss)
            print("")
            ss = ""

        print("enter elements one by one")
        for i in range(9):
            for j in range(9):
                print("(" + str(i) + "," + str(j) + ") :")
                Grid[i][j] = int(input())
        t.clear()
    else:
        for i in range(9):
            for j in range(9):
                Grid[i][j] = 0

            # The range here is the amount
            # of numbers in the grid
        for i in range(5):
            # choose random numbers
            row = random.randrange(9)
            col = random.randrange(9)
            num = random.randrange(1, 10)
            while (not CheckValid(Grid, row, col, num) or Grid[row][col] != 0):  # if taken or not valid reroll
                row = random.randrange(9)
                col = random.randrange(9)
                num = random.randrange(1, 10)
            Grid[row][col] = num;

    option = int(wn.numinput("Input", "do you want a solution?  enter 1 for : yes , enter 2 for : no ", 1, minval=1, maxval=2))
    #print("do you want a solution?")
    #option = int(input("      1)Yes  2)No  :"))
    #print("NOTE: THERE MIGHT BE MORE THAN ONE SOLUTION!")
    if (option == 1):
        sudokuGui(Grid)
    else:
        t.clear()
        t.write(" Confidence Maxxx" , font=("Ariel Narrow", 12, "bold"))



def Printgrid(Grid):
    TableTB = "|--------------------------------|"
    TableMD = "|----------+----------+----------|"
    print(TableTB)
    for x in range(9):
        for y in range(9):
            if ((x == 3 or x == 6) and y == 0):
                print(TableMD)
            if (y == 0 or y == 3 or y == 6):
                print("|", end=" ")
            print(" " + str(Grid[x][y]), end=" ")
            if (y == 8):
                print("|")
    print(TableTB)


#     |-----------------------------|
#     | 0  0  0 | 0  0  0 | 0  0  0 |
#     | 0  0  0 | 0  0  0 | 0  0  0 |
#     | 0  0  0 | 0  0  0 | 0  0  0 |
#     |---------+---------+---------|
#     | 0  0  0 | 0  0  0 | 0  0  0 |
#     | 0  0  0 | 0  0  0 | 0  0  0 |
#     | 0  0  0 | 0  0  0 | 0  0  0 |
#     |---------+---------+---------|
#     | 0  0  0 | 0  0  0 | 0  0  0 |
#     | 0  0  0 | 0  0  0 | 0  0  0 |
#     | 0  0  0 | 0  0  0 | 0  0  0 |
#     |-----------------------------|

def CheckValid(Grid, row, col, num):
    # check if in row
    valid = True
    # check row and collumn
    for x in range(9):
        if (Grid[x][col] == num):
            valid = False
    for y in range(9):
        if (Grid[row][y] == num):
            valid = False
    rowsection = row // 3
    colsection = col // 3
    for x in range(3):
        for y in range(3):
            # check if section is valid
            if (Grid[rowsection * 3 + x][colsection * 3 + y] == num):
                valid = False
    return valid


MakeSudoku()
