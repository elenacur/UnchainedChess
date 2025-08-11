import pygame

pygame.init()

#window
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

#piece variables
piece_image = pygame.Surface((80, 80))
piece_image.fill(("blue"))
piece_rect = piece_image.get_rect()
dragging = False

run = True
while run == True: #game loop
  screen.fill((0, 0, 0))
  
  pos = pygame.mouse.get_pos() #getting position of the mouse

  screen.blit(piece_image, piece_rect)

  #event handler
  for event in pygame.event.get():

    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1: 
       if piece_rect.collidepoint(pos): #if user left clicks on piece
         dragging = True
    
    if event.type == pygame.MOUSEMOTION and dragging == True: #if user moves mouse after clicking on piece
      piece_rect.move_ip(event.rel) #update position of the piece by the same change as the mouse position

    if event.type == pygame.MOUSEBUTTONUP and event.button == 1: #if user stops holding down left click
      dragging = False #stop moving piece
      

    if event.type == pygame.QUIT:
      run = False

  pygame.display.update()  

pygame.quit()
