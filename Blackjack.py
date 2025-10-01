import CardFunctions

playerHand = []
dealerHand = []
# Main game loop
for _ in range(2):
    CardFunctions.cardShuffle()
    CardFunctions.DealCard(playerHand)
    CardFunctions.DealCard(dealerHand)

print(f"Player Hand = {playerHand} Dealer Hand = {dealerHand}")

