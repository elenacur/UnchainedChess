#imports
import pygame
from modules.chess_game.pieces.parent_piece import Piece

#using inheritance of Piece

#bishop
class Bishop(Piece):

    #constructor
    def __init__(self, board, colour, taken, row, column, size):
        super().__init__("bishop", board, colour, taken, row, column, size) #initialising parent class
        self.set_value(3)

        if self.get_colour() == "white": #assigning different images based on colour
            self.set_image(pygame.image.load("assets/chess_pieces_images/white-bishop.png"))
        else:
            self.set_image(pygame.image.load("assets/chess_pieces_images/black-bishop.png"))

        self.set_image(pygame.transform.scale_by(self.get_image(), (self.get_size()/105))) #scaling the image

    #getters
    
    #setters

    #other methods
    def get_legal_moves(self, colour, pieces):
        return self.get_legal_bishop_moves(colour, pieces)