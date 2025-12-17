#imports
import pygame

class Square:

    #constructor
    def __init__(self, row, column, size, colour):
        self.__row = row
        self.__column = column
        self.__size = size
        self.__colour = colour
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
    
    def get_x(self):
        return self.__x
    
    def get_y(self):
        return self.__y

    def get_rect(self):
        return self.__rect

    #setters
    def set_row(self, p_row):
        self.__row = p_row
    
    def set_column(self, p_column):
        self.__column = p_column

    def set_size(self, p_size):
        self.__size = p_size

    def set_colour(self, p_colour):
        self.__colour = p_colour

    def set_x(self, p_x):
        self.__x = p_x

    def set_y(self, p_y):
        self.__y = p_y
    
    def set_rect(self, p_rect):
        self.__rect = p_rect


    #other methods
    def draw_square(self, screen): #draws one square
        pygame.draw.rect(screen, self.__colour, self.__rect)