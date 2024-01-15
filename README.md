# FINAL PROJECT CS50W

## Distinctiveness and Complexity

My project consists of a python chess engine that I wrote myself combined with a library called Chessboard.js that allows the user to input custom chess positions into a UI and calcualte the optimal best move for the given chess position. (Though not as strong as modern chess engines such as Stockfish after some testing my engine represents a decently strong club player around the 1800 to 2000 ELO)

This project is distinct as it doesn't imitate any similar project built durring the courses curriculum and the I believe the complexity is explained by itself.

## Files

We have a variety of files:
-Eval.py: here we find a evaluation function with plenty of dicts, used by the search function when it comes to calculating the best move.
-Search.py: here we find a alphabeta minimax algorithm that the application uses in combination with the evaluation function to calcualte the best move in any given position
-script.js and index.html: In index.html we implement the HTML for the website as well as add the Chessboard.js package that makes the UI possible, in Script.js we find fetch request to allow the page to return the best possible move as well as a function that takes as input the UI board and turns into FEN (Forsyth–Edwards Notation) that we need in the views.py file to calculate the best possible move.

## How to run the application 
- The application is quite simple to run, just run python3 managepy runserver in the main directory and utilize it as a normal webpage.

