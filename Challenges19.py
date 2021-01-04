#The Primiera

#Primiera (from the french word prime, "prize") is a combination of cards of Scopa, a popular Italian card game.

#For establishing the value of the Primiera, a separate point scale is used for selecting the best cards in the player's deck, in each of the four suits and totaling those four cards point values. A Primiera requires at least one card for each suit, otherwise, it can't be calculated.

##This is the Primiera points scale:

    #7 is worth 21 points.
    #6 is worth 18 points.
    #Ace is worth 16 points.
    #Cards from 2 to 5 are worth 10 points plus the card value.
    #Face cards (Jack, Queen and King) are worth 10 points.

#Create a function that takes in a list representing a cards deck and returns the value of the Primiera.

##Examples
"""
get_primiera_score(["Ad", "7d", "5h", "2c", "Ks"]) ➞ 58
# In the diamonds set 7 is higher than Ace (21 > 16).

get_primiera_score(["2d", "Jd", "7h", "Qc", "5s", "As"]) ➞ 59
# In the diamonds set 2 is higher than Jack (12 > 10), while in
# the spades set Ace is higher than 5 (16 > 15 ).

get_primiera_score(["2d", "Jd", "Qc", "5s", "As"]) ➞ 0
# There aren't cards in the hearts set, so Primiera can't be
# calculated.
"""
##Notes

    #Notation: Ace, card numbers from 2 to 7, Jack, Queen or King + diamonds, hearts, clubs or spades.
    #If one or more seeds are missing from the deck the value of the Primiera is equal to 0.

##Calculation method: 
#Taking the greatest number of the four seeds, of a grain is missing, it returns 0

cards = {
    "7":21, "6":18,
    "A":16, "5":15,
    "4":14, "3":13,
    "2":12, "J":10,
    "Q":10, "K":10}

seeds = ['d','h','c','s']

def get_primiera_score(cards_deck:list) -> int:
    for seed in seeds:
        if seed in [i[1] for i in cards_deck]:
            pass
        else:
            return 0
    d= []
    h= []
    c= [] 
    s= []
    for card in cards_deck:
        if card[1] == 'd':
            d.append(cards[card[0]])
        elif card[1] == 'h':
            h.append(cards[card[0]])
        elif card[1] == 'c':
            c.append(cards[card[0]])
        elif card[1] == 's':
            s.append(cards[card[0]])
    return sorted(d)[len(d) - 1] + sorted(h)[len(h) - 1] + sorted(c)[len(c) - 1] + sorted(s)[len(s) - 1]