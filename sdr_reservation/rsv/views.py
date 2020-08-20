from django.shortcuts import render, redirect, get_object_or_404
from .models import Board
import datetime


# Create your views here.
def board(request):
    content = Board.objects
    return render(request, 'index.html', {'boards':content})

def create(request):
    return render(request, 'create.html')

def register(request):
    board = Board()
    board.name = request.GET['name']
    board.phone_number = request.GET['phone_number']
    board.start_date = request.GET['start_date']
    board.end_date = request.GET['end_date']
    board.start_time = request.GET['start_time']
    board.end_time = request.GET['end_time']
    board.people = request.GET['people']
    board.memo = request.GET['memo']
    date = request.GET['start_date'].split("-")
    board.m_d = str(date[1]+"_"+date[2])
    board.save()
    return redirect('../../')

def read(request):
    content = Board.objects
    # read = get_object_or_404(Board, pk=board_id)
    return render(request, 'read.html', {'boards':content})

def delete(request, board_id):
    delete = get_object_or_404(Board, pk=board_id)
    delete.delete()
    return redirect('../../')

# views파일에서 pk는 board_id로 고정
def update(request, board_id):
    change = get_object_or_404(Board, pk=board_id) 
    return render(request, 'update.html', {'change':change})

def update_board(request, board_id):
    up = get_object_or_404(Board, pk=board_id)
    up.name = request.GET['name']
    up.phone_number = request.GET['phone_number']
    up.start_date = request.GET['start_date']
    up.end_date = request.GET['end_date']
    up.start_time = request.GET['start_time']
    up.end_time = request.GET['end_time']
    up.people = request.GET['people']
    up.memo = request.GET['memo']
    up.save()
    return redirect('/'+str(board_id))    
