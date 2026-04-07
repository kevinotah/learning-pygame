import pygame, os

pygame.init()
display = pygame.display.set_mode((1000, 500))

icon = pygame.image.load("epita.png")
icon = pygame.transform.scale(icon, (32, 32))

pygame.display.set_icon(icon)
pygame.display.set_caption("Basics")

clock = pygame.time.Clock()

font = pygame.font.Font("retrovibes.ttf", 100)

sky_surface = pygame.image.load('sky.png')
ground_surface = pygame.image.load('pavement.png')
text_surface = font.render("Basics", True, 'black')
rect = text_surface.get_rect(center = (500, 100))

folder = "monster"
monster_frames = []
for file in sorted(os.listdir(folder)):
    monster = pygame.image.load(f"{folder}/{file}")
    monster = pygame.transform.scale(monster, (300, 300))
    monster_frames.append(monster)

running = True
i = 0
x = 700
y = 200
while running:
    if i >= len(monster_frames) - 1:
        i = 0
    if x <= -200:
        x = 1000
    
    clock.tick(60)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    display.blit(sky_surface, (-1, -1))
    display.blit(ground_surface, (-20, -50))
    display.blit(text_surface, rect)  
    display.blit(monster_frames[i], (x, 200))
    i += 1
    x -= 5
        
    pygame.display.update()
    
pygame.quit()