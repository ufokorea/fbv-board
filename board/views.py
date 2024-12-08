from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'board/index.html')

from .models import Board

def list(request):
    board_list =Board.objects.all()
    context = {
        'board_list' : board_list,
    }
    return render(
        request, 
        'board/list.html', 
        context
    )
    
def read(request, id):
    board = Board.objects.get(pk=id)
    board.incrementReadCount()
    return render(request, 'board/read.html', {'board':board})

