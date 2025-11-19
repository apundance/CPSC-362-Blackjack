import random

# Full 52-card deck with suits
values = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
suits  = ['♥','♦','♣','♠']
originalDeck = [v + s for v in values for s in suits]
Deck = originalDeck.copy()

playerHand = []
dealerHand = []

# Deal a card
def DealCard(hand):
    global Deck
    if not Deck:
        reshuffle()
    card = random.choice(Deck)
    hand.append(card)
    Deck.remove(card)

# Reshuffle (rebuild full deck)
def reshuffle():
    global Deck
    Deck = originalDeck.copy()
    random.shuffle(Deck)

# Start fresh hands
def playAgain():
    playerHand.clear()
    dealerHand.clear()

# Calculate total of each hand
def Total(hand):
    total, aces = 0, 0
    for card in hand:
        value = card[:-1] if isinstance(card, str) else card
        if value in ['J', 'Q', 'K']:
            total += 10
        elif value == 'A':
            total += 11
            aces += 1
        else:
            total += int(value)

    while total > 21 and aces > 0:
        total -= 10
        aces -= 1

    return total

# Deal starting hands (2 each)
def starting_hands():
    for _ in range(2):
        DealCard(playerHand)
        DealCard(dealerHand)

# Dealer logic: check who wins
def DealerWins():
    p = Total(playerHand)
    d = Total(dealerHand)
    if p > 21:
        return True      # player bust
    if d > 21:
        return False     # dealer bust
    return d >= p
