import random

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

def calculateValue(card, total):
    if card == "ace":
        total += 11
        if total > 21:
            return 1
        else:
            return 11
    if card == "king" or card == "queen" or card == "jack":
        return 10
    else: 
        return card

def drawCard(deck):
    card = random.randint(0, (len(deck) - 1))
    return deck[card]

def keepGoing():
    while True:
        decision = input("Would you like to play again?  Type 1 for yes and 0 for no: ")
        if decision == 1:
            return True
        elif decision == 0:
            return False
    