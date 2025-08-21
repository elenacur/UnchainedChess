#imports
import pygame
from modules.chess_board.pieces.parent_piece import Piece

#using inheritance of Piece for all these classes

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
    def legal(self, colour, pieces):
        friendly_fire = False
        moving_forward = False
        taking_diagonally = False

        if colour == "white":
            colour_factor = -1
        else:
            colour_factor = 1

        if self.get_new_column() == self.get_column():
            if self.get_new_row() == self.get_row() + colour_factor * 1:
                if pieces[self.get_new_row()][self.get_new_column()] == None:
                    self.__has_moved = True
                    return True
            elif self.get_new_row() == self.get_row() + colour_factor * 2 and self.__has_moved == False:
                if pieces[self.get_new_row()][self.get_new_column()] == None and pieces[self.get_row() + colour_factor][self.get_column()] == None:
                    self.__has_moved = True
                    return True
        elif self.get_new_row() == self.get_row() + colour_factor:
            if self.get_new_column() == self.get_column() + 1 or self.get_new_column() == self.get_column() + -1:
                if pieces[self.get_new_row()][self.get_new_column()] != None:
                    if pieces[self.get_new_row()][self.get_new_column()].get_colour() != colour:
                        return True



    def promote(self, new_piece):
        None

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
    def get_legal_moves(self):
        None
    
    def castle(self):
        None

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
    def legal(self, colour, pieces):
        friendly_fire = False
        legal_moves = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)] #ways a knight can move  
        for i in range(0, 8):
            legal_row = self.get_row() + legal_moves[i][0]
            legal_column = self.get_column() + legal_moves[i][1]
            if pieces[self.get_new_row()][self.get_new_column()] != None:
                if pieces[self.get_new_row()][self.get_new_column()].get_colour() == colour:
                    friendly_fire = True
            if self.get_new_row() == legal_row and self.get_new_column() == legal_column and 0 <= self.get_new_row() <= 7 and 0 <= self.get_new_column() <= 7 and friendly_fire == False:
                return True

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
    def get_legal_moves(self):
        None

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

    #getters
    
    #setters

    #other methods
    def get_legal_moves(self):
        None

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
    def get_legal_moves(self):
        None

