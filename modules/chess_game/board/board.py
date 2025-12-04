#imports
import pygame
from modules.chess_game.board.square import Square
from modules.chess_game.pieces.king import King
from modules.chess_game.pieces.queen import Queen
from modules.chess_game.pieces.rook import Rook
from modules.chess_game.pieces.bishop import Bishop
from modules.chess_game.pieces.knight import Knight
from modules.chess_game.pieces.pawn import Pawn
from modules.notation.notation import Notation
from modules.notation.stack import Stack
from modules.chess_game.pieces.parent_piece import clone_board

class Board():

    #constructor
    def __init__(self, square_size, fen, whites_turn, num_of_moves, game_over):
        self.__board = [["", "", "", "", "", "", "", ""], ["", "", "", "", "", "", "", ""], 
                        ["", "", "", "", "", "", "", ""], ["", "", "", "", "", "", "", ""], 
                        ["", "", "", "", "", "", "", ""], ["", "", "", "", "", "", "", ""], 
                        ["", "", "", "", "", "", "", ""], ["", "", "", "", "", "", "", ""]] #2D array of Square objects
        self.__pieces = [[None, None, None, None, None, None, None, None], 
                         [None, None, None, None, None, None, None, None], 
                         [None, None, None, None, None, None, None, None], 
                         [None, None, None, None, None, None, None, None], 
                         [None, None, None, None, None, None, None, None], 
                         [None, None, None, None, None, None, None, None], 
                         [None, None, None, None, None, None, None, None], 
                         [None, None, None, None, None, None, None, None]] #2D array of Piece objects
        self.__square_size = square_size
        self.__fen = fen
        self.__whites_turn = whites_turn
        self.__num_of_moves = num_of_moves
        self.__game_over = game_over
        self.__white_points = 0
        self.__black_points = 0
        self.__white_king_pos = None
        self.__black_king_pos = None
        self.__free_mode = False
        self.__notation = Notation()
        self.__undo_stack = Stack()   # stores past positions + current one
        self.__redo_stack = Stack()   # stores undone positions
        self.__current_position_index = 0

        #putting Square objects in the board array, alternating black and white
        white = True
        for i in range(0, 8):
            for j in range(0, 8):
                if white:
                    colour = "white"
                else:
                    colour = (144, 149, 128)
                if j != 7: #start of new row is same colour as end of previous row so colour should not change
                    white = not white
                self.__board[i][j] = Square(i, j, self.__square_size, colour)

    #getters
    def get_board(self):
        return self.__board
    
    def get_pieces(self, row, column):
        return self.__pieces[row][column]
    
    def get_square_size(self):
        return self.__square_size
    
    def get_fen(self):
        return self.__fen
    
    def get_whites_turn(self):
        return self.__whites_turn
    
    def get_num_of_moves(self):
        return self.__num_of_moves
    
    def get_game_over(self):
        return self.__game_over
    
    def get_white_points(self):
        return self.__white_points
    
    def get_black_points(self):
        return self.__black_points
    
    def get_white_king_pos(self):
        return self.__white_king_pos
    
    def get_black_king_pos(self):
        return self.__black_king_pos
    
    def get_free_mode(self):
        return self.__free_mode
    
    def get_notation(self):
        return self.__notation

    def get_undo_stack(self):
        return self.__undo_stack

    def get_redo_stack(self):
        return self.__redo_stack

    def get_current_position_index(self):
        return self.__current_position_index

    
    #setters
    def set_board(self, p_board):
        self.__board = p_board

    def set_pieces(self, new_piece, row, column):
        self.__pieces[row][column] = new_piece

    def set_square_size(self, p_square_size):
        self.__square_size = p_square_size
    
    def set_fen(self, p_fen):
        self.__fen = p_fen

    def set_whites_turn(self, p_whites_turn):
        self.__whites_turn = p_whites_turn
    
    def set_num_of_moves(self, p_num_of_moves):
        self.__num_of_moves = p_num_of_moves
    
    def set_game_over(self, p_game_over):
        self.__game_over = p_game_over

    def set_white_points(self, p_white_points):
        self.__white_points = p_white_points

    def set_black_points(self, p_black_points):
        self.__black_points = p_black_points

    def set_white_king_pos(self, p_white_king_pos):
        self.__white_king_pos = p_white_king_pos

    def set_black_king_pos(self, p_black_king_pos):
        self.__black_king_pos = p_black_king_pos

    def set_free_mode(self, p_free_mode):
        self.__free_mode = p_free_mode

    def set_notation(self, p_notation):
        self.__notation = p_notation

    def set_undo_stack(self, p_undo_stack):
        self.__undo_stack = p_undo_stack

    def set_redo_stack(self, p_redo_stack):
        self.__redo_stack = p_redo_stack

    def set_current_position_index(self, p_index):
        self.__current_position_index = p_index

    #other methods
    def reset_board(self): #filling pieces array with Piece objects in order of chess starting position
        
        #pawns
        for i in range(0, 8):
            self.__pieces[1][i] = Pawn(self, "black", False, 1, i, 84)

        for i in range(0, 8):
            self.__pieces[6][i] = Pawn(self, "white", False, 6, i, 84)

        #rooks
        self.__pieces[0][0] = Rook(self, "black", False, 0, 0, 84)
        self.__pieces[0][7] = Rook(self, "black", False, 0, 7, 84)
        self.__pieces[7][0] = Rook(self, "white", False, 7, 0, 84)
        self.__pieces[7][7] = Rook(self, "white", False, 7, 7, 84)

        #knights
        self.__pieces[0][1] = Knight(self, "black", False, 0, 1, 84)
        self.__pieces[0][6] = Knight(self, "black", False, 0, 6, 84)
        self.__pieces[7][1] = Knight(self, "white", False, 7, 1, 84)
        self.__pieces[7][6] = Knight(self, "white", False, 7, 6, 84)

        #bishops
        self.__pieces[0][2] = Bishop(self, "black", False, 0, 2, 84)
        self.__pieces[0][5] = Bishop(self, "black", False, 0, 5, 84)
        self.__pieces[7][2] = Bishop(self, "white", False, 7, 2, 84)
        self.__pieces[7][5] = Bishop(self, "white", False, 7, 5, 84)

        #queens
        self.__pieces[0][3] = Queen(self, "black", False, 0, 3, 84)
        self.__pieces[7][3] = Queen(self, "white", False, 7, 3, 84)

        #kings
        self.__pieces[0][4] = King(self, "black", False, 0, 4, 84)
        self.__black_king_pos = [0, 4]
        self.__pieces[7][4] = King(self, "white", False, 7, 4, 84)
        self.__white_king_pos = [7, 4]

        self.reset_past_positions() #resets past positions

    
    def draw_whole_board(self, screen): #draws every object in the board array i.e. the whole board

        columns = ["a", "b", "c", "d", "e", "f", "g", "h"]
        rows = ["8", "7", "6", "5", "4", "3", "2", "1"]

        for i in range(0, 8):
            for j in range(0, 8):

                #drawing the board
                square = self.__board[i][j]
                square.draw_square(screen)

                #drawing the coordinates
                #letter coordinates
                if i == 7: #on bottom row
                    label = pygame.font.SysFont("Arial", 20).render(columns[j], True, (0, 0, 0))
                    screen.blit(label, (square.get_x() + 1, square.get_y() + square.get_size() - 25))
                
                #number coordinates
                if j == 0: #on left column
                    label = pygame.font.SysFont("Arial", 20).render(rows[i], True, (0, 0, 0))
                    screen.blit(label, (square.get_x() + 1, square.get_y() + 1))
    

    def draw_all_pieces(self, screen): #draws every object in the piece array
        for i in self.__pieces:
            for j in i:
                if j != None:
                    j.draw_piece(screen)
    
    def move_pieces(self, event, pos): #allows user to move pieces
        for list in self.__pieces:
            for piece in list:
                if piece != None:
                    returned_values, castling = piece.move(event, pos, self.__pieces, self.__whites_turn, self.__free_mode)
                    
                    #updating piece array and piece attributes
                    if returned_values != None:
                        new_row, new_column = returned_values

                        old_column = piece.get_column() #for recording notation

                        #updating piece that was moved by user
                        captured_piece = self.__pieces[new_row][new_column]                        
                        self.set_pieces(None, piece.get_row(), piece.get_column())
                        piece.set_row(new_row)
                        piece.set_column(new_column)
                        self.set_pieces(piece, new_row, new_column)

                        if piece.get_has_moved() == False: #piece has now moved so need to update this attribute
                            piece.set_has_moved(True)
                        
                        #checking if a pawn has been promoted
                        choice = None
                        if piece.get_name() == "pawn":
                            if (piece.get_colour() == "white" and new_row == 0) or (piece.get_colour() == "black" and new_row == 7):
                                piece.set_can_promote(True)
                                choice = piece.promote()
                                self.promote_pawn(piece, choice)
                        
                        
                        if self.__free_mode == False:

                            self.update_points(captured_piece) #updates points

                            self.save_position() #store board after every move done when free mode isn't on

                            #remove future text notation user may be rewriting
                            current_moves = self.__notation.get_moves()
                            move_index = self.__current_position_index // 2
                            
                            if self.__current_position_index % 2 == 1: #if user is playing a black move
                                if move_index < len(current_moves):
                                    self.__notation.set_moves(current_moves[:move_index + 1]) #get rid of future move pairs

                                    if len(self.__notation.get_moves()) > 0:
                                        new_moves = self.__notation.get_moves()
                                        new_moves[-1][1] = "" #get rid of black move user wants to replace
                                        self.__notation.set_moves(new_moves) 

                            else: #if user playing a white move
                                self.__notation.set_moves(current_moves[:move_index]) #get rid of all future move pairs


                            #updating move notation
                            new_move = self.get_move_notation(piece, old_column, new_row, new_column, captured_piece, choice, castling)
                            self.__notation.record_move(new_move, self.__whites_turn)
                            print(self.__notation.get_notation_text()) #printing notation for testing

                            self.__current_position_index += 1 #updating move we are on

                            self.__whites_turn = not self.__whites_turn #other player's turn now

                        #updating rook if castling is occurring
                        if castling[0] != None:
                            self.castle(castling, new_column)

    def print_pieces(self): #prints the current board position in terminal
        for list in self.__pieces:
            for piece in list:
                if piece != None:
                    print(piece.get_name(), end = " ")
                else:
                    print("None", end = " ")
            print()
    
    def update_points(self, taken_piece): #updates points of each player i.e. total value of pieces they've taken
        if taken_piece != None:
            if taken_piece.get_colour() == "white":
                self.__black_points += taken_piece.get_value()
            else:
                self.__white_points += taken_piece.get_value()

    #displays players' points on the screen
    def draw_points(self, screen, text):
        white_points_str = str(self.__white_points)
        black_points_str = str(self.__black_points)
        screen.blit(text.render(white_points_str, True, "black"), (910, 685))
        screen.blit(text.render(black_points_str, True, "black"), (910, 95))
        
    def castle(self, castling, new_column):
        self.set_pieces(None, castling[1].get_row(), castling[1].get_column())

        if castling[0] == "king_side":
            new_rook_column = new_column - 1 #rook is on left of king
        elif castling[0] == "queen_side":
            new_rook_column = new_column + 1 #rook is on right of king

        castling[1].set_column(new_rook_column)
        castling[1].get_rect().center = self.__board[castling[1].get_row()][castling[1].get_column()].get_rect().center
        self.set_pieces(castling[1], castling[1].get_row(), new_rook_column)

        if castling[1].get_has_moved() == False:
            castling[1].set_has_moved(True)
    
    #replaces pawn with piece of user's choice
    def promote_pawn(self, pawn, choice):
        
        row = pawn.get_row()
        column = pawn.get_column()
        colour = pawn.get_colour()
        size = pawn.get_size()

        if choice == "queen":
            new_piece = Queen(self, colour, False, row, column, size)
        elif choice == "rook":
            new_piece = Rook(self, colour, False, row, column, size)
        elif choice == "bishop":
            new_piece = Bishop(self, colour, False, row, column, size)
        elif choice == "knight":
            new_piece = Knight(self, colour, False, row, column, size) 

        self.set_pieces(new_piece, row, column)

    #putting the move just played into notation form
    def get_move_notation(self, piece, old_column, new_row, new_column, captured_piece, promotion_choice, castling):

        #if castling, use unique castling notation
        if castling[0] != None:
            if castling[0] == "queen_side":
                move = "0-0-0"
            elif castling[0] == "king_side":
                move = "0-0"

        #if not castling, use normal notation
        else:
            #putting new square into chess notation format
            columns = ['a','b','c','d','e','f','g','h']
            rows = ['8','7','6','5','4','3','2','1']
            new_square = columns[new_column] + rows[new_row]

            #getting letter of piece being moved
            name_map = {"pawn": "", "knight": "N", "bishop": "B", "rook": "R", "queen": "Q", "king": "K"}
            move = name_map[piece.get_name()] 

            #adding an x if a piece is being taken
            if captured_piece != None:
                if piece.get_name() == "pawn": #pawns need their original column before an x
                    move += columns[old_column]
                move += "x"
                
            move += new_square

            #promotion notation
            if promotion_choice != None:
                move = move + "=" + name_map[promotion_choice]

        #check, checkmate, stalemate and final result notation
        #if piece moved was white
        if piece.get_colour() == "white":
            situation = piece.checkmated_or_stalemated("black", self.__pieces)
            if situation == "checkmate": #the piece checkmates the king, meaning white wins
                move += "# 1-0"
            elif situation == "stalemate": #the piece causes stalemate, meaning a draw
                move += "½–½"
            elif situation == "neither": 
                if piece.in_check("black", self.__pieces): #the piece puts king in check notation
                    move += "+"

        #if piece moved was black
        if piece.get_colour() == "black":
            situation = piece.checkmated_or_stalemated("white", self.__pieces)
            if situation == "checkmate": #the piece checkmates the king, meaning black wins
                move += "# 0-1"
            elif situation == "stalemate": #the piece causes stalemate, meaning a draw
                move += "½–½"
            elif situation == "neither":
                if piece.in_check("white", self.__pieces): #the piece puts king in check notation
                    move += "+"

        return move

    #resetting past positions
    def reset_past_positions(self):

        #clearing stacks/instantiating them
        self.__undo_stack = Stack()
        self.__redo_stack = Stack()

        self.__undo_stack.push(clone_board(self.__pieces)) #save starting position

        self.__current_position_index = 0 #updating move we are on

    #cloning the current board state and adding it to the undo stack
    def save_position(self):
        cloned_pieces = clone_board(self.__pieces) #clones baord

        #if a new move is made, clear the redo stack (can't redo after a new move)
        self.__redo_stack = Stack() #instantiates a new, empty object

        #add a copy of the new board position onto the undo stack
        self.__undo_stack.push(cloned_pieces)


    #position on board goes back one move of notation
    def go_back_one_move(self):
        if self.__undo_stack.size() > 1: #can't undo the starting position

            current_position = self.__undo_stack.pop() #pop current position from undo stack

            if current_position != None:
                self.__redo_stack.push(clone_board(current_position)) #put current position on redo stack
            
                new_position = self.__undo_stack.peek()

                if new_position != None:
                    self.__pieces = clone_board(new_position) #board position is new top of undo stack

                    #update whose move it is
                    if self.__whites_turn == True:
                        self.__whites_turn = False
                    else:
                        self.__whites_turn = True

                    #attaching board back to pieces
                    for row in self.__pieces:
                        for piece in row:
                            if piece != None:
                                piece.set_board(self)

                    self.__current_position_index -= 1 #updating move we are on

                    print("Moved back one position.") #for testing

        else:
            print("Already at the first position.") #for testing

    #position on board goes forward one move of notation
    def go_forward_one_move(self):

        if self.__redo_stack.is_empty() == False: #can't redo a move when no moves have been made

            new_position = self.__redo_stack.pop() #remove new position from redo stack

            if new_position != None:
                self.__undo_stack.push(clone_board(new_position)) #put new position on undo stack
            
                new_position = self.__undo_stack.peek()

                if new_position != None:
                    self.__pieces = clone_board(new_position) #set new position to be one on top of undo

                    #update whose move it is
                    if self.__whites_turn == True:
                        self.__whites_turn = False
                    else:
                        self.__whites_turn = True

                    #attaching board back to pieces
                    for row in self.__pieces:
                        for piece in row:
                            if piece != None:
                                piece.set_board(self)
                    
                    self.__current_position_index += 1 #updating move we are on

                    print("Move forward one position.") #for testing

        else:
            print("Already at the latest position.") #for testing

    #position on board goes to most recent non-free mode one when user exits free mode
    def reset_to_latest_position(self):
        if self.__undo_stack.size() > 0: #validation

            latest_position = self.__undo_stack.peek() #checking undo stack for what latest position is

            if latest_position != None:
                self.__pieces = clone_board(latest_position) #setting board to be latest position

                #attaching board back to pieces
                for row in self.__pieces:
                    for piece in row:
                        if piece != None:
                            piece.set_board(self)

                print("Returned to latest position.") #for testing

    
               
    

