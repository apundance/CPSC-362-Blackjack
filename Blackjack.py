import pygame, sys, os, random
import CardFunctions

pygame.init()

# Colors
# ───────────────────────────────
GREEN_LIGHT = (0, 120, 0)
WHITE = (255, 255, 255)
GOLD = (255, 215, 0)

# ───────────────────────────────

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
def draw_button(surface, text, rect, base_color, events=None):
    clicked = False
    if events:
        for e in events:
            if e.type == pygame.MOUSEBUTTONDOWN and e.button == 1:
                if rect.collidepoint(e.pos):
                    clicked = True

    # Button color stays fixed
    pygame.draw.rect(surface, base_color, rect, border_radius=10)
    draw_text(surface, text, rect.centerx, rect.centery, 36, center=True)
    return clicked
# ───────────────────────────────

# Setup pygame
# ───────────────────────────────
width, height = 1000, 700
screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
pygame.display.set_caption("BlackjackTesting")
clock = pygame.time.Clock()

state = "menu"
running = True
# ───────────────────────────────

# Main loop
# ───────────────────────────────
while running:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False

    # Draw background
    screen.fill(GREEN_LIGHT)

    # ─────────────── MENU SCREEN ───────────────
    if state == "menu":
        draw_text(screen, "Welcome to Blackjack", 0, 100, 60, GOLD, screen_center=True)

        start_button = pygame.Rect(width // 2 - 120, 400, 240, 70)
        rules_button = pygame.Rect(width // 2 - 120, 500, 240, 70)

        if draw_button(screen, "Start Game", start_button, (30,100,30), events):
            state = "loading"

        if draw_button(screen, "Rules", rules_button, (100,30,30), events):
            state = "rules"

    # ───────────── LOADING ─────────────
    elif state == "loading":
        draw_text(screen, "Shuffling cards...", 0, height//2, 60, GOLD, screen_center=True)
        pygame.display.flip()
        pygame.time.delay(1000)

        # Prepare new game
        CardFunctions.cardShuffle()
        CardFunctions.playAgain()

        game_started = False
        winner_message = None
        state = "play"

    
    # ───────────── PLAY ─────────────
    elif state == "play":
         # Initialize game hands only once
        if not game_started:
            CardFunctions.starting_hands()
            game_started = True

        # Draw labels
        draw_text(screen, "Dealer", 0, 80, 40, WHITE, screen_center=True)
        draw_text(screen, "Player", 0, 350, 40, WHITE, screen_center=True)

        # Display totals
        dealer_total = CardFunctions.Total(CardFunctions.dealerHand)
        player_total = CardFunctions.Total(CardFunctions.playerHand)
        draw_text(screen, f"Dealer Total: {dealer_total}", 0, 150, 32, WHITE, screen_center=True)
        draw_text(screen, f"Player Total: {player_total}", 0, 420, 32, WHITE, screen_center=True)

        hit_button = pygame.Rect(width // 2 - 250, 600, 200, 60)
        stand_button = pygame.Rect(width // 2 + 50, 600, 200, 60)

        # Play buttons
        if draw_button(screen, "Hit", hit_button, (30, 100, 30), events):
            print("Hit clicked!")

        if draw_button(screen, "Stand", stand_button, (100, 30, 30), events):
            print("Stand clicked!")


        back_button = pygame.Rect(40, 40, 200, 60)
        if draw_button(screen, "Back", back_button, (30, 100, 30), events):
            state = "menu"
            game_started = False

    # ─────────────── RULES SCREEN ───────────────
    elif state == "rules":
        draw_text(screen, "Blackjack Rules", 0, 80, 60, GOLD, screen_center=True)

        rules = [
                    "1. Try to get as close to 21 as possible without going over.",
                    "2. Number cards are worth their face value.",
                    "3. Face cards are worth 10, Aces are 1 or 11.",
                    "4. Dealer hits until reaching 17 or higher.",
                    "5. You win if closer to 21 than dealer without busting."
                ]
        
        y = 250
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
