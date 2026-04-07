import os, pygame
folder = "monster"
monster_frames = []
for file in sorted(os.listdir(folder)):
    monster_frames.append(pygame.image.load(f"{folder}/{file}"))

for img in monster_frames:
    print(img)