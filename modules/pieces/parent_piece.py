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
        self.__image = None
        self.__rect = None
        self.__is_moving = False

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
    
    def get_size(self):
        return self.__size

    def get_image(self):
        return self.__image 

    def get_rect(self):
        return self.__rect
    
    def get_is_moving(self):
        return self.__is_moving

    #setters
    def set_name(self, p_name):
        self.__name = p_name

    def set_colour(self, p_colour):
        self.__colour = p_colour

    def set_taken(self, p_taken):
        self.__taken = p_taken

    def set_row(self, p_row):
        self.__row = p_row

    def set_column(self, p_column):
        self.__column = p_column

    def set_size(self, p_size):
        self.__size = p_size

    def set_image(self, p_image):
        self.__image = p_image

    def set_rect(self, p_rect):
        self.__rect = p_rect

    def set_is_moving(self, p_is_moving):
        self.__is_moving = p_is_moving


    #other methods
    def get_legal_moves(self):
        legal_moves = None
        return legal_moves
    
    def remove(self):
        None

    def draw(self, screen):
        None

    def move(self, event, pos):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1: 
            if self.__rect.collidepoint(pos): #if user left clicks on piece
                self.__is_moving = True
    
        if event.type == pygame.MOUSEMOTION and self.__is_moving == True: #if user moves mouse after clicking on piece
            self.__rect.move_ip(event.rel) #update position of the piece by the same change as the mouse position

        if event.type == pygame.MOUSEBUTTONUP and event.button == 1: #if user stops holding down left click
            self.__is_moving = False #stop moving piece
