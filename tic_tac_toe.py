import random

# This class is responsible for managing the Tic-Tac-Toe board & checking the game state
class TTT_cs170_judge:
  # Initializes the empty board
  def __init__(self):
    self.board = []

  # Creates a n x n board  
  def create_board(self, n):
    for i in range(n):
      row = []
      for j in range(n):
        row.append('-')
      self.board.append(row)

  # Prints the board state  
  def display_board(self):
    for row in self.board:
      print(" ".join(row))
    print()

  # Checks if the given player ('X' or 'O') has won
  def is_winner(self, player):
    # Check rows
    for row in self.board:
      if all([cell == player for cell in row]):
        return True

    # Check columns
    for col in range(len(self.board)):
      if all([self.board[row][col] == player for row in range(len(self.board))]):
        return True

    # Check diagonals
    if all([self.board[i][i] == player for i in range(len(self.board))]):
      return True
    if all([self.board[i][len(self.board) - i - 1] == player for i in range(len(self.board))]):
      return True

    return False
  
  # Checks if the board is full
  def is_board_full(self):
    return all([cell in ['X', 'O'] for row in self.board for cell in row])

# Represents the human player
class Player_1:
  # Initializes with the current board
  def __init__(self, judge):
    self.board = judge.board

  # Takes input for the next move
  def my_play(self):
    while True:
      row, col = map(int, input("Enter the row and column numbers separated by space: ").split())

      if 1 <= row <= len(self.board) and 1 <= col <= len(self.board[0]):
        self.board[row-1][col-1] = 'X'
        break
      else:
        print("Wrong coordination!")

# Represents the AI player
class Player_2:
  # Initializes with the current board and game judge
  def __init__(self, judge):
    self.judge = judge
    self.board = judge.board

  # Determines the next move using the Minimax algorithm
  def my_play(self):
    # Minimax for AI
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

  # The Minimax algorithm for determining the best move
  # depth = how many moves ahead we want to search
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

# Main Game Loop
# Function manages the game play
def game_loop():
  n = 3 # Board size
  game = TTT_cs170_judge()
  game.create_board(n)
  starter = random.randint(0, 1)
  win = False

  player1 = Player_1(game)
  player2 = Player_2(game)

  if starter == 0:
    print("Player 1 starts.")
    while not win:
      game.display_board()
      player1.my_play()
      win = game.is_winner('X')
      game.display_board()
      if win:
        print("Player 1 wins!")
        break
      if game.is_board_full():
        print("It's a tie!")
        break

      game.display_board()
      player2.my_play()
      win = game.is_winner('O')
      game.display_board()
      if win:
        print("Player 2 wins!")
        break
      if game.is_board_full():
        print("It's a tie!")
        break
  else:
    print("Player 2 starts.")
    while not win:
      game.display_board()
      player2.my_play()
      win = game.is_winner('O')
      game.display_board()
      if win:
        print("Player 2 wins!")
        break
      if game.is_board_full():
        print("It's a tie!")
        break
      
      game.display_board()
      player1.my_play()
      win = game.is_winner('X')
      game.display_board()
      if win:
        print("Player 1 wins!")
        break
      if game.is_board_full():
        print("It's a tie!")
        break
      
# game_loop()
