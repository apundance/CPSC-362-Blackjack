import pygame, sys, os, random
import CardFunctions

pygame.init()

# ───────────────────────────────
# Colors
GREEN_LIGHT = (0, 120, 0)
WHITE = (255, 255, 255)
GOLD = (255, 215, 0)

# ───────────────────────────────
# Draw text
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
def draw_button(surface, text, rect, base_color, events=None):
    clicked = False
    if events:
        for e in events:
            if e.type == pygame.MOUSEBUTTONDOWN and e.button == 1:
                if rect.collidepoint(e.pos):
                    clicked = True

    # button color stays fixed
    pygame.draw.rect(surface, base_color, rect, border_radius=10)
    draw_text(surface, text, rect.centerx, rect.centery, 36, center=True)
    return clicked

# ───────────────────────────────
# Setup pygame
width, height = 1000, 700
screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
pygame.display.set_caption("BlackjackTesting")
clock = pygame.time.Clock()

state = "menu"
running = True

# ───────────────────────────────
# Main loop
while running:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False

    # draw background
    screen.fill(GREEN_LIGHT)

    # ─────────────── MENU SCREEN ───────────────
    if state == "menu":
        draw_text(screen, "Welcome to Blackjack", 0, 200, 72, GOLD, screen_center=True)

        start_button = pygame.Rect(width // 2 - 120, 400, 240, 70)
        rules_button = pygame.Rect(width // 2 - 120, 500, 240, 70)

        if draw_button(screen, "Start Game", start_button, (30,100,30), events):
            print("Start Game Clicked!")  # later will go to gameplay

        if draw_button(screen, "Rules", rules_button, (100,30,30), events):
            state = "rules"

    # ─────────────── RULES SCREEN ───────────────
    elif state == "rules":
        draw_text(screen, "Blackjack Rules", 0, 100, 72, GOLD, screen_center=True)

        rules = [
            "1. Try to get as close to 21 as possible without going over.",
            "2. Face cards are worth 10; Aces are 1 or 11.",
            "3. Dealer hits until reaching 17 or higher.",
            "4. Player wins if closer to 21 than dealer without busting."
        ]
        y = 200
        for line in rules:
            draw_text(screen, line, 0, y, 32, WHITE, screen_center=True)
            y += 50

        back_button = pygame.Rect(width // 2 - 120, 600, 240, 60)
        if draw_button(screen, "Back to Menu", back_button, (30,100,30), events):
            state = "menu"

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
