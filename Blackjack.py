import CardFunctions

playerHand = []
dealerHand = []

# Main game loop
for _ in range(2):
    CardFunctions.cardShuffle()
    CardFunctions.DealCard(playerHand)
    CardFunctions.DealCard(dealerHand)

totalPlayer = CardFunctions.Total(playerHand)
totalDealer = CardFunctions.Total(dealerHand)

print(f"\nPlayers and Dealers starting hands and totals\n")
print(f"Player Hand = {playerHand} player total is: {totalPlayer}\nDealer Hand = {dealerHand}, dealer total is: {totalDealer}\n" )

