#imports
import pygame

class NotationPanel:
    def __init__(self, x, y, width, height, font):
        self.__x = x
        self.__y = y
        self.__width = width
        self.__height = height
        self.__font = font
        self.__rect = pygame.Rect(self.__x, self.__y, self.__width, self.__height)
        self.__font = font
        self.__scroll_offset = 0

    #getters
    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def get_width(self):
        return self.__width

    def get_height(self):
        return self.__height

    def get_font(self):
        return self.__font

    def get_rect(self):
        return self.__rect

    def get_scroll_offset(self):
        return self.__scroll_offset
        
    def get_scroll_speed(self):
        return self.__scroll_speed

    #setters
    def set_x(self, p_x):
        self.__x = p_x

    def set_y(self, p_y):
        self.__y = p_y

    def set_width(self, p_width):
        self.__width = p_width

    def set_height(self, p_height):
        self.__height = p_height

    def set_font(self, p_font):
        self.__font = p_font

    def set_rect(self, p_rect):
        self.__rect = p_rect

    def set_scroll_offset(self, p_scroll_offset):
        self.__scroll_offset = p_scroll_offset
        
    def set_scroll_speed(self, p_scroll_speed):
        self.__scroll_speed = p_scroll_speed


    #draw the notation panel
    def draw(self, screen, moves):

        #drawing background, border and title
        pygame.draw.rect(screen, (201, 218, 248), self.__rect)
        pygame.draw.rect(screen, (0, 0, 0), self.__rect, 2)
        screen.blit(self.__font.render("notation", True, (0, 0, 0)), (self.__rect.x, self.__rect.y - self.__font.get_height() - 5))

        #get the lines, the height of each line and the total height of all the lines
        lines = self.format_notation(moves)
        line_height = self.__font.get_height() + 5
        lines_height = len(lines) * line_height

        #prevent user scrolling above or below notation
        max_scroll_distance = lines_height - (self.__rect.h - 20) #distance user can scoll before reaching end
        if self.__scroll_offset < 0 or lines_height < 672: #scroll offset is 0 if notation doesn't fill panel or theres no notation above panel
            self.__scroll_offset = 0
        elif self.__scroll_offset > max_scroll_distance: #if there's no notation below panel
            self.__scroll_offset = max_scroll_distance

        #set clipping region to prevent text from drawing outside panel
        screen.set_clip(self.__rect)

        #draw all text lines but only ones within the clipping region are drawn
        y_position = self.__rect.y + 10 - self.__scroll_offset #top of panel, moved up by how much user had scrolled
        for line in lines:
            text_surface = self.__font.render(line, True, (0, 0, 0))
            screen.blit(text_surface, (self.__rect.x + 10, y_position))
            y_position += line_height #each line has a different y

        #remove clipping so other things on the GUI draw normally
        screen.set_clip(None)


    def update_scroll(self, keys):

        move_amount = 15 #pixels user scrolls for each time an up/down key is pressed

        if keys[pygame.K_UP]: #if up arrow is pressed
            self.__scroll_offset = self.__scroll_offset - move_amount #decrease scroll offset
        elif keys[pygame.K_DOWN]: #if down arrow is pressed
            self.__scroll_offset = self.__scroll_offset + move_amount #increase scroll offset


    #formats the notation to have the move number in front, stored in 1D list
    def format_notation(self, moves):
        lines = []
        for i in range(0, len(moves)):
            full_move = ""
            full_move += (str(i + 1) + ". ") #move number
            full_move += moves[i][0] + " " + moves[i][1] #actual moves
            lines.append(full_move) #appends each full move onto a 1D list
        
        return lines
