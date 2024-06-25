from helpers import cards, drawCard, calculateValue, keepGoing
import time

playerMoney = 100
bettingMoney = 0
playerTotal = 0
dealerTotal = 0

while True: # Loops untiil player says they don't want to continue
    print(f"Welcome to blackjack.  You currently have ${playerMoney}.")
    bettingMoney = 0
    playerTotal = 0
    dealerTotal = 0
    deck = cards
    time.sleep(1)

    # Get amount player wants to bet
    while True:
        bet = input(f"How much would you like to bet? You have {playerMoney}: ")
        try:
            bettingMoney = int(bet)
            if bettingMoney <= playerMoney:
                print(f"You bet {bettingMoney}")
                break
            else:
                print(f"You can't bet more than you have!  You have: ${playerMoney}")
        except ValueError:
            print("Please put an integer amount of money!")

    # Initial two cards for dealer and player
    i = 1
    while i <= 2:
        time.sleep(1)

        playerCard = drawCard(deck)
        playerTotal += calculateValue(playerCard, playerTotal)
        deck.remove(playerCard)
        print(f"You drew a(n) {playerCard}.  Your total is: {playerTotal}")
        time.sleep(1)

        dealerCard = drawCard(deck)
        dealerTotal += calculateValue(dealerCard, dealerTotal)
        deck.remove(dealerCard)
        if i == 1:
            print(f"The dealer draws a(n) {dealerCard}.  The dealer's total is: {dealerTotal}.")
        else: 
            print("The dealer draws another card.")

        i += 1
        time.sleep(1)

    # If 21 is achieved on first two cards
    if playerTotal == 21 and dealerTotal != 21:
        playerMoney += bettingMoney
        print(f"You win!  Your total is now: ${playerMoney}")
        keepGoing(playerMoney)
    elif playerTotal < 21 and dealerTotal == 21:
        playerMoney -= bettingMoney
        print(f"You lost!  The dealer's second card was {dealerCard}.  Your total is now: ${playerMoney}")
        keepGoing(playerMoney)
    elif playerTotal == 21 and dealerTotal == 21:
        print(f"You and the dealer both got 21!  The dealer's second card was {dealerCard}.  Your bet was returned.")
        keepGoing(playerMoney)

    print(f"Once again, your total is {playerTotal}")
    time.sleep(1)

    # Player hitting or standing
    while playerTotal <= 21:
        while True:
            hitOrStand = input("Would you like to hit or stand?: ")
            if hitOrStand == "hit" or hitOrStand == "stand":
                break
            else:
                print("Please say hit or stand!")
        if hitOrStand == "hit":
            playerCard = drawCard(deck)
            print(f"You hit.  You draw a {playerCard}.")
            playerTotal += calculateValue(playerCard, playerTotal)
            print(f"Your total is now: {playerTotal}.")
            deck.remove(playerCard)
        else:
            print(f"You stood.  Your total is: {playerTotal}")
            break

    # If player busts
    if playerTotal > 21:
        print(f"You busted!  You lost: {bettingMoney}")
        playerMoney -= bettingMoney
        print(f"Your balance is now: ${playerMoney}.")
        keepGoing(playerMoney)

    time.sleep(1)
    print(f"The dealer flips over their second card.  It's a {dealerCard}.")
    time.sleep(1)
    # Dealer drawing cards and hitting/standing
    while dealerTotal <= 18:
        dealerCard = drawCard(deck)
        dealerTotal += calculateValue(dealerCard, dealerTotal)
        print(f"The dealer draws another card.  It's a {dealerCard}! The dealer's total is now {dealerTotal}. ")
        time.sleep(1)

    # If dealer gets 21 or busts
    if dealerTotal == 21:
        playerMoney -= bettingMoney
        print(f"You lost! Your balance is now: ${playerMoney}")
        keepGoing(playerMoney)
    elif dealerTotal > 21:
        print("The dealer busts!")
        playerMoney += bettingMoney
        time.sleep(1)
        print(f"You won! Your balance is now: ${playerMoney}")
        keepGoing(playerMoney)

    # If dealer total is below 21.  Dealer will not hit if their total is above 18
    print(f"The dealer chooses to stand.  Their total is {dealerTotal}.")
    time.sleep(1)

    # If both dealer and player stand before getting 21
    if playerTotal == dealerTotal:
        print(f"You tied!  Your bet has been returned.")
        keepGoing(playerMoney)
    elif playerTotal > dealerTotal:
        playerMoney += bettingMoney
        print(f"You won!  Your balance is now: {playerMoney}")
        keepGoing(playerMoney)
    elif playerTotal < dealerTotal:
        playerMoney -= bettingMoney
        print(f"You lost!  Your balance is now: {playerMoney}")
        keepGoing(playerMoney)
