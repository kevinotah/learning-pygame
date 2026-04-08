import pygame, os

pygame.init()
display = pygame.display.set_mode((1000, 500))

icon = pygame.image.load("epita.png")
icon = pygame.transform.scale(icon, (32, 32))

pygame.display.set_icon(icon)
pygame.display.set_caption("Basics")

clock = pygame.time.Clock()

font = pygame.font.Font("retrovibes.ttf", 100)

sky_surface = pygame.image.load('sky.png').convert_alpha()
ground_surface = pygame.image.load('pavement.png').convert_alpha()
text_surface = font.render("Basics", True, 'black')
text_surface_rect = text_surface.get_rect(center = (500, 100))

monster_folder = "monster"
monster_frames = []
for file in sorted(os.listdir(monster_folder)):
    monster = pygame.image.load(f"{monster_folder}/{file}").convert_alpha()
    monster = pygame.transform.scale(monster, (300, 300))
    monster_frames.append(monster)

player_standing_folder = "ben10standing"
player_standing_frames = []
for file in sorted(os.listdir(player_standing_folder)):
    player = pygame.image.load(f"{player_standing_folder}/{file}").convert_alpha()
    player = pygame.transform.scale(player, (300, 300))
    player_standing_frames.append(player)
    
player_running_folder = "ben10running"
player_running_frames = []
player_running_backward_frames = []
for file in sorted(os.listdir(player_running_folder)):
    player = pygame.image.load(f"{player_running_folder}/{file}").convert_alpha()
    player = pygame.transform.scale(player, (300, 300))
    player_running_frames.append(player)
    
    player_running_backward_frames.append(pygame.transform.flip(player, True, False))

monster_index = 0
monster_x = 700
monster_y = 200

player_index = 0
player_x = 0
player_y = 180

running = True
while running:
    clock.tick(30)
    
    if monster_index >= len(monster_frames) - 1:
        monster_index = 0
    if monster_x <= -200:
        monster_x = 1000
        
    if player_index >= len(player_standing_frames) or player_index >= len(player_running_frames):
        player_index = 0
    if player_x <= -60:
        player_x = -60
    if player_x >= 770:
        player_x = 770
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    display.blit(sky_surface, (-1, -1))
    display.blit(ground_surface, (-20, -50))
    display.blit(text_surface, text_surface_rect)  
    display.blit(monster_frames[monster_index], (monster_x, monster_y))
    monster_index += 1
    monster_x -= 5
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        display.blit(player_running_frames[int(player_index)], (player_x, player_y))
        player_x += 5
    elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
        display.blit(player_running_backward_frames[int(player_index)], (player_x, player_y))
        player_x -= 5
    else:
        display.blit(player_standing_frames[int(player_index)], (player_x, player_y))
    player_index += 0.2
        
    pygame.display.update()
    
pygame.quit()