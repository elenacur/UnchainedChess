#imports
import pygame
from modules.chess_game.pieces.parent_piece import Piece
from modules.user_interface.pop_up_box import PopUpBox

#using inheritance of Piece

#pawn
class Pawn(Piece):

    #constructor
    def __init__(self, board, colour, taken, row, column, size):
        super().__init__("pawn", board, colour, taken, row, column, size) #initialising parent class
        self.__en_passant = False #for en passant
        self.__can_promote = False #for promoting
        self.set_value(1)

        if self.get_colour() == "white": #assigning different images based on colour
            self.set_image(pygame.image.load("assets/chess_pieces_images/white-pawn.png"))
        else:
            self.set_image(pygame.image.load("assets/chess_pieces_images/black-pawn.png"))

        self.set_image(pygame.transform.scale_by(self.get_image(), (self.get_size()/105))) #scaling the image

    #getters
    def get_en_passant(self):
        return self.__en_passant

    def get_can_promote(self):
        return self.__can_promote
    
    #setters
    def set_en_passant(self, p_en_passant):
        self.__en_passant = p_en_passant

    def set_can_promote(self, p_can_promote):
        self.__can_promote = p_can_promote

    #other methods
    def get_legal_moves(self, colour, pieces):
        legal_moves = []

        #pawns can only move in one direction depending on their colour
        if colour == "white":
            colour_factor = -1
        else:
            colour_factor = 1
        
        #moving 1 square forward
        if pieces[self.get_row() + colour_factor][self.get_column()] == None:
            legal_moves.append([self.get_row() + colour_factor, self.get_column()])
            #moving 2 squares forward
            if pieces[self.get_row() + (colour_factor * 2)][self.get_column()] == None and self.get_has_moved() == False:
                legal_moves.append([self.get_row() + (colour_factor * 2), self.get_column()])

        #taking diagonally
        for i in range(-1, 2, 2): #-1 for left, 1 for right
            if 0 <= (self.get_row() + colour_factor) <= 7 and 0 <= (self.get_column() + i) <= 7:
                if pieces[self.get_row() + colour_factor][self.get_column() + i] != None:
                    if pieces[self.get_row() + colour_factor][self.get_column() + i].get_colour() != colour:
                        legal_moves.append([self.get_row() + colour_factor, self.get_column() + i])
        return legal_moves

    #opens a pop up box that asks what the user wants to promote their pawn to
    def promote(self):

        screen = pygame.display.get_surface()
        font = pygame.font.SysFont("Arial", 24)
        pop_up_box = PopUpBox(screen, "Promote to:", font)
        pop_up_box.open()

        promoting = True
        error_message = ""

        while promoting:
            for event in pygame.event.get():
                pop_up_box.register_keyboard_inputs(event)

                #let the user still quit while the pop up box is open
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

                #handle enter key after pop up box closes itself
                if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:

                    #validating user input
                    if pop_up_box.get_active() == False:
                        choice = pop_up_box.get_result()
                        if choice != None:
                            choice = choice.strip().lower()
                            if choice in ["queen", "rook", "bishop", "knight"]: #did user enter a valid letter?
                                promoting = False
                                return choice
                            else: 
                                error_message = "Invalid input. Please try again."
                                pop_up_box.open() #if invalid input, we re-open pop up box with error message too
                
                #continue drawing board and pop up box on to screen while we wait for the user to give valid input
                screen.fill((217, 210, 233))
                self.get_board().draw_whole_board(screen)
                self.get_board().draw_all_pieces(screen)
                pop_up_box.draw()   
                

            #drawing error message if necessary
            if error_message != "":
                error_surface = font.render(error_message, True, (200, 0, 0))
                pop_up_rect = pop_up_box.get_rect()
                screen.blit(error_surface, (pop_up_rect.x + 10, pop_up_rect.bottom + 10))

            pygame.display.update()
            
        return None