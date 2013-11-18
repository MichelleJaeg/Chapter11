# Problem 13

# Write a program that creates a list of card objects (see Programming Exercise 11 from Chapter 10)
# and prints out the cards grouped by suit and in rank order within suit. Your program should read the list
# of cards from a file, where each line in the file represents a single card with the rank and suit separated by
# a space. Hint: first sort by rank and then by suit.

from cardPoker import Card


def main ():
    # open file
    infile = open("cardsFor13", 'r')
    # create list of card objects
    cardObjects = []
    for line in infile:
        items = line.split()
        rank = int(items[0])
        suit = items[1]
        card = Card(rank,suit)
        cardObjects.append(card)
    # Sort list by rank
    cardObjects.sort(key = Card.getRank)
    # Sort list by suit
    cardObjects.sort(key = Card.getSuit)

    # print out cards
    for card in cardObjects:
        print (card.__str__())

    # Close file
    infile.close()






















if __name__ == '__main__':
    main ()
