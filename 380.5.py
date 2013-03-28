# Problem 5

# Write an algorithm for each of the following Python operations and test your algorithm by writing
# it up in a suitable function. For example, as a function, reverse(MyList) should do the same as
# myList.reverse()

def count(myList, x):
    # Like myList.count(x)
    counter=0
    for item in myList:
        if item==x:
            counter+=1
    return counter

def isin(myList,x):
    # Like x in myList
    xinlist=False
    for item in myList:
        if item==x:
            xinlist=True
    return xinlist

def index(myList,x):
    # Like myList.index(x)
    index="Not in list"
    for i in range(len(myList)):
        if myList[i]==x:
            if index=="Not in list":
                index=i
    return index

def reverse(myList):
    # Like myList.reverse()
    newList=[]
    for item in myList:
        newList.insert(0,item)
    return newList

def sort(myList):
    # Like myList.sort()
    for i in range(len(myList)-1):
        for j in range(len(myList)-1):
            if myList[j]>myList[j+1]:
                temp=myList[j]
                myList[j]=myList[j+1]
                myList[j+1]=temp
    return myList

def main ():
    myList=[4,4,2,2,8,6]
    x=2
    print (count(myList,x))
    print (isin(myList,x))
    print (index(myList,x))
    print (reverse(myList))
    print (sort(myList))

main ()







