from django.shortcuts import render, redirect
from .eval import evaluate 
from .search import minimax_alphabeta
from django.http import JsonResponse, HttpResponse
import math
import chess

# Create your views here.

def index(request):
    return render(request, "best_move_generator/index.html")

# Function that allows the images to load
def piece_png(request, piece):
    return redirect(f"https://chessboardjs.com/img/chesspieces/wikipedia/{piece}")

# API that calculates the best possible move
def calculate_best_move(request, fen, moves_next):

# Check if request is GET
    if request.method != "GET":
        return JsonResponse({"error": "GET request required."}, status=400)

# If request is GET return best move from fen        
    else:

# Transform into valid fen
        fen = fen.replace("_","/")

# Black or white to move
        isMaximizingPlayer = ""
        if moves_next == "white":
            isMaximizingPlayer = True
        else:
            isMaximizingPlayer = False
            

# TODO: calculate best move
            
        board = chess.Board(f"{fen}")
        best_value, best_moves = minimax_alphabeta(board, 3, -math.inf, math.inf, isMaximizingPlayer)
        print(best_value, best_moves)
        return JsonResponse({"value":str(best_value),"moves":str(best_moves)})