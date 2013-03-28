# Problem 19

# Create and test a Set class to represent a classical set.

class Set():

    def __init__(self,elements):
        set=[]
        self.set=set
        for item in elements:
            self.set.append(item)

    def addElement(self,x):
        if x not in self.set:
            self.set.append(x)

    def deleteElement(self,x):
        if x in self.set:
            self.set.remove(x)

    def member(self,x):
        return x in self.set

    def intersection(self,set2):
        newSet=[]
        for item in self.set:
            if item in set2:
                newSet.append(item)
        return newSet

    def union(self,set2):
        newSet=[]
        for item in self.set:
            if not item in set2:
                newSet.append(item)
        for item in set2:
            if not item in newSet:
                newSet.append(item)
        return newSet

    def subtract(self,set2):
        newSet=[]
        for item in self.set:
            if not item in set2:
                newSet.append(item)
        return newSet

# testing methods
def main ():
    set=Set([3,4,5])
    set.addElement(7)
    set.deleteElement(3)
    print (set.member(4))
    print (set.member(7))
    print (set.member(3))
    print (set.intersection([5,8]))
    print (set.union([4,8]))
    print (set.subtract([4,5,8]))


main ()