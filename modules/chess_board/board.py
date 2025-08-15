#imports
from modules.chess_board.square import Square
from modules.chess_board.pieces.child_pieces import Pawn, Rook, Knight, Bishop, Queen, King

class Board():

    #constructor
    def __init__(self, square_size, fen, whites_turn, num_of_moves, game_over):
        self.__board = [["", "", "", "", "", "", "", ""], ["", "", "", "", "", "", "", ""], 
                        ["", "", "", "", "", "", "", ""], ["", "", "", "", "", "", "", ""], 
                        ["", "", "", "", "", "", "", ""], ["", "", "", "", "", "", "", ""], 
                        ["", "", "", "", "", "", "", ""], ["", "", "", "", "", "", "", ""]] #2D array of Square objects
        self.__pieces = [[None, None, None, None, None, None, None, None], 
                         [None, None, None, None, None, None, None, None], 
                         [None, None, None, None, None, None, None, None], 
                         [None, None, None, None, None, None, None, None], 
                         [None, None, None, None, None, None, None, None], 
                         [None, None, None, None, None, None, None, None], 
                         [None, None, None, None, None, None, None, None], 
                         [None, None, None, None, None, None, None, None]] #2D array of Piece objects
        self.__square_size = square_size
        self.__fen = fen
        self.__whites_turn = whites_turn
        self.__num_of_moves = num_of_moves
        self.__game_over = game_over

        #putting Square objects in the board array, alternating black and white
        white = True
        for i in range(0, 8):
            for j in range(0, 8):
                if white:
                    colour = "white"
                else:
                    colour = (144, 149, 128)
                if j != 7: #start of new row is same colour as end of previous row so colour should not change
                    white = not white
                self.__board[i][j] = Square(i, j, self.__square_size, colour)

    #getters
    def get_board(self):
        return self.__board
    
    def get_pieces(self):
        return self.__pieces
    
    def get_fen(self):
        return self.__fen
    
    def get_whites_turn(self):
        return self.__whites_turn
    
    def get_num_of_moves(self):
        return self.__num_of_moves
    
    def get_game_over(self):
        return self.__game_over
    
    #setters
    def set_board(self, p_board):
        self.__board = p_board

    def set_pieces(self, new_piece, row, column):
        self.__pieces[row][column] = new_piece
    
    def set_fen(self, p_fen):
        self.__fen = p_fen

    def set_whites_turn(self, p_whites_turn):
        self.__whites_turn = p_whites_turn
    
    def set_num_of_moves(self, p_num_of_moves):
        self.__num_of_moves = p_num_of_moves
    
    def set_game_over(self, p_game_over):
        self.__game_over = p_game_over

    #other methods
    def reset_board(self): #filling pieces array with Piece objects in order of chess starting position
        
        #pawns
        for i in range(0, 8):
            self.__pieces[1][i] = Pawn(self, "black", False, 1, i, 84)

        for i in range(0, 8):
            self.__pieces[6][i] = Pawn(self, "white", False, 6, i, 84)

        #rooks
        self.__pieces[0][0] = Rook(self, "black", False, 0, 0, 84)
        self.__pieces[0][7] = Rook(self, "black", False, 0, 7, 84)
        self.__pieces[7][0] = Rook(self, "white", False, 7, 0, 84)
        self.__pieces[7][7] = Rook(self, "white", False, 7, 7, 84)

        #knights
        self.__pieces[0][1] = Knight(self, "black", False, 0, 1, 84)
        self.__pieces[0][6] = Knight(self, "black", False, 0, 6, 84)
        self.__pieces[7][1] = Knight(self, "white", False, 7, 1, 84)
        self.__pieces[7][6] = Knight(self, "white", False, 7, 6, 84)

        #bishops
        self.__pieces[0][2] = Bishop(self, "black", False, 0, 2, 84)
        self.__pieces[0][5] = Bishop(self, "black", False, 0, 5, 84)
        self.__pieces[7][2] = Bishop(self, "white", False, 7, 2, 84)
        self.__pieces[7][5] = Bishop(self, "white", False, 7, 5, 84)

        #queens
        self.__pieces[0][3] = Queen(self, "black", False, 0, 3, 84)
        self.__pieces[7][3] = Queen(self, "white", False, 7, 3, 84)

        #kings
        self.__pieces[0][4] = King(self, "black", False, 0, 4, 84)
        self.__pieces[7][4] = King(self, "white", False, 7, 4, 84)
    
    def draw_whole_board(self, screen): #draws every object in the board array i.e. the whole board
        for i in self.__board:
            for j in i:
                j.draw_square(screen)
    
    def draw_all_pieces(self, screen): #draws every object in the piece array
        for i in self.__pieces:
            for j in i:
                if j != None:
                    j.draw_piece(screen)
    
    def move_pieces(self, event, pos): #allows user to move pieces
        for list in self.__pieces:
            for piece in list:
                if piece != None:
                    piece.move(event, pos)

    def print_pieces(self): #prints the current board position in terminal
        for list in self.__pieces:
            for piece in list:
                if piece != None:
                    print(piece.get_name(), end = " ")
                else:
                    print("None", end = " ")
            print()


    

    