# Problem 5

# Write an algorithm for each of the following Python operations and test your algorithm by writing
# it up in a suitable function. For example, as a function, reverse(myList) should do the same as
# myList.reverse()

def count(myList, x):
    # Like myList.count(x)
    counter = 0
    for item in myList:
        if item == x:
            counter += 1
    return counter

def is_in(myList,x):
    # Like x in myList
    x_in_list = False
    for item in myList:
        if item == x:
            x_in_list = True
            break
    return x_in_list

def index(myList,x):
    # Like myList.index(x)
    index = "Number not in list"
    for i in range(len(myList)):
        if myList[i] == x:
            index = i
            break
    return index

def reverse(myList):
    # Like myList.reverse()
    newList = myList[::-1]
    return newList

def sort(myList):
    # Like myList.sort()
    for i in range(len(myList)-1):
        for j in range(len(myList)-1):
            if myList[j] > myList[j+1]:
                temp = myList[j]
                myList[j] = myList[j+1]
                myList[j+1] = temp
    return myList






