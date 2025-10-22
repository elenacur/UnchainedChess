
import pygame
from modules.user_interface.button import Button

class FreeModeButton(Button):

    #constructor
    def __init__(self, x, y, width, height, colour, image):
        super().__init__(x, y, width, height, colour, image)


    def check_if_clicked(self, board):
        pos = pygame.mouse.get_pos()

        #if user clicks on button, toggle free mode on/off
        if pygame.mouse.get_pressed()[0] and self.get_rect().collidepoint(pos) and self.get_clicked() == False:

            self.set_clicked(True)

            if board.get_free_mode() == True:
                board.set_free_mode(False) #if free mode was on, turn it off
                self.set_image(pygame.image.load("assets/button_images/red-free-mode-button.png"))
            else:
                board.set_free_mode(True) #if free mode was off, turn it on
                self.set_image(pygame.image.load("assets/button_images/green-free-mode-button.png"))

        #resetting button
        if pygame.mouse.get_pressed()[0] == False:
            self.set_clicked(False)