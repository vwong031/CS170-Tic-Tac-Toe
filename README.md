# CS170-Tic-Tac-Toe Report

In this tic-tac-toe game, either the AI or the human player will start first. The AI player will make decisions based on the best move to take. The human player may choose any move by inputting the row and column number. It is important to implement an AI algorithm for the tic-tac-toe game because AI adds intelligence to the game by trying to make the best move, therefore, making it more challenging and fun for the human player. If the algorithm just chose any open spot randomly, the game would not be as fun. 

The AI algorithm I have implemented is called the Minimax algorithm. The Minimax algorithm is a decision-making algorithm and is commonly used in games similar to tic-tac-toe. The strengths of the Minimax algorithm is that it makes the best/optimal choices. Its weakness is that it can be inefficient for bigger trees as it will take a long time to search the branches. I did not consider any other algorithms as the instructions stated to implement the Minimax algorithm.
 
Consider the following example: Imagine the current board looks like the following: 
![IMG-3405](https://github.com/vwong031/CS170-Tic-Tac-Toe/assets/74090811/40a3f499-95d1-4348-8129-34cf721ed874)

  
The my_play() function is called to determine the AI’s next move. The AI player is evaluating the best move using the Minimax algorithm. It does this by recursively evaluating each possible move by simulating the future game state and picking which move leads to the highest score. 

This function determines the next move using the Minimax algorithm
  
    def my_play(self):
  
    best_score = float('-inf')
    indices = None
    alpha = float('-inf')
    beta = float('inf')
    
    for i in range(len(self.board)):
      for j in range(len(self.board[i])):
        if self.board[i][j] == '-':
          self.board[i][j] = 'O'
          score = self.minimax(self.board, 0, alpha, beta, False)
          self.board[i][j] = '-'
         
          if score > best_score:
            best_score = score
            indices = (i, j)
           
            alpha = max(alpha, best_score)


    self.board[indices[0]][indices[1]] = 'O'


    def minimax(self, board, depth, alpha, beta, maximizing):
    # Base Case: Checks to see who is the winner (if there is a winner)
    if self.judge.is_winner('O'):
      return 1
    if self.judge.is_winner('X'):
      return -1
    if self.judge.is_board_full():
      return 0

    if maximizing:
      best_score = float('-inf')
      for i in range(len(board)):
        for j in range(len(board[i])):
          if board[i][j] == '-':
            board[i][j] = 'O'
            score = self.minimax(board, depth + 1, alpha, beta, False)
            board[i][j] = '-'
            best_score = max(score, best_score)
            
            alpha = max(alpha, score)
            if beta <= alpha:
              break
            
      return best_score
    else:
      best_score = float('inf')
      for i in range(len(board)):
        for j in range(len(board[i])):
          if board[i][j] == '-':
            board[i][j] = 'X'
            score = self.minimax(board, depth + 1, alpha, beta, True)
            board[i][j] = '-'
            best_score = min(score, best_score)  
            beta = min(beta, score)
            
            if beta <= alpha:
              break
            
      return best_score


The Minimax algorithm assigns a score to each game state, with ‘O’ being positive and ‘X’ being negative. If the score is 0, that means there is a tie. The minimax function will continue until all empty cells are considered. 

Because alpha-beta pruning is implemented, it will make the Minimax algorithm more efficient by reducing the number of nodes evaluated in the tree. The alpha value represents the minimum score of the maximizing player and the beta value represents the maximum score of the minimizing player. 

As the Minimax algorithm runs, it will keep track of the alpha and beta values for each node. For the maximizing player, if the Minimax algorithm finds a node with a value greater than or equal to beta, it will search the rest of the children except that branch. For the minimizing player, if the Minimax algorithm finds a node with a value less than or equal to alpha, it will check the other nodes. As mentioned above, the AI player will pick the move that gives the highest score. In this case, the AI identifies that the best move is to place ‘O’ at (1, 2).
![60476](https://github.com/vwong031/CS170-Tic-Tac-Toe/assets/74090811/e00f92d1-13da-4d6c-99ec-36f5a48d4840)


The Minimax algorithm seems to be a sufficient algorithm for games like tic-tac-toe. It provides intelligence to the games, which makes it more challenging and fun for players. I can improve the Minimax algorithm by implementing Alpha-Beta Pruning (which I did in my code since it got an error for not being efficient enough (https://youtu.be/l-hh51ncgDI?si=yAZSBImXYObtm-rg). This will reduce the number of nodes that the Minimax algorithm needs to search by choosing which branches need to and do not need to be searched. This then improves runtime for larger trees. I tried doing research and I could not find many ways to improve the Minimax algorithm further.

## How To Run the Code
You may run the code by uncommenting game_play() at the very bottom of the file and run it in your own IDE. I personally use VSCode. Press the run button and either the AI ('O') will start or you will start ('X'). When playing, input the row and column number that you want to place your 'X' at. When the game is over, you will get a message indicating if you won or lost. You may restart by pressing the run/play button again.

## Sources:

This source is a video I used to help me understand the Minimax algorithm as well as implement alpha-beta pruning
https://youtu.be/l-hh51ncgDI?si=yAZSBImXYObtm-rg 
