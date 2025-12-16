import pygame
from modules.user_interface.button import Button
from modules.save_game.save_game import save_game

class SaveGameButton(Button):
    #constructor
    def __init__(self, x, y, width, height, image):
        
        super().__init__(x, y, width, height, image)

    
    def check_if_clicked(self, board):
        pos = pygame.mouse.get_pos()

        #if user clicks on button, save game
        if pygame.mouse.get_pressed()[0] and self.get_rect().collidepoint(pos) and self.get_clicked() == False:

            self.set_clicked(True)

            if board.get_free_mode() == False:
                save_game(board.get_notation().get_notation_text())
            
            else:
                print("Cannot save game when in free mode.") #for testing

        #resetting button
        if pygame.mouse.get_pressed()[0] == False:
            self.set_clicked(False)