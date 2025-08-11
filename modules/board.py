import pygame
from modules.square import Square

class Board():

    #constructor
    def __init__(self):
        self.__board = [["", "", "", "", "", "", "", ""], ["", "", "", "", "", "", "", ""], 
         ["", "", "", "", "", "", "", ""], ["", "", "", "", "", "", "", ""], ["", "", "", "", "", "", "", ""], 
         ["", "", "", "", "", "", "", ""], ["", "", "", "", "", "", "", ""], ["", "", "", "", "", "", "", ""]]
        self.__fen = ""
        self.__whites_turn = True
        self.__num_of_moves = 0
        self.__game_over = False
        self.__white_square = pygame.Rect(100, 100, 200, 200)

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
        white = True
        for i in range(1, 9):
            for j in range(1, 9):
                if white:
                    colour = "white"
                    if j != 8:
                        white = False
                else:
                    colour = "black"
                    if j != 8:
                        white = True
                square = Square(i, j, 75, colour)
                square.draw(screen)


    

    