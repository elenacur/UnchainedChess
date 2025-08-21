#imports
import pygame
from modules.chess_board.pieces.parent_piece import Piece

#using inheritance of Piece

#knight
class Knight(Piece):

    #constructor
    def __init__(self, board, colour, taken, row, column, size):
        super().__init__("knight", board, colour, taken, row, column, size) #initialising parent class
        self.set_value(3)

        if self.get_colour() == "white": #assigning different images based on colour
            self.set_image(pygame.image.load("assets/chess_pieces_images/white-knight.png"))
        else:
            self.set_image(pygame.image.load("assets/chess_pieces_images/black-knight.png"))

        self.set_image(pygame.transform.scale_by(self.get_image(), (self.get_size()/105))) #scaling the image

    #getters
    
    #setters

    #other methods
    def get_legal_moves(self, colour, pieces):
        legal_moves = []
        knight_moves = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)] #ways a knight can move  
        for i in range(0, 8):
            friendly_fire = False #so it can't take a piece of the same colour
            legal_row = self.get_row() + knight_moves[i][0]
            legal_column = self.get_column() + knight_moves[i][1]
            if 0 <= legal_row <= 7 and 0 <= legal_column <= 7:
                if pieces[legal_row][legal_column] != None:
                    if pieces[legal_row][legal_column].get_colour() == colour: 
                        friendly_fire = True
                if friendly_fire == False:
                    #adding this move to the legal_moves list if it's in range and isn't moving to a piece of the same colour
                    legal_moves.append([legal_row, legal_column])
        return legal_moves