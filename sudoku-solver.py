board = [
        [0,0,0,0,0,0,0,0,4],
        [0,0,0,4,5,0,6,7,0],
        [4,8,9,1,6,0,0,3,0],
        [2,1,4,3,0,5,0,0,0],
        [0,0,8,0,0,0,0,0,0],
        [6,9,0,0,0,4,0,0,3],
        [0,3,1,0,4,0,5,0,0],
        [8,0,5,7,0,0,0,9,0],
        [9,6,2,0,8,0,0,0,0]]

########################### VALIDATION ###########################

def checkRows():
    for row in range(0, 9):
        arr = []
        for col in range(0, 9):
            if board[row][col] != 0:
                if board[row][col] in arr:
                    return False
                elif board[row][col] not in arr:
                    arr.append(board[row][col])
    return True

def checkCols():
    for col in range(0, 9):
        arr = []
        for row in range(0, 9):
            if board[row][col] != 0:
                if board[row][col] in arr:
                    return False
                elif board[row][col] not in arr:
                    arr.append(board[row][col])
    return True

def checkBox(r, c):     # r = first row; c = first col
    arr = []
    for row in range(r, r+3):
        for col in range(c, c+3):
            if board[row][col] != 0:
                if board[row][col] in arr:
                    return False
                elif board[row][col] not in arr:
                    arr.append(board[row][col])
    return True

def checkAllBoxes():
    for row in range(0, 7, 3):
        for col in range(0, 7, 3):
            if checkBox(col,row) == False:
                return False
    return True

def checkEverything():
    # checkRows()
    # checkCols()
    # checkAllBoxes()
    if checkRows() == False:
        return False
    if checkCols() == False:
        return False
    if checkAllBoxes() == False:
        return False
    return True

def isEmpty(position):
    for row in range(0, 9):
        for col in range(0, 9):
            if board[row][col] == 0:
                position[0] = row
                position[1] = col
                return True
    return False

########################### SOLVER ###########################

# def inputNumber(row, col, start):
#     for i in range(start, 10):
#         board[row][col] = i
#         if checkEverything():
#             print("inputNumber check everything -- TRUE:", board)
#             return True
#     # if no valid number for cell, set value back to 0
#     # board[row][col] = 0
#     print("inputNumber check everything -- FALSE:", board)
#     return False

def inputNumber(row, col, number):
    board[row][col] = number
    if checkEverything():
        # print("inputNumber check everything -- TRUE:", board)
        return True
    # if no valid number for cell, set value back to 0
    board[row][col] = 0
    # print("inputNumber check everything -- FALSE:", board)
    return False

def solver():
    print("--------solver()")
    position = [0,0]

    checkEmpty = isEmpty(position)  # find the first empty cell
    # print("check empty:", checkEmpty)
    if checkEmpty == False: # if the board is not empty
        return True
    row = position[0]
    col = position[1]

    for number in range(1, 10):
    # print("current postion", position)
        print("call inputNumber", row, col)
        isValid = inputNumber(row, col, number)  # input number
        print("check input", isValid)

        if isValid:
            board[row][col] = number
            print("assign board - ", board[row][col])
            if solver():
                # print("is SOLVE")
                print("true", board)
                return True
            print("backtrack.....", row, col )
            board[row][col] = 0
    
    print(board)
    return False
   

solver()





