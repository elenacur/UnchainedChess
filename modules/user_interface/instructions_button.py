import pygame
from modules.user_interface.button import Button

class InstructionsButton(Button):
    #constructor
    def __init__(self, x, y, width, height, colour, image):
        
        super().__init__(x, y, width, height, colour, image)

    
    def check_if_clicked(self):
        pos = pygame.mouse.get_pos()

        #if user clicks on button, save game
        if pygame.mouse.get_pressed()[0] and self.get_rect().collidepoint(pos) and self.get_clicked() == False:

            self.set_clicked(True)

            

            #load_instructions() or just put all the code in here? idk it doesnt make sense for it to be in board whereas savign game deos because oyu need the ntoation.

        #resetting button
        if pygame.mouse.get_pressed()[0] == False:
            self.set_clicked(False)