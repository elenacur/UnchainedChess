#imports
import pygame
from modules.user_interface.button import Button


class InstructionsButton(Button):
    #constructor
    def __init__(self, x, y, width, height, image):
        
        super().__init__(x, y, width, height, image)

    #checks if user clicks on button and carries out appropriate response
    def check_if_clicked(self):
        pos = pygame.mouse.get_pos()

        #if user clicks on button, draw the instruction menu
        if pygame.mouse.get_pressed()[0] and self.get_rect().collidepoint(pos) and self.get_clicked() == False:

            self.set_clicked(True)

            return True


        #resetting button
        if pygame.mouse.get_pressed()[0] == False:
            self.set_clicked(False)
        
        return False
