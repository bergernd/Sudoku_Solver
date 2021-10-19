
import copy

def Vert(x,y):
    #Checks that there are no invalid numbers in the selected column
    valid = True
    i=0
    while i < 9:
        if y == i:
            pass
        elif newBoard[y][x] == newBoard[i][x]:
            valid = False
            return valid
        i+=1

    return valid

def Hori(x,y):
    #Checks that there are no invalid numbers in the selected row
    valid = True
    i=0
    while i < 9:
        if x == i:
            pass
        elif newBoard[y][x] == newBoard[y][i]:
            valid = False
            return valid
        i+=1
    return valid

def Square(x,y):
    #Checks that there are no invalid numbers in the selected 3x3 box
    valid = True
    xbox = x//3
    ybox = y//3

    if ybox == 0 and xbox == 0:
        i= 0
        while i < 3:
            ii = 0
            while ii < 3:
                    if i == y and ii == x:
                        pass
                    elif newBoard[y][x] == newBoard[i][ii]:
                        valid = False
                        return valid
                    ii+=1
            i+=1
        return valid


    elif ybox == 0 and xbox == 1:
            i= 0
            while i < 3:
                ii = 3
                while ii < 6:
                        if i == y and ii == x:
                            pass
                        elif newBoard[y][x] == newBoard[i][ii]:
                            valid = False
                            return valid
                        ii+=1
                i+=1
            return valid

    elif ybox == 0 and xbox == 2:
            i= 0
            while i < 3:
                ii = 6
                while ii < 9:
                        if i == y and ii == x:
                            pass
                        elif newBoard[y][x] == newBoard[i][ii]:
                            valid = False
                            return valid
                        ii+=1
                i+=1
            return valid

    elif ybox == 1 and xbox == 0:
            i= 3
            while i < 6:
                ii = 0
                while ii < 3:
                        if i == y and ii == x:
                            pass
                        elif newBoard[y][x] == newBoard[i][ii]:
                            valid = False
                            return valid
                        ii+=1
                i+=1
            return valid

    elif ybox == 1 and xbox == 1:
        i= 3
        while i < 6:
            ii = 3
            while ii < 6:
                    if i == y and ii == x:
                        pass
                    elif newBoard[y][x] == newBoard[i][ii]:
                        valid = False
                        return valid
                    ii+=1
            i+=1
        return valid

    elif ybox == 1 and xbox == 2:
        i= 3
        while i < 6:
            ii = 6
            while ii < 9:
                    if i == y and ii == x:
                        pass
                    elif newBoard[y][x] == newBoard[i][ii]:
                        valid = False
                        return valid
                    ii+=1
            i+=1
        return valid

    elif ybox == 2 and xbox == 0:
        i= 6
        while i < 9:
            ii = 0
            while ii < 3:
                    if i == y and ii == x:
                        pass
                    elif newBoard[y][x] == newBoard[i][ii]:
                        valid = False
                        return valid
                    ii+=1
            i+=1
        return valid

    elif ybox == 2 and xbox == 1:
            i= 6
            while i < 9:
                ii = 3
                while ii < 6:
                        if i == y and ii == x:
                            pass
                        elif newBoard[y][x] == newBoard[i][ii]:
                            valid = False
                            return valid
                        ii+=1
                i+=1
            return valid

    elif ybox == 2 and xbox == 2:
        i= 6
        while i < 9:
            ii = 6
            while ii < 9:
                    if i == y and ii == x:
                        pass
                    elif newBoard[y][x] == newBoard[i][ii]:
                        valid = False
                        return valid
                    ii+=1
            i+=1
        return valid

def Increase(x,y):
    #moves itteration to the next spot on the board
    while True:
        x+=1
        if x >= 9:
            x=0
            y+=1
        if y >= 9:
            return(x,y)
        elif board[y][x] == 0:
            return(x,y)



def Decrease(x,y):
    #moves itteration to the previous spot on the board
    while True:
        x-=1
        if x <= -1:
            x=8
            y-=1
        if y <= -1:
            return(x,y)
        elif board[y][x] == 0:
            return(x,y)


def BoardChecker():
    #ensure good input
    x = 0
    y = 0

    while y<9:
        if board[y][x] == 0:
            pass
        elif Vert(x,y) == True and Hori(x,y) == True and Square(x,y) == True:
            pass
        else:
            return False

        x+=1
        if x >=9:
            x=0
            y+=1


board = [ [0,0,5,0,0,0,1,0,0],
          [0,0,0,6,0,5,0,0,0],
          [7,6,0,9,0,0,0,2,0],
          [3,0,0,0,4,0,0,0,5],
          [0,5,9,0,3,0,2,4,0],
          [8,0,0,0,6,0,0,0,1],
          [0,1,0,0,0,2,0,6,3],
          [0,0,0,3,0,7,0,0,0],
          [0,0,3,0,0,0,8,0,0]]




#makes copy of board
newBoard = copy.deepcopy(board)
isGood = BoardChecker()

#Starting coordinates
x = 0
y = 0



while y < 9:
    if board[y][x] == 0:
        while newBoard[y][x] < 10:
            newBoard[y][x] +=1
            if newBoard[y][x] > 9:
                if board[y][x] != 0:
                    pass
                else:
                     newBoard[y][x] = 0
                x,y = Decrease(x,y)
                if y <= -1:
                    #if

                    y=10
                    isGood = False
                    break


            elif Vert(x,y) == True and Hori(x,y) == True and Square(x,y) == True:
                break



    x,y = Increase(x,y)

if isGood == False:
    print("Invalid Board")
    for i in board:
        print(i)
else:
    for i in newBoard:
        print(i)
