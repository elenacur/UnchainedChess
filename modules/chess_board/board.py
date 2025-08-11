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

        white = True
        for i in range(0, 8):
            for j in range(0, 8):
                if white:
                    colour = "white"
                else:
                    colour = "black"
                if j != 7:
                    white = not white
                self.__board[i][j] = Square(i, j, 75, colour)

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
        self.__board = [["R", "N", "B", "Q", "K", "B", "N", "R"], ["P", "P", "P", "P", "P", "P", "P", "P"], 
         ["", "", "", "", "", "", "", ""], ["", "", "", "", "", "", "", ""], ["", "", "", "", "", "", "", ""], 
         ["", "", "", "", "", "", "", ""], ["p", "p", "p", "p", "p", "p", "p", "p"], 
         ["r", "n", "b", "q", "k", "b", "n", "r"]]
        
    def draw(self, screen):
        for i in self.__board:
            for j in i:
                j.draw(screen)


    

    