import random

# List of cards in deck
cards = ["ace", "ace", "ace", "ace",
         "king", "king", "king", "king",
         "queen", "queen", "queen", "queen",
         "jack", "jack", "jack", "jack",
         10, 10, 10, 10,
         9, 9, 9, 9,
         8, 8, 8, 8,
         7, 7, 7, 7,
         6, 6, 6, 6,
         5, 5, 5, 5,
         4, 4, 4, 4,
         3, 3, 3, 3,
         2, 2, 2, 2
         ]

# Calculate the value of a card
def calculateValue(card, total):
    if card == "ace":
        total += 11
        if total > 21: # Takes into account that aces can be worth 1 or 11
            return 1
        else:
            return 11
    if card == "king" or card == "queen" or card == "jack":
        return 10
    else: 
        return card

# Randomly draw a card from the deck
def drawCard(deck):
    card = random.randint(0, (len(deck) - 1))
    return deck[card]

# Ask the player if they want to keep playing
def keepGoing(money):
    while True:
        decision = input("Would you like to play again?  Type n for no and anything else for yes: ")
        if decision == "n":
            print(f"Session ended.  You walked away with: {money}")
            quit()
    