import pygame

class Piece():

    #constructor
    def __init__(self, name, colour, taken, row, column, size):
        self.__name = name
        self.__colour = colour
        self.__taken = taken
        self.__row = row
        self.__column = column
        self.__size = size
        self.__image = ""

    #getters
    def get_name(self):
        return self.__name

    def get_colour(self):
        return self.__colour

    def get_taken(self):
        return self.__taken

    def get_row(self):
        return self.__row

    def get_column(self):
        return self.__column

    #setters
    def set_name(self, p_name):
        self.__name = p_name

    def set_colour(self, p_colour):
        self.__colour = p_colour

    def set_taken(self, p_taken):
        self.__taken = p_taken

    def move(self, p_row, p_column):
        self.__row = p_row
        self.__column = p_column

    #other methods
    def get_legal_moves(self):
        legal_moves = None
        return legal_moves
    
    def remove(self):
        None

    def draw(self, screen):
        None
