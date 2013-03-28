# Problem 1
# "Modify the statistics package from the chapter so that client programs have more flexibility
# in computing the mean and/or standard deviation. Specifically, redesign the library to have the
# following functions:

# mean(nums) Returns the mean of numbers in nums.
# stdDev(num) Returns the standard deviation of nums.
# meanStdDev(nums) Returns both the mean and the standard deviation of nums.


from math import sqrt

def getNumbers():
    nums = []    #start with an empty list

    # sentinel loop to get numbers
    xStr = input ("Enter a number (<Enter> to quit) >> ")
    while xStr != "":
        x = eval(xStr)
        nums.append(x)  # add this value to the list
        xStr = input("Enter a number (<Enter> to quit) >> ")
    return nums

def mean (nums):
    sum = 0.0
    for num in nums:
        sum = sum + num
    return sum / len(nums)

def stdDev(nums):
    #mean
    sum = 0.0
    for num in nums:
        sum = sum + num
    xbar = sum/len(nums)
    # SD
    sumDevSq = 0.0
    for num in nums:
        dev= num - xbar
        sumDevSq = sumDevSq + dev * dev
    return sqrt(sumDevSq/(len(nums)-1))

def meanStdDev(nums):
    #mean
    sum = 0.0
    for num in nums:
        sum = sum + num
    xbar = sum/len(nums)
    # SD
    sumDevSq = 0.0
    for num in nums:
        dev= num - xbar
        sumDevSq = sumDevSq + dev * dev
    SD = sqrt(sumDevSq/(len(nums)-1))
    return xbar, SD


