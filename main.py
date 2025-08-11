import pygame
from modules.board import Board
from modules.pieces.child_pieces import Pawn

pygame.init()

#window
SCREEN_WIDTH = 1360
SCREEN_HEIGHT = 765

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

board = Board()
pawn = Pawn("white")

run = True
while run == True: #game loop
  
  screen.fill((217, 210, 233))

  board.draw(screen)

  pawn.draw(screen)


  #event handler
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False

  pygame.display.update()  

pygame.quit()
