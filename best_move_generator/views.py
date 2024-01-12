from django.shortcuts import render, redirect
from .search import minimax_alphabeta
from django.http import JsonResponse
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

    # Not GET request
    if request.method != "GET":
        return JsonResponse({"error": "GET request required."}, status=400)

    # GET request        
    else:

        # Transform into valid fen
        fen = fen.replace("_","/")
        board = chess.Board(f"{fen}")

        print(fen)

        # TODO: Check that fen only has 1 king of each color (Valid FEN)
        if fen.count("k") != 1 or fen.count("K") != 1:
            return  JsonResponse({"Invalid board": "Please input only 1 king of each color"})
        
        # Black or white to move
        isMaximizingPlayer = ""
        if moves_next == "white":
            isMaximizingPlayer = True
            
        elif moves_next == "black":
            # Added this so player can also select move with black
            board.turn = False
            isMaximizingPlayer = False
        
        best_value, best_moves = minimax_alphabeta(board, 5, -math.inf, math.inf, isMaximizingPlayer)
        return JsonResponse({"value":str(best_value),"move":str(best_moves)})