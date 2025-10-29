import CardFunctions
import pygame, sys, os, random
import CardFunctions
pygame.init()

# Colors 
GREEN_DARK = (10, 80, 10)
GREEN_LIGHT = (0, 120, 0)
WHITE = (255, 255, 255)
GOLD = (255, 215, 0)


# Draw text
# ───────────────────────────────
def draw_text(surface, text, x, y, size=36, color=WHITE, center=False, screen_center=False):
    font = pygame.font.Font("freesansbold.ttf", size)
    img = font.render(text, True, color)
    rect = img.get_rect()

    if screen_center:
        rect.center = (surface.get_width() // 2, y)
    elif center:
        rect.center = (x, y)
    else:
        rect.topleft = (x, y)

    surface.blit(img, rect)

# ───────────────────────────────


# Draw button
# ───────────────────────────────
def draw_button(surface, text, rect, base_color, hover_color, events=None):
    mouse_pos = pygame.mouse.get_pos()
    clicked = False

    if events:
        for e in events:
            if e.type == pygame.MOUSEBUTTONDOWN and e.button == 1:
                if rect.collidepoint(e.pos):
                    clicked = True

    color = hover_color if rect.collidepoint(mouse_pos) else base_color
    pygame.draw.rect(surface, color, rect, border_radius=10)
    draw_text(surface, text, rect.centerx, rect.centery, 36, center=True)
    return clicked

# ───────────────────────────────


# Setup pygame
pygame.init()
width, height = 1000, 700
screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
pygame.display.set_caption("BlackjackTesting")
clock = pygame.time.Clock()

state = "menu"
running = True

# main loop
# ───────────────────────────────
while running:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False

    # draw green background
    screen.fill(GREEN_LIGHT)

    if state == "menu":
        # title
        draw_text(screen, "Welcome to BlackJack", 0, 200, 72, GOLD, screen_center=True)

        # button
        start_button = pygame.Rect(width // 2 - 120, 400, 240, 70)
        if draw_button(screen, "Start Game", start_button, (30,100,30), (60,160,60)):
            print("Start button clicked!")  # later we’ll move to the play state

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()