#imports
import pygame
from modules.chess_game.pieces.parent_piece import Piece

#using inheritance of Piece

#queen
class Queen(Piece):

    #constructor
    def __init__(self, board, colour, taken, row, column, size):
        super().__init__("queen", board, colour, taken, row, column, size) #initialising parent class
        self.set_value(9)

        if self.get_colour() == "white": #assigning different images based on colour
            self.set_image(pygame.image.load("assets/chess_pieces_images/white-queen.png"))
        else:
            self.set_image(pygame.image.load("assets/chess_pieces_images/black-queen.png"))

        self.set_image(pygame.transform.scale_by(self.get_image(), (self.get_size()/105))) #scaling the image

    #getters- N/A
    
    #setters- N/A

    #other methods
    def get_legal_moves(self, colour, pieces):

        #queens can move in the same ways as the bishop and rook
        list1 = self.get_legal_bishop_moves(colour, pieces)
        list2 = self.get_legal_rook_moves(colour, pieces)
        legal_moves = list1 + list2
        return legal_moves