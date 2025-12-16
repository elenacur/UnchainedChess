#imports
import pygame
from modules.chess_game.pieces.parent_piece import Piece

#using inheritance of Piece

#king
class King(Piece):

    #constructor
    def __init__(self, board, colour, taken, row, column, size):
        super().__init__("king", board, colour, taken, row, column, size) #initialising parent class
  
        self.set_value(0) #kings do not have a value

        if self.get_colour() == "white": #assigning different images based on colour
            self.set_image(pygame.image.load("assets/chess_pieces_images/white-king.png"))
        else:
            self.set_image(pygame.image.load("assets/chess_pieces_images/black-king.png"))

        self.set_image(pygame.transform.scale_by(self.get_image(), (self.get_size()/105))) #scaling the image

    # getters

    # setters

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

        if self.get_has_moved() == False:
            #making sure no pieces are blocking the castling
            if 0 <= self.get_column() - 3 <= 7 and 0 <= self.get_column() + 2 <= 7:
                if pieces[self.get_row()][self.get_column() + 1] == None: #if no blockage
                    if pieces[self.get_row()][self.get_column() + 2] == None: #if king not going on a piece
                        legal_moves.append([self.get_row(), self.get_column() + 2]) #king side castling allowed

                if pieces[self.get_row()][self.get_column() - 1] == None: #if no blockage
                    if pieces[self.get_row()][self.get_column() - 2] == None: #if king not going on a piece
                        if pieces[self.get_row()][self.get_column() - 3] == None: #checking extra queen side square
                            legal_moves.append([self.get_row(), self.get_column() - 2]) #queen side castling allowed
        return legal_moves