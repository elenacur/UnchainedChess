
import pygame

class Button:

    #constructor
    def __init__(self, x, y, width, height, colour, image):

        self.__x = x
        self.__y = y
        self.__width = width
        self.__height = height
        self.__colour = colour
        self.__image = image

        self.__rect = pygame.Rect(x, y, width, height)
        self.__clicked = False

    #getters
    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def get_width(self):
        return self.__width

    def get_height(self):
        return self.__height

    def get_colour(self):
        return self.__colour

    def get_image(self):
        return self.__image

    def get_rect(self):
        return self.__rect
    
    def get_clicked(self):
        return self.__clicked

    #setters
    def set_x(self, p_x):
        self.__x = p_x
        self.__rect.x = p_x #keep rect in sync

    def set_y(self, p_y):
        self.__y = p_y
        self.__rect.y = p_y #keep rect in sync

    def set_width(self, p_width):
        self.__width = p_width
        self.__rect.width = p_width #keep rect in sync

    def set_height(self, p_height):
        self.__height = p_height
        self.__rect.height = p_height #keep rect in sync

    def set_colour(self, p_colour):
        self.__colour = p_colour

    def set_image(self, p_image):
        self.__image = p_image

    def set_rect(self, p_rect):
        self.__rect = p_rect

    def set_clicked(self, p_clicked):
        self.__clicked = p_clicked


    def draw(self, screen):

        #draw image if any
        if self.__image != None:
            scaled_image = pygame.transform.scale(self.__image, (self.__width, self.__height)) #resize image
            screen.blit(scaled_image, self.__rect.topleft) #draw on screen

    
            

