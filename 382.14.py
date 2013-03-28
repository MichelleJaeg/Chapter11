# Problem 14

# Extend the previous program to analyze a list of five cards as a poker hand. After printing the cards, the program
# categorizes accordingly.

from cardPoker import Card

def main ():
    # open file
    infile=open("cardsFor14", 'r')
    # create list of card objects
    cardObjects=[]
    for line in infile:
        items=line.split()
        rank=int(items[0])
        suit=items[1]
        card=Card(rank,suit)
        cardObjects.append(card)
    # Sort list by rank
    cardObjects.sort(key=Card.getRank)
    # Sort list by suit
    cardObjects.sort(key=Card.getSuit)

    # print out cards
    for card in cardObjects:
        print (card.__str__())

    # Analyze hand
    # Flushes
    if (cardObjects[0].getSuit()==cardObjects[1].getSuit()==cardObjects[2].getSuit()
        ==cardObjects[3].getSuit()==cardObjects[4].getSuit()):
            flush=True
    else:
        flush=False
    if flush:
        #Royal Flush
        if (cardObjects[0].getRank()==10 and cardObjects[1].getRank()==11 and cardObjects[2].getRank()==12
            and cardObjects[3].getRank()==13 and cardObjects[4].getRank()==14):
                result='Royal Flush'
        # Straight Flush
        elif (cardObjects[1].getRank()==cardObjects[0].getRank()+1 and cardObjects[2].getRank()==cardObjects[1].getRank()+1
             and cardObjects[3].getRank()==cardObjects[2].getRank()+1 and cardObjects[4].getRank()==cardObjects[3].getRank()+1):
                 result='Straight Flush'
        # Flush
        else:
            result='Flush'
    # Other types of hands
    # Straight
    else:
        cardObjects.sort(key=Card.getRank)
        if (cardObjects[1].getRank()==cardObjects[0].getRank()+1 and cardObjects[2].getRank()==cardObjects[1].getRank()+1
           and cardObjects[3].getRank()==cardObjects[2].getRank()+1 and cardObjects[4].getRank()==cardObjects[3].getRank()+1):
               result = 'Straight'
        else:
            cards=[]
            for card in cardObjects:
                num=card.getRank()
                cards.append(num)
            nums=[]
            for num in cards:
                count=cards.count(num)
                nums.append(count)
            # Four of a Kind
            if max(nums)==4:
                result = 'Four of a Kind'
            elif max(nums)==3:
                # Full House or Three of a Kind
                if nums.count(2)==2:
                    result = 'Full House'
                else:
                    result = 'Three of a Kind'
            elif max(nums)==2:
                # Two Pair or Pair
                if nums.count(2)==4:
                    result = 'Two Pair'
                if nums.count(2)==2:
                    result = 'Pair'
            else:
                # Highest Card
                highestNumber=max(cards)
                if highestNumber==11:
                    highestNumber='Jack'
                elif highestNumber==12:
                    highestNumber='Queen'
                elif highestNumber==13:
                    highestNumber='King'
                elif highestNumber==14:
                    highestNumber='Ace'
                result = str(highestNumber) + ' High'




    # print result
    print ()
    print (result)

    # Close file
    infile.close()






























if __name__=='__main__':
    main ()
