#imports
import pygame
from modules.chess_board.square import Square
from modules.chess_board.pieces.child_pieces import Pawn

class Board():

    #constructor
    def __init__(self, square_size, fen, whites_turn, num_of_moves, game_over):
        self.__board = [["", "", "", "", "", "", "", ""], ["", "", "", "", "", "", "", ""], 
                        ["", "", "", "", "", "", "", ""], ["", "", "", "", "", "", "", ""], 
                        ["", "", "", "", "", "", "", ""], ["", "", "", "", "", "", "", ""], 
                        ["", "", "", "", "", "", "", ""], ["", "", "", "", "", "", "", ""]] #2D array of sqauares
        self.__pieces = [[None, None, None, None, None, None, None, None], 
                         [None, None, None, None, None, None, None, None], 
                         [None, None, None, None, None, None, None, None], 
                         [None, None, None, None, None, None, None, None], 
                         [None, None, None, None, None, None, None, None], 
                         [None, None, None, None, None, None, None, None], 
                         [None, None, None, None, None, None, None, None], 
                         [None, None, None, None, None, None, None, None]] #2D array of pieces
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
    def reset_board(self):
        
        #pawns
        for i in range(0, 8):
            self.__pieces[1][i] = Pawn(self, "black", False, 1, i, 84)

        for i in range(0, 8):
            self.__pieces[6][i] = Pawn(self, "white", False, 6, i, 84)

        #rooks

        #knights

        #bishops

        #queens

        #kings
    
    def draw_whole_board(self, screen): #draws every object in the board array i.e. the whole board
        for i in self.__board:
            for j in i:
                j.draw_square(screen)
    
    def draw_all_pieces(self, screen): #draws every object in the piece array and allows them to move
        for i in self.__pieces:
            for j in i:
                if j != None:
                    j.draw_piece(screen)
    
    def move_pieces(self, event, pos):
        for list in self.__pieces:
            for piece in list:
                if piece != None:
                    piece.move(event, pos)

    def print_pieces(self):
        for list in self.__pieces:
            for piece in list:
                if piece != None:
                    print(piece.get_name(), end = " ")
                else:
                    print("None", end = " ")
            print()


    

    