from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect


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
    checkRows()
    checkCols()
    checkAllBoxes()
    if checkRows() == False:
        return False
    if checkCols() == False:
        return False
    if checkAllBoxes() == False:
        return False
    return True

def index(request):
    # print("-"*50)
    print("request post:  ", request.POST)
    # print("request post list:  ", request.POST.getlist('board[1][]'))
    # regenerate board
    new_board = []
    for i in range(9):
        row_arr = []
        for i in request.POST.getlist('board[1][]'):
            value = int(i)
            row_arr.append(value)
        new_board.append(row_arr)
    print("this is new board" , new_board)
    return render(request, 'sudoku.html')

def new_game(request):
    return redirect('/')

# def validate(request):
#     print("INSIDE VALIDATE METHOD")
#     return redirect('/')

