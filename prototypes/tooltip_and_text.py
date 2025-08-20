import pygame

pygame.init()

#window
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

#rectangle variable
rectangle = pygame.Rect(100, 100, 200, 200)

#tooltip variables
font = pygame.font.Font(None, 20)
tooltip_rectangle = pygame.Rect(160, 305, 80, 30)
tooltip_text = font.render("tooltip text", True, (0, 0, 0))

#game loop
run = True
while run == True:
  screen.fill((0, 0, 0)) #background colour

  pygame.draw.rect(screen, (80, 200, 120), rectangle) #draw rectangle
  pos = pygame.mouse.get_pos() #getting position of the mouse

  if rectangle.collidepoint(pos): #if user is hovering over button
    pygame.draw.rect(screen, (211, 211, 211), tooltip_rectangle) #draw tooltip rectangle
    screen.blit(tooltip_text, (160, 320)) #draw tooltip text

  #event handler
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False

  pygame.display.update()  

pygame.quit()
