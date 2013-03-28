# Problem 7

# Write and test a function innerProd(x,y) that computes the inner product of two (same length) lists.

def innerProd(x,y):
    sum=0
    for i in range(len(x)):
        sum+=x[i]* y[i]
    return sum

print (innerProd([1,2],[3,5]))