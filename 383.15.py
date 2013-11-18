# Problem 15

# Create a class Deck that represents a deck of cards. Your class should contain the following methods:
#constructor
#shuffle
#dealCard
#cardsLeft


from random import shuffle

class Deck:

    def __init__(self):
        deck = []
        self.deck = deck
        for i in range(4):
            if i == 0:
                suit = 'Clubs'
            elif i == 1:
                suit = 'Diamonds'
            elif i == 2:
                suit = 'Hearts'
            elif i == 3:
                suit = 'Spades'
            for j in range(2,15):
                if j == 11:
                    rank = 'Jack'
                elif j == 12:
                    rank = 'Queen'
                elif j == 13:
                    rank = 'King'
                elif j == 14:
                    rank = "Ace"
                else:
                    rank = str(j)
                card = (rank, suit)
                deck.append(card)

    def shuffle(self):
        shuffle(self.deck)

    def dealCard(self):
        card = self.deck[0]
        self.deck.remove(card)
        return card

    def cardsLeft(self):
        counter = 0
        for card in self.deck:
            counter += 1
        return counter


def main ():
    deck = Deck()
    deck.shuffle()
    n = eval(input("How many cards would you like the program to deal? "))
    print ()
    for i in range(n):
        print (deck.dealCard())
main ()



