# Problem 8

# Write and test a function removeDuplicates(somelist) that removes duplicate values from a list

def removeDuplicates(somelist):
    for item in somelist:
        total=somelist.count(item)
        if total>1:
            for i in range(total-1):
                somelist.remove(item)
    return somelist

print (removeDuplicates([1,2,4,4,3]))