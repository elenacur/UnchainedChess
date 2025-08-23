#imports
import pygame
from modules.chess_board.pieces.parent_piece import Piece

#using inheritance of Piece

#king
class King(Piece):

    #constructor
    def __init__(self, board, colour, taken, row, column, size):
        super().__init__("king", board, colour, taken, row, column, size) #initialising parent class
        self.__checked = False #for legal moves
        self.__checkmated = False #for ending the game
        self.__has_moved = False #for castling
        self.__can_move = False #for stalemates
        self.set_value(0) #kings do not have a value

        if self.get_colour() == "white": #assigning different images based on colour
            self.set_image(pygame.image.load("assets/chess_pieces_images/white-king.png"))
        else:
            self.set_image(pygame.image.load("assets/chess_pieces_images/black-king.png"))

        self.set_image(pygame.transform.scale_by(self.get_image(), (self.get_size()/105))) #scaling the image

    # getters
    def get_checked(self):
        return self.__checked

    def get_checkmated(self):
        return self.__checkmated

    def get_has_moved(self):
        return self.__has_moved

    def get_can_move(self):
        return self.__can_move

    # setters
    def set_checked(self, p_checked):
        self.__checked = p_checked

    def set_checkmated(self, p_checkmated):
        self.__checkmated = p_checkmated

    def set_has_moved(self, p_has_moved):
        self.__has_moved = p_has_moved

    def set_can_move(self, p_can_move):
        self.__can_move = p_can_move

    #other methods
    def get_legal_moves(self, colour, pieces):
        legal_moves = []
        king_moves = [(1, 1), (1, -1), (-1, 1), (-1, -1), (0, 1), (0, -1), (1, 0), (-1, 0)] #ways a king can move  
        for i in range(0, 8):
            friendly_fire = False #so it can't take a piece of the same colour
            legal_row = self.get_row() + king_moves[i][0]
            legal_column = self.get_column() + king_moves[i][1]
            if 0 <= legal_row <= 7 and 0 <= legal_column <= 7:
                if pieces[legal_row][legal_column] != None:
                    if pieces[legal_row][legal_column].get_colour() == colour: 
                        friendly_fire = True
                if friendly_fire == False:
                    #adding this move to the legal_moves list if it's in range and isn't moving to a piece of the same colour
                    legal_moves.append([legal_row, legal_column])
        return legal_moves