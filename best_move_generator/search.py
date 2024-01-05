import chess
import copy
import math
import sys 

# The function takes as input: board, depth, -math.infinity, math.infinity and True if 
# it is whites turn or flase if it is blacks turn

def minimax_alphabeta(node, depth, alpha, beta, isMaximizingPlayer):
    
# Base case, reached desired depth or game is over
    if depth == 0 or node.is_checkmate():
        return evaluate(node), []

    # White to play 
    if isMaximizingPlayer:

        # In white's case we make value -infinity since, when the evaluate function is favorable
        # for black it returns a positive integer
        value = -math.inf

        # Store best sequence of moves
        best_moves = []

        # Iterate trough moves and call funcion recursively
        for child in list(node.legal_moves):

            # Creating another board where we play each move
            temp = copy.deepcopy(node)
            temp.push_san(f"{child}")

            # Calling function recursively
            child_value, child_moves = minimax_alphabeta(temp, depth - 1, alpha, beta, False)

            if child_value > value:
                value = child_value

                # Add move if its better
                best_moves = [child] + child_moves


            alpha = max(alpha, value)

            # Prune the search tree if necessary
            if value >= beta:
                break

        return value, best_moves

# Black to play
    else:
        # In black's case we make value infinity since, when the evaluate function is favorable
        # for black it returns a negative integer
        value = math.inf

        best_moves = []

        for child in list(node.legal_moves):
            temp = copy.deepcopy(node)
            temp.push_san(f"{child}")

            child_value, child_moves = minimax_alphabeta(temp, depth - 1, alpha, beta, True)

            if child_value < value:
                value = child_value
                best_moves = [child] + child_moves

            beta = min(beta, value)

            if value <= alpha:
                break

        return value, best_moves