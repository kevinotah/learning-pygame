import pygame

pygame.init()
display = pygame.display.set_mode((1000, 500))

icon = pygame.image.load("epita.png")
icon = pygame.transform.scale(icon, (32, 32))

pygame.display.set_icon(icon)
pygame.display.set_caption("Basics")

clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
    pygame.display.update()
    clock.tick(60)
pygame.quit()