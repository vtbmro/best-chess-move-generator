import chess
import copy
import math
import sys 
from .eval import evaluate

# The function takes as input: board, depth, -math.infinity, math.infinity and True if 
# it is whites turn or flase if it is blacks turn

def minimax_alphabeta(node, depth, alpha, beta, isMaximizingPlayer):
    
# Base case, reached desired depth or game is over
    if depth == 0 or node.is_checkmate():
        return evaluate(node), None

    # White to play 
    if isMaximizingPlayer:

        best_move = None 

        # In white's case we make value -infinity since, when the evaluate function is favorable
        # for black it returns a positive integer
        value = -math.inf

        # Iterate trough moves and call funcion recursively
        for child in list(node.legal_moves):

            # Creating another board where we play each move
            temp = copy.deepcopy(node)
            temp.push_san(f"{child}")

            # Calling function recursively
            child_value, _ = minimax_alphabeta(temp, depth - 1, alpha, beta, False)

            if child_value > value:
                value = child_value

                # Add move if its better
                best_move = child


            alpha = max(alpha, value)

            # Prune the search tree if necessary
            if value >= beta:
                break

        return value, best_move

# Black to play
    else:
        # In black's case we make value infinity since, when the evaluate function is favorable
        # for black it returns a negative integer
        value = math.inf
        best_move = None

        for child in list(node.legal_moves):
            temp = copy.deepcopy(node)
            temp.push_san(f"{child}")

            child_value, _ = minimax_alphabeta(temp, depth - 1, alpha, beta, True)

            if child_value < value:
                value = child_value
                best_move = child 

            beta = min(beta, value)

            if value <= alpha:
                break

        return value, best_move