class TicTacToe:
    def draw_board(self, board):
        print('   |   |')
        print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
        print('   |   |')
        print('-----------')
        print('   |   |')
        print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
        print('   |   |')
        print('-----------')
        print('   |   |')
        print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
        print('   |   |')

    def play_again(self):
        print('Do you want to play again? (yes or no)')
        return input().lower().startswith('y')

    def make_move(self, board, letter, move):
        board[move] = letter

    def check_winner(self, bo, le):
        return ((bo[7] == le and bo[8] == le and bo[9] == le) or #  top
        (bo[4] == le and bo[5] == le and bo[6] == le) or    #  middle
        (bo[1] == le and bo[2] == le and bo[3] == le) or    #  bottom
        (bo[7] == le and bo[4] == le and bo[1] == le) or    # down left
        (bo[8] == le and bo[5] == le and bo[2] == le) or    # down middle
        (bo[9] == le and bo[6] == le and bo[3] == le) or    # down right
        (bo[7] == le and bo[5] == le and bo[3] == le) or    # diagonal
        (bo[9] == le and bo[5] == le and bo[1] == le))      # diagonal

    def is_space_free(self, board, move):
        return board[move] == ' '

    def get_player_move(self, board):
        move = ' '
        while move not in '1 2 3 4 5 6 7 8 9'.split() or not self.is_space_free(board, int(move)):
            print('What is your next move? (1-9)')
            move = input()
        return int(move)

    def is_board_full(self, board):
        # Return True if every space on the board has been taken. Otherwise return False.
        for i in range(1, 10):
            if self.is_space_free(board, i):
                return False
        return True

    def run(self):
        print('Welcome to Tic Tac Toe!')

        while True:
            # Reset the board
            theBoard = [' '] * 10
            gameIsPlaying = True
            turn = 'Xplayer'

            while gameIsPlaying:
                if turn == 'Xplayer':
                    # X Player’s turn.
                    self.draw_board(theBoard)
                    move = self.get_player_move(theBoard)
                    self.make_move(theBoard, 'X', move)

                    if self.check_winner(theBoard, 'X'):
                        self.draw_board(theBoard)
                        print('Player X has won the game')
                        gameIsPlaying = False
                    else:
                        if self.is_board_full(theBoard):
                            self.draw_board(theBoard)
                            print('The game is a tie!')
                            break
                        else:
                            turn = 'Oplayer'

                else:
                    # O Player’s turn.
                    self.draw_board(theBoard)
                    move = self.get_player_move(theBoard)
                    self.make_move(theBoard, 'O', move)

                    if self.check_winner(theBoard, 'O'):
                        self.draw_board(theBoard)
                        print('Player O has won the game')
                        gameIsPlaying = False
                    else:
                        if self.is_board_full(theBoard):
                            self.draw_board(theBoard)
                            print('The game is a tie!')
                            break
                        else:
                            turn = 'Xplayer'

            if not self.play_again():
                break
