# Library for functions
import random

 # Deck of cards

## Deck of cards * 4 = 
Deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A'] * 4

# Deal hands (pass in player or dealer and get card dealt)
def DealCards(Turn):
    card = random.choice(Deck)
    Turn.append(card)
    Deck.remove(card)

# Calculate Total of each hand

# Check for winner

# Check whose closer to 21

