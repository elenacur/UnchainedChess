import pygame

class PopUpBox:
    def __init__(self, screen, prompt_text, font, width=300, height=120):
        self.__screen = screen
        self.__prompt_text = prompt_text
        self.__font = font
        self.__width = width
        self.__height = height
        self.__active = False
        self.__user_text = ""
        self.__result = None
        self.__rect = None
    
    #getters
    def get_screen(self):
        return self.__screen

    def get_prompt_text(self):
        return self.__prompt_text

    def get_font(self):
        return self.__font

    def get_width(self):
        return self.__width

    def get_height(self):
        return self.__height

    def get_active(self):
        return self.__active

    def get_user_text(self):
        return self.__user_text

    def get_result(self):
        return self.__result

    def get_rect(self):
        return self.__rect

    #setters
    def set_screen(self, p_screen):
        self.__screen = p_screen

    def set_prompt_text(self, p_prompt_text):
        self.__prompt_text = p_prompt_text

    def set_font(self, p_font):
        self.__font = p_font

    def set_width(self, p_width):
        self.__width = p_width

    def set_height(self, p_height):
        self.__height = p_height

    def set_active(self, p_active):
        self.__active = p_active

    def set_user_text(self, p_user_text):
        self.__user_text = p_user_text

    def set_result(self, p_result):
        self.__result = p_result

    def set_rect(self, p_rect):
        self.__rect = p_rect


    #opens a pop up box
    def open(self):

        self.__active = True
        self.__user_text = ""
        self.__result = None

        #make a pop up box at the centre of the screen
        self.__rect = pygame.Rect((self.__screen.get_width() - self.__width) // 2, (self.__screen.get_height() - self.__height) // 2, self.__width, self.__height)


    #register what keys the user is pressing and change the text accordingly
    def register_keyboard_inputs(self, event):
        if self.__active == False:
            return None

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_RETURN: #if user presses enter, we need to close the pop up box
                self.__result = self.__user_text.strip()
                self.__active = False

            elif event.key == pygame.K_BACKSPACE: #if user presses the backspace, we need to remove the last letter
                self.__user_text = self.__user_text[:-1]

            else: #if user presses another key, record that key
                self.__user_text += event.unicode


    def draw(self):

        #only draw stuff if the pop up box is active
        if self.__active == False:
            return None

        #dim background
        overlay = pygame.Surface((self.__screen.get_width(), self.__screen.get_height()))
        overlay.set_alpha(160)
        overlay.fill((50, 50, 50))
        self.__screen.blit(overlay, (0, 0))

        #draw a pop up box onto the screen
        pygame.draw.rect(self.__screen, (240, 240, 240), self.__rect)
        pygame.draw.rect(self.__screen, (0, 0, 0), self.__rect, 2)

        #draw the test prompt
        prompt_surface = self.__font.render(self.__prompt_text, True, (0, 0, 0))
        self.__screen.blit(prompt_surface, (self.__rect.x + 10, self.__rect.y + 15))

        #draw the user's inputs
        text_surface = self.__font.render(self.__user_text, True, (20, 20, 20))
        self.__screen.blit(text_surface, (self.__rect.x + 10, self.__rect.y + 60))
