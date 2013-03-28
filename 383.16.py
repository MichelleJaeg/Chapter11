# Problem 16

# Create a class called StatSet that can be used to do simple statistical calculations.

import math


class StatSet:

    def __init__(self):
        a_set=set()
        self.a_set=a_set

    def addNumber(self,x):
        self.a_set.add(x)

    def mean (self):
        sum = 0.0
        for num in self.a_set:
            sum = sum + num
        return sum / len(self.a_set)

    def median (self):
        # put items in list and sort
        list=[]
        for item in self.a_set:
            list.append(item)
        list.sort()
        # find median
        size = len(list)
        midPos = size //2
        # if the total divided by 2 is even
        if size % 2 == 0:
            median = (list[midPos] + list[midPos-1]) / 2.0
        # if the total divided by 2 is odd
        else:
            median = list[midPos]
        return median

    def stdDev(self):
        sumDevSq = 0.0
        mean = self.mean()
        for num in self.a_set:
            dev = num - mean
            sumDevSq = sumDevSq + dev * dev
        return math.sqrt(sumDevSq/(len(self.a_set)-1))

    def count(self):
        counter=0
        for item in self.a_set:
            counter+=1
        return counter

    def min(self):
        return min(self.a_set)

    def max(self):
        return max(self.a_set)

def main ():
    set=StatSet()
    for i in range(5,15,3):
        set.addNumber(i)
    print (set.mean())
    print (set.median())
    print (set.stdDev())
    print (set.count())
    print (set.min())
    print (set.max())

main ()






