import random

# Deck of cards
Deck = [2, 3, 4, 5, 6, 7, 8, 9, 'J', 'Q', 'K', 'A'] # Game deck
originalDeck = [2, 3, 4, 5, 6, 7, 8, 9, 'J', 'Q', 'K', 'A'] #Unaltered deck
playerHand = []
dealerHand = []

# Deal hands
def DealCard(Turn):
    card = random.choice(Deck)
    Turn.append(card)     
    Deck.remove(card)

# Shuffle function
#just for future proofing if we decide to do more specific cards like 2 of Aces - can create the cards here
def cardShuffle():
    global Deck
    DeckSize = 4
    Deck = originalDeck * DeckSize
    random.shuffle(Deck)
    return print("Shuffling...")

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


def starting_hands():
    for _ in range(2):
        DealCard(playerHand)
        DealCard(dealerHand)
    print(f"Dealer has {revealDealerHand()} and X")
    print(f"You have {playerHand} with total of {Total(playerHand)}\n")

# Reveal Dealer hand
def revealDealerHand():
    if len(dealerHand) == 2:
        return dealerHand[0]
    else: 
        return dealerHand  
    
#  Check whoever is closer to 21
def DealerWins():
    if 21 - Total(dealerHand) < 21 - Total(playerHand):
        return True
    else: 
        return False