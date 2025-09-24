import random

# Deck of cards

Deck = [2, 3, 4, 5, 6, 7, 8, 9, 'J', 'Q', 'K', 'A']
playerHand = []
dealrHand = []

# Deal hands
def DealCard(Turn):
    card = random.choice(Deck)
    Turn.append(card)     
    Deck.remove(card)
