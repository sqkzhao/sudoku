from django.shortcuts import render, redirect

def index(request):
    return render(request, 'sudoku.html')

def new_game(request):
    return redirect('/')
def board(request):
    print("-"*50)
    print(request.POST)
    return "hello"
