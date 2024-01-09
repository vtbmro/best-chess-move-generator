from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name = "index"),

    # Necessary path for chessboard.js to work with Django
    path("img/chesspieces/wikipedia/<str:piece>", views.piece_png, name="piece_png"),

    # API
    path("calculate_best_move/<str:fen>/<str:moves_next>" ,views.calculate_best_move, name="calculate_best_move")
]
