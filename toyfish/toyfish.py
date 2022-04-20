import json
class Chess:
	def __init__(self,filename):
		with open(filename) as f:
			self.__dict__=json.loads(f.read())#讀入json檔
			#棋盤↓
			self.board=list('         \n'*2+' '+''.join([
			'.'* int(c) if c.isdigit() else c 
			for c in 
			self.fen.split()[0].replace('/','\n ')
			])+'\n'+'         \n'*2)
			
			self.side=0 if self.fen.split()[1]=='w' else 1#先手方
			
	def generate_move(self):
		for square in range(len(self.board)):
			piece = self.board[square]
			if piece not in ' .\n' and self.colors[piece]==self.side:
				for offset in self.directions[piece]:
					target_square = square
					 captured_piece = self.board[target_square]
					 if captured_piece in ' \n':break
						 
					
			
chess = Chess("setup.json")
print(''.join(chess.board))
print(chess.side)
chess.generate_move()



