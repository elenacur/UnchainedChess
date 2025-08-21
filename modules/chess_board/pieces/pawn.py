#imports
import pygame
from modules.chess_board.pieces.parent_piece import Piece

#using inheritance of Piece

#pawn
class Pawn(Piece):

    #constructor
    def __init__(self, board, colour, taken, row, column, size):
        super().__init__("pawn", board, colour, taken, row, column, size) #initialising parent class
        self.__has_moved = False #for checking if pawn can move two squares
        self.__en_passant = False #for en passant
        self.__can_promote = False #for promoting
        self.set_value(1)

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
    def get_legal_moves(self, colour, pieces):
        legal_moves = []

        #pawns can only move in one direction depending on their colour
        if colour == "white":
            colour_factor = -1
        else:
            colour_factor = 1
        
        #moving 1 square forward
        if pieces[self.get_row() + colour_factor][self.get_column()] == None:
            legal_moves.append([self.get_row() + colour_factor, self.get_column()])
            #moving 2 squares forward
            if pieces[self.get_row() + (colour_factor * 2)][self.get_column()] == None and self.__has_moved == False:
                legal_moves.append([self.get_row() + (colour_factor * 2), self.get_column()])
                self.__has_moved = True

        #taking diagonally
        for i in range(-1, 2, 2): #-1 for left, 1 for right
            if 0 <= (self.get_row() + colour_factor) <= 7 and 0 <= (self.get_column() + i) <= 7:
                if pieces[self.get_row() + colour_factor][self.get_column() + i] != None:
                    if pieces[self.get_row() + colour_factor][self.get_column() + i].get_colour() != colour:
                        legal_moves.append([self.get_row() + colour_factor, self.get_column() + i])
        return legal_moves

    def promote(self, new_piece):
        None