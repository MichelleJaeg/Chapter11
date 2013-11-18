# Problem 6

# Write and test a function shuffle(myList) that scrambles a list into a random
# order, like shuffling a deck of cards.

from random import randrange

def shuffle (myList):
    newList = []
    for i in range(len(myList)):
        itemToMove = randrange(0, len(myList))
        newList.append(myList[itemToMove])
        myList.pop(itemToMove)
    return newList

print (shuffle([1,2,3,4,5]))
