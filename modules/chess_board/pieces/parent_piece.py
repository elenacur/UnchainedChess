#imports
import pygame

class Piece():

    #constructor
    def __init__(self, name, board, colour, taken, row, column, size):
        self.__name = name
        self.__board = board
        self.__colour = colour
        self.__taken = taken
        self.__row = row
        self.__column = column
        self.__size = size
        self.__image = None
        self.__is_moving = False
        self.__original_pos = None
        self.__value = None
        self.__new_row = None
        self.__new_column = None
        #creating rect that's same size and position as given square and correct perspective
        self.__rect = pygame.Rect(self.__column * self.__size + 210, self.__row * self.__size + 70, 
                            self.__size, self.__size) 
        
    #getters
    def get_name(self):
        return self.__name
    
    def get_board(self):
        return self.__board

    def get_colour(self):
        return self.__colour

    def get_taken(self):
        return self.__taken

    def get_row(self):
        return self.__row

    def get_column(self):
        return self.__column
    
    def get_size(self):
        return self.__size

    def get_image(self):
        return self.__image 
    
    def get_is_moving(self):
        return self.__is_moving
    
    def get_original_pos(self):
        return self.__original_pos
    
    def get_value(self):
        return self.__value
    
    def get_new_row(self):
        return self.__new_row
    
    def get_new_column(self):
        return self.__new_column

    def get_rect(self):
        return self.__rect

    #setters
    def set_name(self, p_name):
        self.__name = p_name

    def set_colour(self, p_colour):
        self.__colour = p_colour

    def set_taken(self, p_taken):
        self.__taken = p_taken

    def set_row(self, p_row):
        self.__row = p_row

    def set_column(self, p_column):
        self.__column = p_column

    def set_size(self, p_size):
        self.__size = p_size

    def set_image(self, p_image):
        self.__image = p_image

    def set_is_moving(self, p_is_moving):
        self.__is_moving = p_is_moving

    def set_original_pos(self, p_original_pos):
        self.__is_moving = p_original_pos

    def set_value(self, p_value):
        self.__value = p_value

    def set_new_row(self, p_new_row):
        self.__new_row = p_new_row

    def set_new_column(self, p_new_column):
        self.__new_column = p_new_column

    def set_rect(self, p_rect):
        self.__rect = p_rect


    #other methods
    def get_legal_moves(self):
        legal_moves = None
        return legal_moves
    
    def get_legal_rook_moves(self, colour, pieces):
        legal_moves = []    

        #columns/rows on each of its sides + 1
        num_columns_left = self.get_column() + 1
        num_columns_right = 8 - self.get_column()
        num_rows_up = self.get_row() + 1
        num_rows_down = 8 - self.get_row()

        #checking up
        i = 1
        no_blockages = True
        if num_rows_up != 1: #if at an edge
            while no_blockages:
                if pieces[self.get_row() - i][self.get_column()] != None:
                    no_blockages = False
                    if pieces[self.get_row() - i][self.get_column()].get_colour() != colour:
                        legal_moves.append([self.get_row() - i, self.get_column()]) #add move to list
                else:
                    legal_moves.append([self.get_row() - i, self.get_column()]) #add move to list
                i += 1 #to loop through row
                if i == num_rows_up:
                    no_blockages = False
        
        #checking down
        i = 1
        no_blockages = True
        if num_rows_down != 1: #if at an edge
            while no_blockages:
                if pieces[self.get_row() + i][self.get_column()] != None:
                    no_blockages = False
                    if pieces[self.get_row() + i][self.get_column()].get_colour() != colour:
                        legal_moves.append([self.get_row() + i, self.get_column()]) #add move to list
                else:
                    legal_moves.append([self.get_row() + i, self.get_column()]) #add move to list
                i += 1 #to loop through row
                if i == num_rows_down:
                    no_blockages = False
        
        #checking left
        i = 1
        no_blockages = True
        if num_columns_left != 1: #if at an edge
            while no_blockages:
                if pieces[self.get_row()][self.get_column() - i] != None:
                    no_blockages = False
                    if pieces[self.get_row()][self.get_column() - i].get_colour() != colour:
                        legal_moves.append([self.get_row(), self.get_column() - i]) #add move to list
                else:
                    legal_moves.append([self.get_row(), self.get_column() - i]) #add move to list
                i += 1 #to loop through column
                if i == num_columns_left:
                    no_blockages = False
        
        #checking right
        i = 1
        no_blockages = True
        if num_columns_right != 1: #if at an edge
            while no_blockages:
                if pieces[self.get_row()][self.get_column() + i] != None:
                    no_blockages = False
                    if pieces[self.get_row()][self.get_column() + i].get_colour() != colour:
                        legal_moves.append([self.get_row(), self.get_column() + i]) #add move to list
                else:
                    legal_moves.append([self.get_row(), self.get_column() + i]) #add move to list
                i += 1 #to loop through column
                if i == num_columns_right:
                    no_blockages = False

        return legal_moves
    
    def get_legal_bishop_moves(self, colour, pieces):
        legal_moves = []

        #columns/rows on each of its sides + 1
        num_columns_left = self.get_column() + 1
        num_columns_right = 8 - self.get_column()
        num_rows_up = self.get_row() + 1
        num_rows_down = 8 - self.get_row()

        #checking top left
        i = 1
        no_blockages = True
        if num_rows_up != 1 and num_columns_left != 1: #if at an edge
            while no_blockages:
                if pieces[self.get_row() - i][self.get_column() - i] != None:
                    no_blockages = False
                    if pieces[self.get_row() - i][self.get_column() - i].get_colour() != colour:
                        legal_moves.append([self.get_row() - i, self.get_column() - i]) #add move to list
                else:
                    legal_moves.append([self.get_row() - i, self.get_column() - i]) #add move to list
                i += 1 #to loop through diagonal
                if i == num_rows_up or i == num_columns_left:
                    no_blockages = False
        
        #checking bottom left
        i = 1
        no_blockages = True
        if num_rows_down != 1 and num_columns_left != 1: #if at an edge
            while no_blockages:
                if pieces[self.get_row() + i][self.get_column() - i] != None:
                    no_blockages = False
                    if pieces[self.get_row() + i][self.get_column() - i].get_colour() != colour:
                        legal_moves.append([self.get_row() + i, self.get_column() - i]) #add move to list
                else:
                    legal_moves.append([self.get_row() + i, self.get_column() - i]) #add move to list
                i += 1 #to loop through diagonal
                if i == num_rows_down or i == num_columns_left:
                    no_blockages = False
        
        #checking top right
        i = 1
        no_blockages = True
        if num_rows_up != 1 and num_columns_right != 1: #if at an edge
            while no_blockages:
                if pieces[self.get_row() - i][self.get_column() + i] != None:
                    no_blockages = False
                    if pieces[self.get_row() - i][self.get_column() + i].get_colour() != colour:
                        legal_moves.append([self.get_row() - i, self.get_column() + i]) #add move to list
                else:
                    legal_moves.append([self.get_row() - i, self.get_column() + i]) #add move to list
                i += 1 #to loop through diagonal
                if i == num_rows_up or i == num_columns_right:
                    no_blockages = False
        
        #checking right
        i = 1
        no_blockages = True
        if num_rows_down != 1 and num_columns_right != 1: #if at an edge
            while no_blockages:
                if pieces[self.get_row() + i][self.get_column() + i] != None: 
                    no_blockages = False
                    if pieces[self.get_row() + i][self.get_column() + i].get_colour() != colour:
                        legal_moves.append([self.get_row() + i, self.get_column() + i]) #add move to list
                else:
                    legal_moves.append([self.get_row() + i, self.get_column() + i]) #add move to list
                i += 1 #to loop through diagonal
                if i == num_rows_down or i == num_columns_right:
                    no_blockages = False

        return legal_moves
    
    def remove(self):
        None

    def draw_piece(self, screen):
        #create a rect that is the image's size and position, put this rect at the centre of self.__rect
        screen.blit(self.__image, self.__image.get_rect(center=self.__rect.center)) #blit image and rect
        #pygame.draw.rect(screen, (255, 0, 0), self.__rect, 2) #temporary outline for testing

    #allows user to move the piece's rect
    def move(self, event, pos, pieces):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.__rect.collidepoint(pos): #if user left clicks on piece's rect
                self.__is_moving = True
                self.__original_pos = self.__rect.center 
    
        if event.type == pygame.MOUSEMOTION and self.__is_moving == True: #if user moves mouse after clicking on piece rect
            self.__rect.center = pos #update position of rect's centre to position of mouse

        if event.type == pygame.MOUSEBUTTONUP and event.button == 1 and self.__is_moving == True: #if user stops holding down left click
            self.__is_moving = False #stop moving rect

            #moving piece to centre of square the user drops the rect on
            not_on_a_square = 0
            for list in self.__board.get_board():
                for square in list:
                    if square.get_rect().collidepoint(pos):
                        self.__rect.center = square.get_rect().center #locking piece's rect to centre of square

                        #returning new row and column of piece
                        self.__new_row = square.get_row()
                        self.__new_column = square.get_column()

                        #validating move
                        legal = False
                        legal_moves = self.get_legal_moves(self.__colour, pieces)
                        for i in legal_moves: #if the move is in the list of legal moves for that piece
                            if i == [self.__new_row, self.__new_column]:
                                legal = True
                        if legal:
                            return (self.__new_row, self.__new_column) #if legal, let board move piece there
                        else:
                            self.__rect.center = self.__original_pos #if illegal, return piece to position before user moved it
                    else:
                        not_on_a_square += 1
            if not_on_a_square == 64: #if user lets go of piece outside of chess board
                self.__rect.center = self.__original_pos #return piece to position before user moved it




