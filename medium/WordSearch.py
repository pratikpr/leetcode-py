class WordSearch:
	def exist(self, board, word):
		self.ROWS = len(board)
		self.COLS = len(board[0])
		self.board = board
		
		for row in range(self.ROWS):
			for col in range(self.COLS):
				if self.backtrack(row, col, word):
					return True
				
		return False
		
	def backtrack(self, row, col, word):
		if len(word) == 0:
			return True
		
		if row < 0 or row >= self.ROWS or col < 0 or col >= self.COLS or self.board[row][col] != word[0]:
			return False
		
		self.board[row][col] = "!"
		
		res = False
		
		for RO, CO in [(0,1), (1,0), (0,-1), (-1,0)]:
			ret = self.backtrack(row+RO, col+CO, word[1:])
			if ret:
				break
				
		self.board[row][col] = word[0]
		return ret

	
obj = WordSearch()
board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCB"
print(obj.exist(board, word))
