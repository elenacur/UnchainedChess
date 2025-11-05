import pygame
from modules.user_interface.button import Button

class SaveGameButton(Button):
    #constructor
    def __init__(self, x, y, width, height, colour, image):
        
        super().__init__(x, y, width, height, colour, image)

    
    def check_if_clicked(self, board):
        pos = pygame.mouse.get_pos()

        #if user clicks on button, save game
        if pygame.mouse.get_pressed()[0] and self.get_rect().collidepoint(pos) and self.get_clicked() == False:

            self.set_clicked(True)

            if board.get_free_mode() == False:
                board.save_game()
            
            else:
                print("Cannot save game when in free mode.") #for testing

        #resetting button
        if pygame.mouse.get_pressed()[0] == False:
            self.set_clicked(False)