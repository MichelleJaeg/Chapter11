from graphics import*

class Card:

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def getRank(self):
        return self.rank

    def getSuit(self):
        return self.suit

    def BJValue(self):
        if self.getRank() == 11:
            return 10
        if self.getRank() == 12:
            return 10
        if self.getRank() == 13:
            return 10
        else:
            return self.getRank()

    def __str__(self):
        rank = self.rank
        if rank == 1:
            rank = "Ace"
        if rank == 2:
            rank = "Two"
        if rank == 3:
            rank = "Three"
        if rank == 4:
            rank = "Four"
        if rank == 5:
            rank = "Five"
        if rank == 6:
            rank = "Six"
        if rank == 7:
            rank = "Seven"
        if rank == 8:
            rank = "Eight"
        if rank == 9:
            rank = "Nine"
        if rank == 10:
            rank = "Ten"
        if rank == 11:
            rank="Jack"
        if rank == 12:
            rank = "Queen"
        if rank == 13:
            rank = "King"


        suit = self.suit
        if suit =='s':
            suit = 'Spades'
        if suit =='c':
            suit = 'Clubs'
        if suit =='h':
            suit ='Hearts'
        if suit =='d':
            suit = "Diamonds"

        return (rank + " of" + " " + suit)

    # For problem 12
    def Draw(self, win, center):
        suit = self.getSuit()
        rank = self.getRank()
        if rank == 11:
            rank = 'j'
        elif rank == 12:
            rank = 'q'
        elif rank == 13:
            rank = 'k'
        else:
            rank = str(rank)
        filename = suit + rank + ".gif"
        card = Image(center, filename)
        card.draw(win)



