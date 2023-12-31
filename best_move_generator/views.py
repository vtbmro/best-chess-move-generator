from django.shortcuts import render, redirect
from .eval import evaluate 
from .search import minimax_alphabeta
from django.http import JsonResponse

# Create your views here.

def index(request):
    return render(request, "best_move_generator/index.html")

# Function that allows the images to load
def piece_png(request, piece):
    return redirect(f"https://chessboardjs.com/img/chesspieces/wikipedia/{piece}")

# API that calculates the best possible move
def calculate_best_move(request, fen):

# Check if request is GET
    if request.method != "GET":
        return JsonResponse({"error": "GET request required."}, status=400)

# If request is GET return best move from fen        
    else:

# Transform into valid fen
        fen = fen.replace("_","/")

# TODO: get input from player wheter it is white to play or black to play


        return JsonResponse({"current board fen":f"{fen}"})