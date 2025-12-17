#imports
import pygame
from modules.user_interface.button import Button

class FreeModeButton(Button):

    #constructor
    def __init__(self, x, y, width, height, image):
        super().__init__(x, y, width, height, image)


    #checks if user clicks on button and carries out appropriate response
    def check_if_clicked(self, board):
        pos = pygame.mouse.get_pos()

        #if user clicks on button, toggle free mode on/off
        if pygame.mouse.get_pressed()[0] and self.get_rect().collidepoint(pos) and self.get_clicked() == False:

            self.set_clicked(True)

            if board.get_free_mode() == True:
                board.set_free_mode(False) #if free mode was on, turn it off
                self.set_image(pygame.image.load("assets/button_images/red-free-mode-button.png"))
                board.reset_to_latest_position() #makes position go back to latest position in game
                print("Free mode turned off") #for testing

            else:
                board.set_free_mode(True) #if free mode was off, turn it on
                self.set_image(pygame.image.load("assets/button_images/green-free-mode-button.png"))
                print("Free mode turned on") #for testing

        #resetting button
        if pygame.mouse.get_pressed()[0] == False:
            self.set_clicked(False)