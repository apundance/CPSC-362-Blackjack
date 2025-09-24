import CardFunctions 
playerHand = []
dealerHand = []
# Main game loop
for _ in range(2):
    CardFunctions.DealCards(playerHand)
    CardFunctions.DealCards(dealerHand)

print(f"Player Hand = {playerHand} Dealer Hand = {dealerHand}")

