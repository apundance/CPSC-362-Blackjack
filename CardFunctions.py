import random

# Deck of cards
Deck = [2, 3, 4, 5, 6, 7, 8, 9, 'J', 'Q', 'K', 'A']  # Game deck
originalDeck = [2, 3, 4, 5, 6, 7, 8, 9, 'J', 'Q', 'K', 'A']  # Unaltered deck
playerHand = []
dealerHand = []

# Deal hands
def DealCard(Turn):
    if not Deck:
        print("Deck is empty! Reshuffling...")
        cardShuffle()
    card = random.choice(Deck)
    Turn.append(card)
    Deck.remove(card)

# Shuffle function
def cardShuffle():
    global Deck
    DeckSize = 4
    Deck = originalDeck * DeckSize
    random.shuffle(Deck)
    print("Shuffling...")

# Clear hands to start again
def playAgain():
    playerHand.clear()
    dealerHand.clear()

# Calculate total of each hand
def Total(Turn):
    Aces = 0
    total = 0
    face = ['J', 'Q', 'K']
    for card in Turn:
        if isinstance(card, int):  # numeric cards
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

# Deal starting hands
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

# Check whoever is closer to 21
def DealerWins():
    player_total = Total(playerHand)
    dealer_total = Total(dealerHand)

    if player_total > 21:
        return True  # player busts
    if dealer_total > 21:
        return False  # dealer busts
    if dealer_total >= player_total:
        return True
    return False
