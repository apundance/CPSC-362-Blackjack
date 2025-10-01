import random

# Deck of cards

Deck = [2, 3, 4, 5, 6, 7, 8, 9, 'J', 'Q', 'K', 'A']
playerHand = []
dealerHand = []

# Deal hands
def DealCard(Turn):
    card = random.choice(Deck)
    Turn.append(card)     
    Deck.remove(card)

# Calculate total of each hand
def Total(Turn):
    Aces = 0
    total = 0
    face = ['J', 'Q', 'K']
    for card in Turn:
        if card in range(1, 11):
            total += card
        elif card in face:
            total += 10
        elif card == 'A':
            Aces += 1
    total += Aces * 11

    for _ in range(Aces):
        if total > 21:
            total -= 10
        else: 
            break

    return total

# Check for winner 
def revealDealerHand():
    if len(dealerHand) == 2:
        return dealerHand[0]
    else: 
        return dealerHand  
    
# Check whoever is closer to 21
def DealerWins():
    if 21 - Total(dealerHand) < 21 - Total(playerHand):
        return True
    else: 
        return False