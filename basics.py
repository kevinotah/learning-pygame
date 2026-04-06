import pygame

pygame.init()
display = pygame.display.set_mode((1000, 500))

icon = pygame.image.load("epita.png")
icon = pygame.transform.scale(icon, (32, 32))

pygame.display.set_icon(icon)
pygame.display.set_caption("Basics")

clock = pygame.time.Clock()

sky_surface = pygame.image.load('sky.png')

ground_surface = pygame.image.load('pavement.png')
ground_surface = pygame.transform.scale(ground_surface, (1200, 600))
center = ground_surface.get_rect(center = (500, 250))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    display.blit(sky_surface, (-1, -1))
    display.blit(ground_surface, center)        
        
    pygame.display.update()
    clock.tick(60)
pygame.quit()