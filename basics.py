import pygame

pygame.init()
display = pygame.display.set_mode((1000, 500))
pygame.display.set_caption("Basics", "bscs")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    pygame.display.update()