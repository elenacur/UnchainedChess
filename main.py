#imports
import pygame
from modules.chess_board.board import Board
from modules.user_interface.free_mode_button import FreeModeButton
from modules.user_interface.back_forward_buttons import BackForwardButtons

pygame.init()

#window and sizing and text
SCREEN_WIDTH = 1344
SCREEN_HEIGHT = 756

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

default_text = pygame.font.SysFont("Arial", 30)

#instantiating objects
board = Board(84, "", True, 0, False)
board.reset_board()
free_mode_button = FreeModeButton(1100, 350, 100, 100, None, pygame.image.load("assets/button_images/red-free-mode-button.png"))
back_button = BackForwardButtons(1100, 500, 80, 80, None, pygame.image.load("assets/button_images/back-button.png"), "back_button")
forward_button = BackForwardButtons(1200, 500, 80, 80, None, pygame.image.load("assets/button_images/forward-button.png"), "forward_button")

run = True
while run == True: #game loop
  
  screen.fill((217, 210, 233)) #background colour
  pos = pygame.mouse.get_pos() #getting position of the mouse

  #drawing user_interface objects onto the screen
  free_mode_button.draw(screen)
  back_button.draw(screen)
  forward_button.draw(screen)

  #checking if user_interface objects are clicked
  free_mode_button.check_if_clicked(board)
  back_button.check_if_clicked(board)
  forward_button.check_if_clicked(board)

  #drawing chess_board objects onto the screen
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

