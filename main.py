#imports
import pygame
from modules.chess_board.board import Board
from modules.chess_board.pieces.child_pieces import Pawn

pygame.init()

#window and sizing
SCREEN_WIDTH = 1344
SCREEN_HEIGHT = 756

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

#instantiating objects
board = Board(84, "", True, 0, False)
pawn1 = Pawn("white", False, 1, 1, 84)
pawn2 = Pawn("black", False, 1, 2, 84)

run = True
while run == True: #game loop
  
  screen.fill((217, 210, 233)) #background colour
  pos = pygame.mouse.get_pos() #getting position of the mouse

  #drawing objects onto the screen
  board.draw_whole_board(screen)
  pawn1.draw(screen)
  pawn2.draw(screen)

  #event handler
  for event in pygame.event.get():

    pawn1.move(event, pos) #move piece when user drags and drops it
    pawn2.move(event, pos)

    if event.type == pygame.QUIT: #close window when user exits
      run = False

  pygame.display.update()  

pygame.quit()
