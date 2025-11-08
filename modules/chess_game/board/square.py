#imports
import pygame

class Square:

    #constructor
    def __init__(self, row, column, size, colour):
        self.__row = row
        self.__column = column
        self.__size = size
        self.__colour = colour
        self.__piece = None
        self.__highlight = False
        self.__x = self.__column * self.__size + 210 #top left x coord
        self.__y = self.__row * self.__size + 70 #top left y coord
        self.__rect = pygame.Rect(self.__x, self.__y, self.__size, self.__size) #square without colour

    #getters
    def get_row(self):
        return self.__row

    def get_column(self):
        return self.__column
    
    def get_size(self):
        return self.__size

    def get_colour(self):
        return self.__colour

    def get_piece(self):
        return self.__piece

    def get_highlight(self):
        return self.__highlight
    
    def get_x(self):
        return self.__x
    
    def get_y(self):
        return self.__y

    def get_rect(self):
        return self.__rect

    #setters- some attributes will never be changed so setters are unnecessary
    def set_colour(self, p_colour):
        self.__colour = p_colour

    def set_piece(self, p_piece):
        self.__piece = p_piece

    def set_highlight(self, p_highlight):
        self.__highlight = p_highlight

    #other methods
    def draw_square(self, screen): #draws one square
        pygame.draw.rect(screen, self.__colour, self.__rect)