#imports
import pygame
from modules.user_interface.button import Button

class BackForwardButtons(Button):

    #constructor
    def __init__(self, x, y, width, height, image, name):
        super().__init__(x, y, width, height, image)

        self.__name = name #so I can distinguish back buttons and forward buttons

    #getters
    def get_name(self):
        return self.__name
    
    #setters
    def set_name(self, p_name):
        self.__name = p_name

    #checks if user clicks on button and carries out appropriate response
    def check_if_clicked(self, board):
        pos = pygame.mouse.get_pos()

        #if user clicks on button, go back/forward
        if pygame.mouse.get_pressed()[0] and self.get_rect().collidepoint(pos) and self.get_clicked() == False:

            self.set_clicked(True)

            if board.get_free_mode() == False:
                if self.__name == "back_button":
                    board.go_back_one_move()
    
                if self.__name == "forward_button":
                    board.go_forward_one_move()
            
            else:
                print("Cannot go back or forward when in free mode.") #for testing

        #resetting button
        if pygame.mouse.get_pressed()[0] == False:
            self.set_clicked(False)


    