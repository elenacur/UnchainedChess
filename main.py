#imports
import pygame
from modules.chess_board.board import Board
from modules.chess_board.pieces.child_pieces import Pawn

pygame.init()

#window and sizing
SCREEN_WIDTH = 1360
SCREEN_HEIGHT = 765

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

#instantiating objects
board = Board("", True, 0, False)
pawn = Pawn("white", False, 1, 1, 50)

run = True
while run == True: #game loop
  
  screen.fill((217, 210, 233)) #background colour
  pos = pygame.mouse.get_pos() #getting position of the mouse

  board.draw_whole_board(screen)
  pawn.draw(screen)

  #event handler
  for event in pygame.event.get():

    pawn.move(event, pos) #move piece when user drags and drops it

    if event.type == pygame.QUIT: #close window when user exits
      run = False

  pygame.display.update()  

pygame.quit()
