playerMoney = 100
print("Welcome to blackjack.  You currently have $100.")

while True:
    bet = input(f"How much would you like to bet? You have {playerMoney}: ")
    try:
        int(bet)
        if bet <= playerMoney:
            break
        else:
            print(f"You can't bet more than you have!  You have: {playerMoney}")
    except ValueError:
        print("Please put an integer amount of money!")