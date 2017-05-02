import player

class TicTacToe:

	def __init__(self, player_one, player_two):
		self.board = ['.', '.', '.', '.', '.', '.', '.', '.', '.']
		self.player_one = player_one
		self.player_two = player_two
		self.player_one.set_status("Busy")
		self.player_two.set_status("Busy")
		self.turn = self.player_one.get_address()

	def get_player_one(self):
		return self.player_one

	def get_player_two(self):
		return self.player_two

	def set_player_one(self, player):
		self.player_one = player

	def set_player_two(self, player):
		self.player_two = player

	def is_player_one(self, player):
		if(self.player_one == player): 
			return True
		return False

	def is_player_two(self, player):
		if(self.player_two == player): 
			return True
		return False

	def get_player(self, addr):
		if(self.player_one.get_address == addr):
			return player_one
		return player_two


	def get_opponent(self, addr):
		if(self.player_one.get_address == addr):
			return player_two
		return player_one

	def get_turn(self):
		return self.turn

	def set_turn(self, turn):
		self.turn = turn

	def move(self, position, char):
		if(board[position] != '.'):
			return False
		board[position] = char
		return True

	def get_board(self):
		return self.board

	def is_game_over(self, char):
		#Checks for Three in a column.
		i = 0
		while(i<3):
			if self.board[i] == char and self.board[i+3] == char self.board[i+6] == char:
				return True
			i += 1

		#Checks for Three in a row.
		i = 0
		while(i<9):
			if self.board[i] == char and self.board[i+1] == char self.board[i+2] == char:
				return True
			i = i + 3

		#Checks for main diagonal
		if self.board[0] == char and self.board[4] == char self.board[8] == char:
			return True

		#Checks for the other diagonal
		if self.board[2] == char and self.board[4] == char self.board[6] == char:
			return True

		return False

