#imports
import pygame
from modules.chess_game.board.board import Board
from modules.user_interface.free_mode_button import FreeModeButton
from modules.user_interface.back_forward_buttons import BackForwardButtons
from modules.user_interface.notation_panel import NotationPanel
from modules.user_interface.save_game_button import SaveGameButton
from modules.user_interface.instructions_button import InstructionsButton
from modules.instructions.instructions_menu import InstructionsMenu

pygame.init()

#window and sizing and text
SCREEN_WIDTH = 1344
SCREEN_HEIGHT = 756

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

default_text = pygame.font.SysFont("Arial", 30)

#instantiating objects
board = Board(84, "", True, 0, False)
board.reset_board()
free_mode_button = FreeModeButton(110, 300, 80, 80, None, pygame.image.load("assets/button_images/red-free-mode-button.png"))
back_button = BackForwardButtons(20, 400, 80, 80, None, pygame.image.load("assets/button_images/back-button.png"), "back_button")
forward_button = BackForwardButtons(110, 400, 80, 80, None, pygame.image.load("assets/button_images/forward-button.png"), "forward_button")
notation_panel = NotationPanel(996, 70, 235, 672, default_text)
save_game_button = SaveGameButton(20, 300, 80, 80, None, pygame.image.load("assets/button_images/save-game-button.png"))
instructions_button = InstructionsButton(1254, 666, 80, 80, None, pygame.image.load("assets/button_images/instructions-button.png"))
instructions_menu = InstructionsMenu(0, 0, 1344, 756, None, pygame.image.load("assets/instructions-menu.png"))

show_instructions = False

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

  if show_instructions == False: #so user cannot edit board when instructions are showing
    #checking if user_interface objects are clicked or user wants to scroll down/up notation
    free_mode_button.check_if_clicked(board)
    back_button.check_if_clicked(board)
    forward_button.check_if_clicked(board)
    notation_panel.update_scroll(pygame.key.get_pressed())
    save_game_button.check_if_clicked(board)

  #check if instructions button is clicked
  if show_instructions == False:
    if instructions_button.check_if_clicked():
      show_instructions = True

  #draw instructions menu if instructions button has been clicked
  if show_instructions == True:
    instructions_menu.draw(screen)
    if instructions_menu.check_for_escape() == True: #if user presses escape, do nto draw instructions menu
      show_instructions = False


  #event handler
  for event in pygame.event.get():

    if show_instructions == False: #so user cannot move pieces when instructions are showing
      board.move_pieces(event, pos) #allows user to move pieces

    if event.type == pygame.QUIT: #close window when user exits
      run = False

  pygame.display.update()  

pygame.quit()

#board.print_pieces() #prints the current board position in terminal

