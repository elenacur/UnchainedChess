#imports
import pygame
from modules.chess_board.pieces.parent_piece import Piece

#using inheritance of Piece for all these classes

#pawn
class Pawn(Piece):

    #constructor
    def __init__(self, colour, taken, row, column, size):
        super().__init__("pawn", colour, taken, row, column, size) #initialising parent class
        self.__has_moved = False
        self.__en_passant = False
        self.__can_promote = False

        if self.get_colour() == "white": #assigning different images based on colour
            self.set_image(pygame.image.load("assets/chess_pieces_images/white-pawn.png"))
        else:
            self.set_image(pygame.image.load("assets/chess_pieces_images/black-pawn.png"))

        self.set_image(pygame.transform.scale_by(self.get_image(), (self.get_size()/105))) #scaling the image

    #getters
    def get_has_moved(self):
        return self.__has_moved

    def get_en_passant(self):
        return self.__en_passant

    def get_can_promote(self):
        return self.__can_promote
    
    #setters
    def set_has_moved(self, p_has_moved):
        self.__has_moved = p_has_moved

    def set_en_passant(self, p_en_passant):
        self.__en_passant = p_en_passant

    def set_can_promote(self, p_can_promote):
        self.__can_promote = p_can_promote

    #other methods
    def get_legal_moves(self):
        None

    def promote(self, new_piece):
        None

#king
class King(Piece):
    None

