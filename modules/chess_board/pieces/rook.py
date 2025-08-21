#imports
import pygame
from modules.chess_board.pieces.parent_piece import Piece

#using inheritance of Piece

#rook
class Rook(Piece):

    #constructor
    def __init__(self, board, colour, taken, row, column, size):
        super().__init__("rook", board, colour, taken, row, column, size) #initialising parent class
        self.__has_moved = False #for castling
        self.set_value(5)

        if self.get_colour() == "white": #assigning different images based on colour
            self.set_image(pygame.image.load("assets/chess_pieces_images/white-rook.png"))
        else:
            self.set_image(pygame.image.load("assets/chess_pieces_images/black-rook.png"))

        self.set_image(pygame.transform.scale_by(self.get_image(), (self.get_size()/105))) #scaling the image

    #getters
    def get_has_moved(self):
        return self.__has_moved
    
    #setters
    def set_has_moved(self, p_has_moved):
        self.__has_moved = p_has_moved

    #other methods
    def get_legal_moves(self, colour, pieces):
        return self.get_legal_rook_moves(colour, pieces)

    def castle(self):
        None