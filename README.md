# TicTacToe - AI project


### Table of Contents  
* [Introduction](#Introduction)
* [Objectives](#Objectives)  
* [Main concept](#Main-concept) 
* [Problem and its formulation](#Problem-and-its-formulation) 
* [Minimax Algorithm](#Minimax=Algorithm) 
* [Alpha-Beta Algorithm](#Alpha-Beta-Algorithm) 
<a name="headers"/>


## **Introduction:**

This project covers a description and solution to the problem of the Tic-Tac-Toe game and its implementation with the best algorithm to apply the rules of the game and provide the best methods to ensure victory. 



## **Objectives:**

* Applying the principles of Minimax and Alpha-Beta. 

* Understand the distinctions between the Minimax and the Alpha-Beta algorithms in order to select the optimum algorithm. 

* Delivering the game in the most efficient structure and with the optimization technique possible, which reduces the search for the ideal position that leads to win. 

* Instead of dealing with codes, provide the game via entertaining interfaces that enable the reader to explore the game in a useful way. 



## **Main concept:** 

Tic-Tac-Toe is a game in which two players alternately place X and O in compartments spaced in a 3×3 grid, and each player tries to get a row of three X or three O (horizontal, vertical, or diagonal) before the opponent to win. If no one wins, then it is said to be a tie. The major idea is the development of the game using the alpha-beta algorithm to get the best game results. 



## **Problem and its formulation:**

### **Problem:** 

Developing an artificial intelligence that considers all alternatives and chooses the best positions to compete so that it always wins or draws and with the shortest time and space complexity. 

### **Formulation:** 

In artificial intelligence and game theory, we encounter search problems that can be interpreted by a graph of interconnected nodes, each representing a possible state. An intelligent agent must traverse graphs by evaluating each node to reach an optimal state.

Every AI move is based on the final output. If we want to create an AI that never loses, it might end up tied but never lose. So AI has to search from the available moves, which can lead to the best result (a win or even a tie). Nevertheless, there are specificific problems where standard graph search algorithms cannot be applied.
  

## **Minimax Algorithm:** 

Minimax is a type of artificial intelligence that is used in two-player games like tic-tac-toe, checkers, chess, and go. This type of game is known as a "zero-sum game" because, in a mathematical representation, one player wins (+1) and the other loses (-1) or neither player wins (0).  
 
### Minimax Example: 
  ![This is an image](https://telegra.ph/file/7d91d51a81b22c38c6aa7.png)
  
## Alpha-Beta Algorithm: 

Alpha-beta pruning is a search strategy that seeks to minimize the number of nodes in the search tree that are evaluated by the minimax algorithm. It is an adversarial search algorithm that is commonly employed in two-player games for machine play. It stops examining a move when at least one alternative that proves the move is worse than a previously discovered option has been found.

### Alpha-Beta Example: 
  ![This is an image](https://materiaalit.github.io/intro-to-ai/img/diagrams/tictactoe-alphabeta-e8cb918f.png)
  





