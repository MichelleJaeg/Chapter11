# Problem 18

# Extend the random walk program from Chapter 9 (Programming Exercise 12) to keep track of how many times
# each square of the sidewalk is crossed. Start your walker in the middle of a sidewalk of length n where n
# is a user input, and continue the simulation until it drops off one of the ends. Then print out the counts of how
# many times each square was landed on.

import random
def main (numtrials):

    #Get input
    n=eval(input("\nHow many squares long would you like the sidewalk to be? "))

    #Simulation
    totalSquaresCount=[]
    for i in range(numtrials):
        location=n/2
        totalSquaresCount.append(location)
        while location>0 and location<n:
            step=random.choice([-1,1])
            location+=step
            totalSquaresCount.append(location)
    for i in range(n):
        total=totalSquaresCount.count(i)
        print (" Square number " + str(i+1)+  " was landed on " + str(total) + " times.")




if __name__=='__main__':
    main (100)