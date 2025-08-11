#imports
import pygame
from modules.chess_board.square import Square

class Board():

    #constructor
    def __init__(self, fen, whites_turn, num_of_moves, game_over):
        self.__board = [["", "", "", "", "", "", "", ""], ["", "", "", "", "", "", "", ""], 
                        ["", "", "", "", "", "", "", ""], ["", "", "", "", "", "", "", ""], 
                        ["", "", "", "", "", "", "", ""], ["", "", "", "", "", "", "", ""], 
                        ["", "", "", "", "", "", "", ""], ["", "", "", "", "", "", "", ""]] #2D array of sqauares
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
                self.__board[i][j] = Square(i, j, 84, colour)

    #getters
    def get_board(self):
        return self.__board
    
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
        None
    
    def draw_whole_board(self, screen): #draws every object in the board array i.e. the whole board
        for i in self.__board:
            for j in i:
                j.draw_square(screen)


    

    