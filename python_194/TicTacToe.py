class TicTacToe:

    def __init__(self):
        self._board =[[" "]*3 for i in range(3)]
        self._winner=""
        self.player ="x" 

    def mark_x(self,x,y):
        self._board[x][y]='x'
        self.winner()
        self.player="o"


    def mark_o(self,x,y):
        self._board[x][y]= 'o'
        self.winner()
        self.player="x"


    def winner(self):
        for i in ['x','o']:
            #check all horizontals
            if(self._hori(i)):
                print("the winner is",self._winner)
            #check all verticals
            if(self._vert(i)):
                print("the winner is",self._winner)
            #check 2 diagonals   
            if(self._diag(i)):
                print("the winner is",self._winner)

    def __str__(self):
        row_lis =  ["  |  ".join(self._board[i]) for i in range(3)]
        return "\n -----------\n".join(row_lis)

    def _hori(self,what):
        for i in range(3):
            if(self._board[i][0]==what and self._board[i][1]==what and self._board[i][2]==what):
                self._winner  = what
                return True
        return False

    def _vert(self,what):
        for j in range(3):
            if(self._board[0][j]==what and self._board[1][j]==what and self._board[2][j]==what):
                self._winner = what
                return True
            return False

    def _diag(self,what):
            if(self._board[0][0]==what and self._board[1][1]==what and self._board[2][2]==what):
                self._winner = what
                return True
            return False
            if(self._board[2][0]==what and self._board[1][1] == what and self._board[0][2]==what):
                self._winner = what
                return True
            False
                            ##testing area
game = TicTacToe()
while(True):
    if(game._winner is not ""):
        break
    print("\n the current player is",game.player)
    x_coord= int(input("enter coordinates X"))
    y_coord = int(input("enter coordinates Y"))
    if(game.player == 'x'):
                  game.mark_x(x_coord,y_coord)
                  print(game)
    else:
                  game.mark_o(x_coord,y_coord)
                  print(game)
                  
