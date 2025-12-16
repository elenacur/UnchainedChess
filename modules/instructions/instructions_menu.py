import pygame
from modules.user_interface.button import Button

class InstructionsMenu(Button):
    #constructor
    def __init__(self, x, y, width, height, image):
        
        super().__init__(x, y, width, height, image)
    
    #pressing ESC key will close the instructions menu
    def check_for_escape(self):

        keys = pygame.key.get_pressed() #get what keys have been pressed
 
        #if escape key is pressed, return True
        if keys[pygame.K_ESCAPE]:
            return True

        return False
