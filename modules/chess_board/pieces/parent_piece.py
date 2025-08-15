#imports
import pygame

class Piece():

    #constructor
    def __init__(self, name, board, colour, taken, row, column, size):
        self.__name = name
        self.__board = board
        self.__colour = colour
        self.__taken = taken
        self.__row = row
        self.__column = column
        self.__size = size
        self.__image = None
        self.__is_moving = False
        self.__original_pos = None
        self.__rect = pygame.Rect(self.__column * self.__size + 210, self.__row * self.__size + 70, 
                            self.__size, self.__size) #creating rect that's same size and position as given square
        
    #getters
    def get_name(self):
        return self.__name
    
    def get_board(self):
        return self.__board

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

    def draw_piece(self, screen):
        #create a rect that is the image's size and position, put this rect at the centre of self.__rect
        screen.blit(self.__image, self.__image.get_rect(center=self.__rect.center)) #blit image and rect
        pygame.draw.rect(screen, (255, 0, 0), self.__rect, 2) #temporary outline for testing

    #allows user to move self.__rect
    def move(self, event, pos):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.__rect.collidepoint(pos): #if user left clicks on rect
                self.__is_moving = True
                self.__original_pos = self.__rect.center
    
        if event.type == pygame.MOUSEMOTION and self.__is_moving == True: #if user moves mouse after clicking on rect
            self.__rect.center = pos #update position of rect's centre to position of mouse

        if event.type == pygame.MOUSEBUTTONUP and event.button == 1 and self.__is_moving == True: #if user stops holding down left click
            self.__is_moving = False #stop moving rect

            #moving piece to centre of square the user drops the rect on
            not_on_a_square = 0
            for list in self.__board.get_board():
                for square in list:
                    if square.get_rect().collidepoint(pos):
                        self.__rect.center = square.get_rect().center
                        self.__board.set_pieces(None, self.__row, self.__column)
                        self.__column = square.get_column()
                        self.__row = square.get_row()
                        self.__board.set_pieces(self, self.__row, self.__column)
                    else:
                        not_on_a_square += 1
            if not_on_a_square == 64:
                self.__rect.center = self.__original_pos




