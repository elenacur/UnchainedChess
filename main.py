#imports
import pygame
from modules.chess_board.board import Board
from modules.user_interface.free_mode_button import FreeModeButton
from modules.user_interface.back_forward_buttons import BackForwardButtons
from modules.user_interface.notation_panel import NotationPanel
from modules.user_interface.save_game_button import SaveGameButton
from modules.user_interface.instructions_button import InstructionsButton

pygame.init()

#window and sizing and text
SCREEN_WIDTH = 1344
SCREEN_HEIGHT = 756

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

default_text = pygame.font.SysFont("Arial", 30)

#instantiating objects
board = Board(84, "", True, 0, False)
board.reset_board()
free_mode_button = FreeModeButton(65, 450, 80, 80, None, pygame.image.load("assets/button_images/red-free-mode-button.png"))
back_button = BackForwardButtons(20, 600, 80, 80, None, pygame.image.load("assets/button_images/back-button.png"), "back_button")
forward_button = BackForwardButtons(110, 600, 80, 80, None, pygame.image.load("assets/button_images/forward-button.png"), "forward_button")
notation_panel = NotationPanel(996, 70, 235, 672, default_text)
save_game_button = SaveGameButton(65, 300, 80, 80, None, pygame.image.load("assets/button_images/save-game-button.png"))
instructions_button = InstructionsButton(65, 150, 80, 80, None, pygame.image.load("assets/button_images/instructions-button.png"))


run = True
while run == True: #game loop
  
  screen.fill((217, 210, 233)) #background colour
  pos = pygame.mouse.get_pos() #getting position of the mouse

  #drawing user_interface objects onto the screen
  free_mode_button.draw(screen)
  back_button.draw(screen)
  forward_button.draw(screen)
  save_game_button.draw(screen)
  instructions_button.draw(screen)

  #drawing chess_board objects onto the screen
  board.draw_whole_board(screen)
  board.draw_all_pieces(screen)
  board.draw_points(screen, default_text)

  #drawing notation panel onto screen
  notation_panel.draw(screen, board.get_notation().get_moves()) 

  #checking if user_interface objects are clicked or user wants to scroll down/up notation
  free_mode_button.check_if_clicked(board)
  back_button.check_if_clicked(board)
  forward_button.check_if_clicked(board)
  notation_panel.update_scroll(pygame.key.get_pressed())
  save_game_button.check_if_clicked(board)
  instructions_button.check_if_clicked()

  #event handler
  for event in pygame.event.get():

    board.move_pieces(event, pos) #allows user to move pieces

    if event.type == pygame.QUIT: #close window when user exits
      run = False

  pygame.display.update()  

pygame.quit()

#board.print_pieces() #prints the current board position in terminal

