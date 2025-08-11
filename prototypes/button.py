import pygame

pygame.init()

#window
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

#rectangle variable
button_clicked = False #used to prevent the button getting activated multiple times despite one click
rectangle = pygame.Rect(100, 100, 200, 200)

#game loop
run = True
while run == True: 
  
  pygame.draw.rect(screen, (80, 200, 120), rectangle) #draw rectangle
  pos = pygame.mouse.get_pos() #getting position of the mouse

  if rectangle.collidepoint(pos): #if user is hovering over button
    if pygame.mouse.get_pressed()[0] and button_clicked == False: #if user clicks button
      print("User clicked green button")
      button_clicked = True

  if not pygame.mouse.get_pressed()[0]: #resetting button when user finishes clicking
    button_clicked = False

  #event handler
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False

  pygame.display.update()  

pygame.quit()
