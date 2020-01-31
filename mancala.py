class Mancala:
	PLAYER_ONE = 0
	PLAYER_TWO = 1
	PO_BIN = 6
	PT_BIN = 13

	def __init__(self):
		self.board = [0 if ((x==self.PO_BIN) or (x==self.PT_BIN)) else 4 for x in range(14)]
		self.turn = self.PLAYER_ONE

	def end_game(self):
		player_one_score = self.board[self.PO_BIN]
		player_two_score = self.board[self.PT_BIN]
		if(player_one_score > player_two_score):
			print(f"Player One wins by score of {player_one_score} to {player_two_score}")
		elif(player_two_score > player_one_score):
			print(f"Player Two wins by score of {player_two_score} to {player_one_score}")
		else:
			print("Tie game. No one wins :(")

	def game_loop(self):
		self.print_board()
		while(True):
			player_name = "Player One" if (self.turn == self.PLAYER_ONE) else "Player Two"
			mv = int(input(f"{player_name} Choose move: "))
			if (not self.validate_move(mv)):
				print("Invalid move selected")
				continue
			self.move(mv)
			self.print_board()
			if (self.game_over()):
				self.end_game()
				break

	def validate_move(self,bn):
		if(self.turn == self.PLAYER_ONE):
			return ((bn > -1) and (bn < 6))
		else:
			return ((bn > 6) and (bn < 13))

	def game_over(self):
		return (all(b == 0 for b in self.board[:6]) or all(b == 0 for b in self.board[7:13]))

	def move(self, bin_number):
		marbles = self.board[bin_number]
		self.board[bin_number] = 0
		last_bin = bin_number + marbles
		i = (bin_number + 1) % 14
		while(marbles > 0):
			if (i == self.PO_BIN):
				if (self.turn == self.PLAYER_ONE):
					self.board[i] += 1
					marbles -= 1
			elif (i == self.PT_BIN):
				if (self.turn == self.PLAYER_TWO):
					self.board[i] += 1
					marbles -= 1
			else:
				self.board[i] += 1
				marbles -= 1
			i = ((i + 1) % 14)

		if ((last_bin == self.PO_BIN) and (self.turn == self.PLAYER_ONE)):
			self.turn = self.PLAYER_ONE
		elif ((last_bin == self.PT_BIN) and (self.turn == self.PLAYER_TWO)):
			self.turn = self.PLAYER_TWO
		else:
			self.turn = self.PLAYER_ONE if (self.turn == self.PLAYER_TWO) else self.PLAYER_TWO


	def print_board(self):
		row_one = self.board[:6]
		row_two = list(reversed(self.board[7:13]))
		pob = self.board[6]
		ptb = self.board[13]
		print("-----------------------------------------")
		print(f" {row_one} ")
		print(f"{ptb}                  {pob}")
		#print(str(ptb) + "                  " + str(pob) + "        TURN:"+str(self.turn))
		print(f" {row_two} ")
		print("-----------------------------------------")


m = Mancala()
m.game_loop()




