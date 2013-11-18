# Problem 10

# Write a program that prompts the user for n and then uses the sieve algorithm to find all the primes less than
# or equal to n.

def main ():

    # Introduction
    print ("This program uses the Sieve of Eratosthenes algorithm to find all the prime numbers up to n.\n")

    # Get input
    n = eval(input("Please enter a number. "))

    #create lists
    listOfNumbers = []
    primes = []
    for i in range(2, n + 1):
        listOfNumbers.append(i)

    # while the list is not empty
    while listOfNumbers != []:
        number = listOfNumbers[0]
        # Add the number to the primes list and remove from original list
        primes.append(number)
        listOfNumbers.remove(number)
        # Find numbers that are left that divide evenly by the number
        i = 0
        while i < len(listOfNumbers):
            num2 = listOfNumbers[i]
            if num2 % number == 0 and num2 != number:
                # Remove number
                listOfNumbers.remove(num2)
                i -= 1
            i += 1




    # print results
    print (primes)

main ()



















