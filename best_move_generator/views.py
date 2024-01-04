from django.shortcuts import render, redirect

# Create your views here.

def index(request):
    return render(request, "best_move_generator/index.html")

# Function that allows the images to load
def piece_png(request, piece):
    return redirect(f"https://chessboardjs.com/img/chesspieces/wikipedia/{piece}")