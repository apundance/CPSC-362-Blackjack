import CardFunctions

# MENU 
def start_menu():
    print("==============================")
    print("1. Start Game")
    print("2. Rules")
    print("3. Exit")
    print("==============================")

def show_rules():
    print("\n=== Blackjack Rules ===")
    print("1. Try to get as close to 21 as possible without going over.")
    print("2. Number cards are worth their number, face cards are 10, Ace is 1 or 11.")
    print("3. Dealer hits until reaching 17 or higher.")
    print("4. Player wins if closer to 21 than dealer without busting.\n")

# Start Menu
print( "==== Welcome to Blackjack ====")
while True:
    start_menu()
    decide = input("Select an option (1-3): ") 
    if decide == '1':
        print("Starting game...\n")
        break
    elif decide == "2":
            show_rules()
    elif decide == "3":
            print("Thanks for playing!")
            exit()
    else:
        print("Invalid choice, please try again.\n")



# Main game loop

CardFunctions.cardShuffle() 
# Set player and dealer 
GameDeck = CardFunctions.Deck
Player = CardFunctions.playerHand
Dealer = CardFunctions.dealerHand

while True:
 
    # Shuffle when deck is close to empty
    if len(GameDeck) < 10:
        CardFunctions.cardShuffle() 
        GameDeck = CardFunctions.Deck
    

    # Initalize start of game
    print("==============================")
    CardFunctions.starting_hands()


    playerTurn = True
    DealerTurn = False
    totalPlayer = CardFunctions.Total(Player)
    totalDealer = CardFunctions.Total(Dealer)

    print(f"Dealer Hand = {Dealer}, dealer total is: {totalDealer}" )
    print(f"Player Hand = {Player} player total is: {totalPlayer}")

    playAgain = input("Would you like to continue ? (Y/y = yes, N/n = no) ==> ").lower()
    if playAgain != "y":
        print("Thank you for playing!")
        print("==============================")
        break
    CardFunctions.playAgain()

    

