#imports
import pygame
from modules.chess_board.board import Board
from modules.chess_board.pieces.child_pieces import Pawn

pygame.init()

#window and sizing and text
SCREEN_WIDTH = 1344
SCREEN_HEIGHT = 756

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

default_text = pygame.font.SysFont("Arial", 30)

#instantiating board
board = Board(84, "", True, 0, False)
board.reset_board()

run = True
while run == True: #game loop
  
  screen.fill((217, 210, 233)) #background colour
  pos = pygame.mouse.get_pos() #getting position of the mouse

  #drawing objects onto the screen
  board.draw_whole_board(screen)
  board.draw_all_pieces(screen)
  board.draw_points(screen, default_text)

  #event handler
  for event in pygame.event.get():

    board.move_pieces(event, pos) #allows user to move pieces

    if event.type == pygame.QUIT: #close window when user exits
      run = False

  pygame.display.update()  

pygame.quit()

#board.print_pieces() #prints the current board position in terminal

