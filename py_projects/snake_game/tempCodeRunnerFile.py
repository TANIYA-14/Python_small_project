
    surface = pygame.display.set_mode((500,500))
    surface.fill((94, 152, 27))
    pygame.display.flip()

#for event loop for input exit
    running = True

    while running:
        for event in pygame.event.get():
          if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
               running = True
          elif event.type == QUIT:
             running = False  
        