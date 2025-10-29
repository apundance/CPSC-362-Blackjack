import CardFunctions
import pygame, sys, os, random
import CardFunctions
pygame.init()


# Setup pygame
pygame.init()
width, height = 1000, 700
screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
pygame.display.set_caption("BlackjackTesting")
clock = pygame.time.Clock()

running = True

# main loop
# ───────────────────────────────
while running:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False



    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()