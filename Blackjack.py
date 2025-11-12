import pygame, sys, os, random
import CardFunctions

pygame.init()

# Colors
# ───────────────────────────────
GREEN_LIGHT = (0, 120, 0)
WHITE = (255, 255, 255)
GOLD = (255, 215, 0)
BLACK = (0, 0, 0)
RED = (200, 0, 0)
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

# ───────────────────────────────
# Draw Card 
# (Visual rectangle cards adapted from partner’s table layout)
def draw_card(surface, card, x, y, hidden = False):
    pygame.draw.rect(surface, WHITE, (x, y, 80, 120), border_radius=5)
    pygame.draw.rect(surface, BLACK, (x, y, 80, 120), 2)

    if hidden: 
        pygame.draw.rect(surface, BLACK, (x, y, 80, 120), border_radius=5)
        pygame.draw.rect(surface, GOLD, (x+5, y+5, 70, 110), 3)
        return
    font = pygame.font.Font("freesansbold.ttf", 28)
    suit = card[-1]
    color = RED if suit in ['♥', '♦'] else BLACK
    text = font.render(str(card), True, color)
    surface.blit(text, (x + 15, y + 45))

# Setup pygame
# ───────────────────────────────
width, height = 1000, 700
screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
pygame.display.set_caption("BlackjackTesting")
clock = pygame.time.Clock()

state = "menu"
running = True
msg_color = GOLD
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
        CardFunctions.reshuffle()
        CardFunctions.playAgain()

        game_started = False
        winner_message = None
        state = "play"

    
    # ───────────── PLAY ─────────────
    elif state == "play":
        if not game_started:
            CardFunctions.starting_hands()
            game_started = True

        # display titles
        draw_text(screen, "Dealer", 0, 70, 40, WHITE, screen_center=True)
        draw_text(screen, "Player", 0, 360, 40, WHITE, screen_center=True)

        # draw dealer cards
        x = 200
        for i, card in enumerate(CardFunctions.dealerHand):
            if i == 1 and not winner_message:
                draw_card(screen, card, x, 120, hidden=True)  # hide dealer's 2nd card
            else:
                draw_card(screen, card, x, 120)
            x += 100

        # draw player cards
        x = 200
        for card in CardFunctions.playerHand:
            draw_card(screen, card, x, 410)
            x += 100

        # show totals
        dealer_total = CardFunctions.Total(CardFunctions.dealerHand)
        player_total = CardFunctions.Total(CardFunctions.playerHand)
        draw_text(screen, f"Dealer Total: {dealer_total}", 0, 260, 32, WHITE, screen_center=True)
        draw_text(screen, f"Player Total: {player_total}", 0, 550, 32, WHITE, screen_center=True)

        # buttons
        hit_button = pygame.Rect(width // 2 - 250, 610, 200, 60)
        stand_button = pygame.Rect(width // 2 + 50, 610, 200, 60)
        back_button = pygame.Rect(40, 40, 160, 50)

        if not winner_message:
            if draw_button(screen, "Hit", hit_button, (30, 100, 30), events):
                CardFunctions.DealCard(CardFunctions.playerHand)
                if CardFunctions.Total(CardFunctions.playerHand) > 21:
                    winner_message = "Dealer Wins!"
                    msg_color = RED

            if draw_button(screen, "Stand", stand_button, (100, 30, 30), events):
                while CardFunctions.Total(CardFunctions.dealerHand) < 17:
                    CardFunctions.DealCard(CardFunctions.dealerHand)
                if CardFunctions.DealerWins():
                    winner_message = "Dealer Wins!"
                    msg_color = RED
                else:
                    winner_message = "Player Wins!"
                    msg_color = GOLD

        # show winner
        if winner_message:
            draw_text(screen, winner_message, 0, 300, 60, msg_color, screen_center=True)
            again_button = pygame.Rect(width // 2 - 150, 630, 300, 50)
            if draw_button(screen, "Play Again", again_button, (30, 100, 30), events):
                CardFunctions.playAgain()
                CardFunctions.starting_hands()
                winner_message = None
                msg_color = GOLD
                game_started = True

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
