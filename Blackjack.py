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
def draw_card(surface, card, x, y, hidden=False):

    if hidden:
        pygame.draw.rect(surface, (200,0,0), (x, y, 80, 120))
        pygame.draw.rect(surface, WHITE, (x, y, 80, 120), 2)
        return
    
    suit = card[-1]
    color = RED if suit in ['♥','♦'] else BLACK

    # white card
    pygame.draw.rect(surface, WHITE, (x, y, 80, 120))
    pygame.draw.rect(surface, BLACK, (x, y, 80, 120), 2)

    # font style 
    font = pygame.font.SysFont("arial", 32)

    # render whole card string (A♥, 10♠, Q♦, etc.)
    text = font.render(card, True, color)

    # center the card text inside the rectangle
    rect = text.get_rect(center=(x + 40, y + 60))
    surface.blit(text, rect)

# Setup pygame
# ───────────────────────────────
width, height = 1000, 700
screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
pygame.display.set_caption("BlackjackTesting")
clock = pygame.time.Clock()

state = "menu"
running = True
msg_color = GOLD

game_started = False
winner_message = None
round_over = False

# Setup Bet
balance = 100
bet = 0
input_box = pygame.Rect(width // 2 - 100, 330, 200, 40)  # Define input box dimensions
active = False  # Initially, the input box is inactive
text = ''  # The text that the user inputs
color_inactive = pygame.Color(255, 255, 255)  # Inactive color (white)
color_active = pygame.Color(200, 200, 200)  # Active color (light grey)
color = color_inactive  # Set the initial input box color
error_message = None  # Placeholder for error message

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
        state = "betting"

    # ───────────── BETTING ─────────────
    elif state == "betting":
        screen.fill(GREEN_LIGHT)  # Fill screen with background color
        
        # Titles and instructions
        draw_text(screen, "Place Your Bet", 0, 100, 60, GOLD, screen_center=True)
        draw_text(screen, f"Your Balance: ${balance}", 0, 180, 40, WHITE, screen_center=True)
        draw_text(screen, "Enter amount:", 0, 260, 40, WHITE, screen_center=True)

        # Event loop for handling user input
        for event in events:
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                # Check if the user clicked inside the input box
                if input_box.collidepoint(event.pos):
                    active = True
                    color = color_active  # Change color to active
                else:
                    active = False
                    color = color_inactive  # Change color to inactive

            if event.type == pygame.KEYDOWN and active:
                if event.key == pygame.K_RETURN:
                    # Handle the enter key (confirm the bet)
                    try:
                        bet_amount = int(text)  # Try to convert text to an integer
                    
                        if bet_amount > 0 and bet_amount <= balance: 
                            bet = bet_amount
                            balance -= bet
                            text = ""
                            error_message = None
                            state = "play"
                        if bet_amount <= 0:
                             error_message = "Bet must be greater than 0."
                        else:
                            error_message = f"Invalid bet. Max bet: ${balance}"  # Error message if invalid bet
                        
                    except ValueError:
                        error_message = "Please enter a valid number."  # Error if input is not a number
                
                elif event.key == pygame.K_BACKSPACE:
                    # Remove the last character from the input text
                    text = text[:-1]
                else:
                    # Add the typed character to the text string
                    if len(text) < 6:  # Optional limit to 6 characters
                       text += event.unicode

        # Render the input box (active or inactive)
        pygame.draw.rect(screen, color, input_box)

        # Render the text inside the input box
        font = pygame.font.SysFont("arial", 32)  # Font for text rendering
        txt_surface = font.render(text, True, BLACK)  # Black text for the input
        screen.blit(txt_surface, (input_box.x + 5, input_box.y + 5))  # Draw text inside the box

        # Draw the input box border
        pygame.draw.rect(screen, WHITE, input_box, 2)  # White border for the input box

        # Display error message if any
        if error_message:
            error_text = font.render(error_message, True, RED)  # Red error text
            screen.blit(error_text, (width // 2 - error_text.get_width() // 2, 450))  # Centered error message

        # Render the "Confirm Bet" button
        confirm_button = pygame.Rect(width // 2 - 120, 500, 240, 70)
        if draw_button(screen, "Confirm Bet", confirm_button, (30, 100, 30), events):
            try:
                bet_amount = int(text)
                if bet_amount > 0 and bet_amount <= balance:
                    bet = bet_amount
                    balance -= bet
                    text = ""
                    error_message = None
                    state = "play"
                else:
                    error_message = f"Invalid bet. Max: ${balance}"
            except:
                error_message = "Enter a valid number."

        # Render the "Back to Menu" button
        back_button = pygame.Rect(40, 40, 160, 50)
        if draw_button(screen, "Menu", back_button, (100, 30, 30), events):
            state = "menu"
            balance = 100  # Reset the bet back to the initial value
            bet = 0
            text = ""
            error_message = None  # Clear any error message


    # ───────────── PLAY ─────────────
    elif state == "play":
    # initialize new round once
        if not game_started:
            CardFunctions.starting_hands()
            game_started = True
            round_over = False
            winner_message = None

        # titles
        draw_text(screen, "Dealer", 0, 70, 40, WHITE, screen_center=True)
        draw_text(screen, "Player", 0, 360, 40, WHITE, screen_center=True)

        # money balance
        draw_text(screen, f"Balance: ${balance}", (width / 1.7 ), 20, 32, WHITE, center=False)


        # draw dealer cards
        x = 200
        for i, card in enumerate(CardFunctions.dealerHand):
            if i == 1 and not round_over:
                draw_card(screen, card, x, 120, hidden=True)
            else:
                draw_card(screen, card, x, 120)
            x += 100

        # draw player cards
        x = 200
        for card in CardFunctions.playerHand:
            draw_card(screen, card, x, 410)
            x += 100

        # totals
        dealer_total = CardFunctions.Total(CardFunctions.dealerHand)
        player_total = CardFunctions.Total(CardFunctions.playerHand)
        dealer_display = "?" if not round_over else dealer_total
        draw_text(screen, f"Dealer Total: {dealer_display}", 0, 260, 32, WHITE, screen_center=True)
        draw_text(screen, f"Player Total: {player_total}", 0, 550, 32, WHITE, screen_center=True)

        # buttons
        hit_button = pygame.Rect(width // 2 - 250, 610, 200, 60)
        stand_button = pygame.Rect(width // 2 + 50, 610, 200, 60)
        back_button = pygame.Rect(40, 40, 160, 50)

        # only allow buttons during round
        if not round_over:
            if draw_button(screen, "Hit", hit_button, (30, 100, 30), events):
                CardFunctions.DealCard(CardFunctions.playerHand)
                if CardFunctions.Total(CardFunctions.playerHand) > 21:
                    winner_message = "Dealer Wins!"
                    msg_color = RED
                    round_over = True

            if draw_button(screen, "Stand", stand_button, (100, 30, 30), events):
                while CardFunctions.Total(CardFunctions.dealerHand) < 17:
                    CardFunctions.DealCard(CardFunctions.dealerHand)
                if CardFunctions.DealerWins():
                    winner_message = f"Dealer Wins! -{bet}"
                    msg_color = RED
                    balance -= bet
                else:
                    winner_message = f"Player Wins! +{bet}"
                    msg_color = GOLD
                    balance += bet * 2
                round_over = True

        # if round finished, display message and wait for user click
        else:
            draw_text(screen, winner_message, 0, 300, 60, msg_color, screen_center=True)
            again_button = pygame.Rect(width // 2 - 150, 630, 300, 50)
            if draw_button(screen, "Play Again", again_button, (30, 100, 30), events):
                CardFunctions.playAgain()
                game_started = False   # reset for next round
                round_over = False
                winner_message = None
                bet = 0
                state = "betting"

        # menu return
        if draw_button(screen, "Menu", back_button, (30, 100, 30), events):
            state = "menu"
            game_started = False
            round_over = False
            winner_message = None

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
