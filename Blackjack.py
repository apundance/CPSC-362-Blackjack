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

def hitStay():
    print("==============================")
    print("1. Hit")
    print("2. Stay")
    print("==============================")

def askBet():
    print("==============================")
    print(f"You currently have {balance} dollars")
    print("How much you betting?")

# Start Menu
print( "==== Welcome to Blackjack ====")
while True:
    start_menu()
    decide = input("Select an option (1-3): ") 
    if decide == '1':
        print("Starting game...")
        break
    elif decide == "2":
            show_rules()
    elif decide == "3":
            print("Thanks for playing!")
            exit()
    else:
        print("Invalid choice, please try again.\n")

balance = 100

# shuffles up the deck
CardFunctions.cardShuffle() 

# sets the player, dealer hands and the deck
GameDeck = CardFunctions.Deck
Player = CardFunctions.playerHand
Dealer = CardFunctions.dealerHand

while True:
    # clears hands so it doesnt retain cards from the last round
    CardFunctions.playAgain()

    # deck should never be close to empty but just in case
    if len(GameDeck) < 10:
        print("Deck is running low on cards!")
        CardFunctions.cardShuffle() 
        GameDeck = CardFunctions.Deck

    if balance <= 0:
        print("==============================")
        print("Looks like someone dropped a 100 dollar chip on the floor...")
        balance = 100
        print("==============================")

    askBet()
    
    while True:
        bet = int(input())
        print("==============================")
        break
    # starts the game
    print("==============================")
    CardFunctions.starting_hands()
    totalPlayer = CardFunctions.Total(Player)
    totalDealer = CardFunctions.Total(Dealer)
    
    # code for player actions
    # checks player initial total
    while True:
        totalPlayer = CardFunctions.Total(Player)
        if totalPlayer > 21:
            print(f"You busted! Total = {totalPlayer}\n")
            break

        # asks the player if they want to hit or stay
        hitStay()
        gamble = input("Hit or stay? ").strip()

        # if 1 then it deals a card and loops, if 2 then it stops
        if gamble == "1":
            CardFunctions.DealCard(Player)
            print(f"Your hand: {Player} (Total: {CardFunctions.Total(Player)})\n")
            continue
        elif gamble == "2":
            break
        else:
            print("Invalid input. Use only 1 or 2.\n")


    # code for automated dealer actions where it checks if their hand is less than 17 and if it is then it hits
    totalDealer = CardFunctions.Total(Dealer)
    while totalDealer < 17:
        CardFunctions.DealCard(Dealer)
        totalDealer = CardFunctions.Total(Dealer)

    # code to determine the winner
    print(f"Dealer's hand: {Dealer} (Total: {totalDealer})")
    print(f"Your hand: {Player} (Total: {CardFunctions.Total(Player)})\n")
    if CardFunctions.DealerWins():
        print("Dealer wins!\n")
        balance -= bet
    else:
        print("You win!\n")
        balance += bet

    # code to ask if the player wants to play again
    playAgain = input("Would you like to play again? (Y/N): ").lower()
    if playAgain != "y":
        print("Thank you for playing!")
        print("==============================")
        break

    

