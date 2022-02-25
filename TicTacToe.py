class tictactoe:
    def __init__(self):
        self.board = []
    
    def createBoard(self):
        for i in range(3):
            row = []
            for j in range(3):
                row.append('-')
            self.board.append(row)
    
    def showBoard(self):
        for row in self.board:
            for val in row:
                print(val, end = ' ')
            print()

    def switchPlayer(self, player):
        if player == 'X':
            player = 'O'
            return player
        else:
            player = 'X'
            return player
    
    def checkIfPlaceIsTaken(self, pos, entries): 
        counter = 0
        taken = False
        for i in range(3):
            for j in range(3): 
                if counter == pos and (self.board[i][j] == 'O' or self.board[i][j] == 'X'): 
                    taken = True
                    while taken:
                        newpos = input('Place is already taken by another marker. Please select another spot:')
                        while newpos not in entries:
                            newpos = input("Entry invalid. Enter value between 0-8:")
                        if newpos != pos:
                            taken = False
                    return int(newpos)
                counter += 1
        return pos

    def placeMarkerOnBoard(self, player, pos):
        counter = 0
        for i in range(3):
            for j in range(3):
                if counter == pos and self.board[i][j] != 'O' and self.board[i][j] != 'X':
                    self.board[i][j] = player
                counter += 1
    
    def isTheBoardFilled(self, stillPlaying, player):
        counter = 0
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == 'O' or self.board[i][j] == 'X':
                    counter += 1
                if counter == 9:
                    stillPlaying = False
                    player = 'No one'
        return stillPlaying, player
    
    def playerWon(self, player): 
        for i in range(len(self.board)):
            win = True
            for j in range(len(self.board)):
                if self.board[i][j] != player:
                    win = False
                    break
            if win:
                return win

        for i in range(len(self.board)):
            win = True
            for j in range(len(self.board)):
                if self.board[j][i] != player:
                    win = False
                    break
            if win:
                return win
        
        for i in range(len(self.board)):
            win = True
            if self.board[i][i] != player:
                win = False
                break
        if win:
            return win

        for i in range(len(self.board)):
            win = True
            if self.board[i][len(self.board) - i - 1] != player:
                win = False
                break
        if win:
            return win

    def playGame(self):
        self.createBoard()
        stillPlaying = True
        entries = ['0','1','2','3','4','5','6','7','8']
        player = 'X'

        while stillPlaying:
            print('Player ' + player + ' turn')
            self.showBoard()
            pos = input("Enter a place between 0-8:")
            while pos not in entries:
                pos = input("Entry invalid. Enter value between 0-8:")
            pos = int(pos)
            pos = self.checkIfPlaceIsTaken(pos, entries)
            self.placeMarkerOnBoard(player, pos)
            if self.playerWon(player):
                break
            stillPlaying,player = self.isTheBoardFilled(stillPlaying, player)
            if stillPlaying == False:
                break
            player = self.switchPlayer(player)
        
        print("Winner is " + player)
        self.showBoard()

tic_tac_toe = tictactoe()
tic_tac_toe.playGame()